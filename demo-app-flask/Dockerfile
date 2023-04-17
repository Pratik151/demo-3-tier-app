FROM python:3.8-slim-buster

WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN opentelemetry-bootstrap -a install
COPY . .
ENV FLASK_APP=main.py
CMD [ "opentelemetry-instrument", "--traces_exporter", "console,otlp","--metrics_exporter", "console", "--service_name","demo-app", "--exporter_otlp_endpoint", "jaeger:4317", "--exporter_otlp_traces_insecure","true", "python3", "-m" , "flask", "run", "--host=0.0.0.0"]