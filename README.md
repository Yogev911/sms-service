# SMS SERVICE - KIN

A REST API for sending sms and keep track on coin balance (and learn math).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
1. git
2. docker

## Service Deployment
1. Set up a SQL server and run the `init-db.sql` script for initialize the db schemes
2. Create and account on `https://www.nexmo.com/` and get the KEY and SECRET passwords
3. Set up a AWS server (optional)
4. Clone the source project And build an docker image of the project (optional)
```
git pull https://github.com/Yogev911/sms-service.git

docker build -t sms-service:vx.x.x 
```

Or pull the latest image from the Docker hub (recommended)
```
docker pull yogev911/sms-service
```

5. Run the container
```
docker run --detach -p 5000:5000 --env DB_PORT=**** --env DB_HOST=**** --env DB_SCHEMA=**** --env DB_PASSWORD=**** --env DB_USER=**** --env NEXMO_SECRET=**** --env NEXMO_KEY=**** --env API_TOKEN_KEY=**** sms-service:latest
```
####clarifications:
--detach will run the container in background

-p 5000:5000 will bind the port 5000 to the container where the app is listening

--env are the env variable that get from the sql server and nexmo

the --env API_TOKEN_KEY=**** will be a string what ever you like for the JWT encryption and decryption


## Swagger-ui deployment
SMS-SERVICE is using swagger API documentation
to reveal the API docs there's a need to use a swagger-ui

```
docker pull swaggerapi/swagger-ui

docker run -p 80:8080 swaggerapi/swagger-ui

open http://localhost
```
for more info `https://hub.docker.com/r/swaggerapi/swagger-ui/` and `https://swagger.io/tools/swagger-ui/`

## How it works
basic flow:

1. register for new account
`curl -X POST "http://ec2-3-17-178-119.us-east-2.compute.amazonaws.com:5000/register" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"user\": \"IamAnewUser\", \"password\": \"mypassword\", \"phone\": \"9728282663\"}"`

2. verify phone number via pin code - the registered phone number will receive a text message with a PIN code
`curl -X PUT "http://ec2-3-17-178-119.us-east-2.compute.amazonaws.com:5000/verify/IamAnewUser/6666" -H "accept: application/json"`

3. login to achieve API token 
`curl -X POST "https://ec2-3-17-178-119.us-east-2.compute.amazonaws.com:5000/login" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"user\": \"IamAnewUser\", \"password\": \"mypassword\", \"phone\": \"9728282663\"}"`

4. send sms
`curl -X POST "http://ec2-3-17-178-119.us-east-2.compute.amazonaws.com:5000/send" -H "accept: application/json" -H "token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJwaG9uZSI6Ijk3MjUyODI4MjY2MyIsImV4cCI6MTU1OTQ4NTMxMn0.R0E83enfbIfPPbdNH0ZWp6pnXSdk8mP3EZkFwORUiv0" -H "Content-Type: application/json" -d "{ \"msg\": \"this is a new message\", \"dest\": \"9728282663\"}"`

5. get math question for achieve coins
`curl -X GET "http://ec2-3-17-178-119.us-east-2.compute.amazonaws.com:5000/puzzle" -H "accept: application/json" -H "token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJwaG9uZSI6Ijk3MjUyODI4MjY2MyIsImV4cCI6MTU1OTQ4NTMxMn0.R0E83enfbIfPPbdNH0ZWp6pnXSdk8mP3EZkFwORUiv0"`

6. submit an answer for math question
`curl -X PUT "http://ec2-3-17-178-119.us-east-2.compute.amazonaws.com:5000/puzzle" -H "accept: application/json" -H "token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJwaG9uZSI6Ijk3MjUyODI4MjY2MyIsImV4cCI6MTU1OTQ4NTMxMn0.R0E83enfbIfPPbdNH0ZWp6pnXSdk8mP3EZkFwORUiv0" -H "Content-Type: application/json" -d "{ \"answer\": \"14\"}"`

7. check current coins balance
`curl -X GET "http://ec2-3-17-178-119.us-east-2.compute.amazonaws.com:5000/user/balance" -H "accept: application/json" -H "token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJwaG9uZSI6Ijk3MjUyODI4MjY2MyIsImV4cCI6MTU1OTQ4NTMxMn0.R0E83enfbIfPPbdNH0ZWp6pnXSdk8mP3EZkFwORUiv0"`

## Tests
Each component has an `test.py` file that contains unittests for the component

Coverage 100%

## Code Documentations
Each function starts with DocString that explains the usage and output

## Exceptions
This project contains a `exception.py` file that defines app custom exceptions

## Built With
* **AWS**
* **Flask Framework**
* **unittest**
* **Nexmo sms adapter**
* **SQL server**
* **LOVE**

## Author

* **Yogev Heskia**  [GitHub](https://github.com/yogev911) [LinkedIn](https://www.linkedin.com/in/yogevh/)

## License

This project is licensed under the MIT License
