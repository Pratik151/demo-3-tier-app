ALB Healthchekc Failover script

- ALB doesn't support active/passive and it servers traffic to all healthy instance in target group.
- To replicate Active-Passive case we create two target groups: Active target group and passive target group.
- This script monitors the healthcheck of target groups and modifies listener to switch to passive if it finds active group as unhealthy and switch backs when active group is healthy.

Modify below parameters in main.py from AWS Cloudformation stack output:
- listener_arn
- active_grp_arn
- passive_grp_arn