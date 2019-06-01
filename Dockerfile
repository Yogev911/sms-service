FROM python:3
RUN apt-get update -y && apt-get install -y python3-pip python3-dev
COPY . /app
WORKDIR /app
RUN pip3 install -r /app/requirements.txt
EXPOSE 5000
CMD ["python", "-u" ,"api.py",  "--host", "0.0.0.0"]