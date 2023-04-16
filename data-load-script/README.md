# 3-tier-app-demo data load

This script is used to load data from excel file to mysql database.

Commands to run:
- docker build --tag pratik151/3-tier-app-demo-loaddata . --platform linux/amd64
- docker run --env-file=.db_details pratik151/3-tier-app-demo-loaddata