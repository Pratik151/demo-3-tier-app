Ansible scripts for demo

- Copies DB properties file to host.
- Instal docker and start app on each instance

Copy instance ip from cloudformation stack output to hosts.yml (This can be dynamically pulled in future)

- ansible-playbook -i hosts.yml copy-propfile.yml
- ansible-playbook -i hosts.yml deploy-app.yml