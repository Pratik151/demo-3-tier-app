AWS Resource for Demo App

- Create AWS Key-Pair with name test-key for connecting to EC2 instance and copy the downloded key to *3-tier-app-demo/ansible-scripts/test-key.pem*
- Upload resources.yaml to AWS cloudformation and wait for resources to be created. (It can take ~10minutes for RDS master and read replica to be created.)
- AWS Cloudformation stack upload output has DNS of Master and read replica database, one Passive and Active instance IP.
- Copy the host output IP details and replace in *3-tier-app-demo/ansible-scripts/hosts.yml*
- Copy the DB master and read details to *3-tier-app-demo/demo-app-flask/.db_details*

AWS Resources created:
- 

- VPC, Subnet, Security groups
- Application Load Balancer 
- Two EC2 Instances (One Active and one Passive)
- MySQL RDS with one Read Replica