import boto3
import time

AWS_ACCESS_KEY='XXX'
AWS_SECRET_KEY='XXX'
active_grp_arn = 'arn:aws:elasticloadbalancing:us-east-1:906389069312:targetgroup/active-target-group/991e59aec66ec693'
passive_grp_arn = 'arn:aws:elasticloadbalancing:us-east-1:906389069312:targetgroup/passive-target-group/c5a15d864b879c76'
listener_arn = 'arn:aws:elasticloadbalancing:us-east-1:906389069312:listener/app/active-demo-app-lb/8125019f6edacba1/b10b3d19cfa70b82'

client = boto3.client('elbv2',aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY,region_name='us-east-1')


def is_active_grp_serving_traffic():
    response = client.describe_listeners(ListenerArns=[listener_arn])
    print(response)
    current_target_grp = response['Listeners'][0]['DefaultActions'][0]['TargetGroupArn']
    if 'active-target-group' in current_target_grp:
        return True
    else:
        return False

def modify_listener(new_arn):
    response = client.describe_listeners(ListenerArns=[listener_arn])
    print(response)
    response = client.modify_listener(ListenerArn=listener_arn,
                                      DefaultActions=[{
                                          'Type':'forward',
                                          'ForwardConfig':{
                                                "TargetGroups": [
                                                    {
                                                        "TargetGroupArn": new_arn,
                                                        "Weight": 1
                                                    },
                                                ],
                                                "TargetGroupStickinessConfig": {
                                                    "Enabled": False
                                                }
                                            }
                                      }])
    print(response)

active_grp_healthy = True
current_traffic_to_active_dc = is_active_grp_serving_traffic()

while True:
    response = client.describe_target_health(TargetGroupArn=active_grp_arn)
    status = response['TargetHealthDescriptions'][0]['TargetHealth']['State']
    print(response)
    if status != 'healthy':
        print("Active target group is unhealthy")
        active_grp_healthy = False
    if status == 'healthy':
        print('Active group is healthy')
        active_grp_healthy = True
    if not active_grp_healthy and current_traffic_to_active_dc:
        print("Routing traffic to passive DC")
        modify_listener(passive_grp_arn)
        current_traffic_to_active_dc = False
    if active_grp_healthy  and not current_traffic_to_active_dc:
        print("Switching traffic back to active DC")
        modify_listener(active_grp_arn)
        current_traffic_to_active_dc = True
    time.sleep(10)