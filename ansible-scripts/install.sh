#!/bin/bash
echo "Hello, world!" > /home/ec2-user/myfile.txt
sudo yum update -y
sudo yum -y install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo chmod 666 /var/run/docker.sock
docker run -d -p 8000:5000 --env-file ./.db_details pratik151/3-tier-app-demo