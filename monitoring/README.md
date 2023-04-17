# 3-tier-app-demo

Monitoring:
-
For monitoring application we will be using Jaeger which is for monitoring distrubuted traces.

Install Jaeger on host:

- docker run --network=jaeger -d --name jaeger \
  -e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \
  -e COLLECTOR_OTLP_ENABLED=true \
  -p 6831:6831/udp \
  -p 6832:6832/udp \
  -p 5778:5778 \
  -p 16686:16686 \
  -p 4317:4317 \
  -p 4318:4318 \
  -p 14250:14250 \
  -p 14268:14268 \
  -p 14269:14269 \
  -p 9411:9411 \
  jaegertracing/all-in-one:1.44
  
- Application Dockerfile is modified to use this jaeger for posting traces
 Ref: https://github.com/Pratik151/demo-3-tier-app/blob/main/demo-app-flask/Dockerfile
  
- Sample screenshots:

All operations
![All operations](https://github.com/Pratik151/demo-3-tier-app/blob/main/monitoring/All%20operations%20for%20Application.png)

Traces showing error when failed
![Traces showing error when failed](https://github.com/Pratik151/demo-3-tier-app/blob/main/monitoring/Trace%20showing%20error%20traces.png)

Details of Failed transaction
![Details of Failed transaction](https://github.com/Pratik151/demo-3-tier-app/blob/main/monitoring/Detail%20of%20error%20for%20failed%20transaction.png)

Trace showing DB call details
![Trace showing DB call details](https://github.com/Pratik151/demo-3-tier-app/blob/main/monitoring/Trace%20showing%20DB%20calls.png)
