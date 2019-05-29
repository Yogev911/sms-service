# SMS SERVICE - KIN

A REST API for sending sms and keep track on tokens balance (and learn math.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
pip install -r requirments.txt
```

## Deployment

The app is deployed on Heroku on https://yogev-sms-service.herokuapp.com/
and configured to remote SQL server on https://remotemysql.com/

## How does it works??

1. register for new account
2. verify phone number via pin code
3. login to achieve api token
4. send sms
5. earn coins while solving math questions!

## Resources

reveal the resources via [Swagger-ui](https://petstore.swagger.io/?_ga=2.81673303.1376567865.1559094208-243859538.1559094208#/)
just insert the url https://yogev-sms-service.herokuapp.com/api/swagger.json and explore

## Built With
* **Flask Framework**
* **Nexmo sms adapter**
* **SQL server**
* **LOVE**

## Author

* **Yogev Heskia**  [GitHub](https://github.com/yogev911) [LinkedIn](https://www.linkedin.com/in/yogevh/)

## License

This project is licensed under the MIT License
