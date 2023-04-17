# 3-tier-app-demo

This is demo application for 3-tier architecture application.

Technologies used:
- Cloud Platform: AWS
- Web Framework: Flask
- Database: MySQL RDS
- Deployment/Setup Tool: Ansible
- Load Balancer: ALB (Application Load balancer by AWS)
- Monitoring : Opentelemetry traces in Jaeger
- Scripting in Python

Each folder has README.md file for providing more details about specific task. For deploying the application follow below flow:
- Create AWS resources. Refer *aws-resources*
- To load Excel data to DB refer *data-load-script* 
- Refer *ansible-scripts* for setting up docker and running application image
- Application code in *demo-app-flask*
- Refer *monitoring* directory for details about monitoring setup


![Architecture](https://github.com/Pratik151/demo-3-tier-app/blob/main/AWS_Architecture.png)
