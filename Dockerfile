FROM ubuntu:16.04
RUN apt-get update -y && apt-get install -y python3-pip python3-dev
COPY ./ ./app
WORKDIR ./app
RUN pip3 install -r ./app/requirements.txt
EXPOSE 8080
CMD ["python", "api.py"]