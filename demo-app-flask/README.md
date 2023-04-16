# 3-tier-app-demo

API:
-
/healthcheck - Returns OK and 200 status if instance is up.

/getallusers - Returns all users data from DB in json format.

/getactiveorpassive - Returns ACTIVE or PASSIVE string based on instance on which requests lands.

Commands to run:
- docker build --tag pratik151/3-tier-app-demo .
- docker run -p 8000:5000 --env-file ./.db_details -e HOST_TYPE=$HOST_TYPE pratik151/3-tier-app-demo