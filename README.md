## Task
1. Write a Flask API in Python to expose 2 endpoints-
/healthcheck: returns "Healthy" with code 200.
/gcd: accepts a JSON with 2 keys x and y. Returns the GCD of the two numbers.

2. Write a Dockerfile to be used to build the docker container that exposes this API to the internet
3. Send Python code, Dockerfile and requirements files

## Solution 

### Introduction

This Flask API provides two endpoints:

* `/healthcheck`: Returns the server's health status.
* `/gcd`: Accepts two numbers in json format and returns their greatest common divisor (GCD).


### Build and run docker image  

1. Build the Docker image:

```
docker build -t gcd-flask-api:v1.0.0 .
```
2. Run the container:

```
docker run -d -p 3000:3000 gcd-flask-api:v1.0.0
```

### Using the API


Access URL : http://localhost:3000/healthcheck to confirm application health status

```
curl http://localhost:3000/healthcheck

```

Examples for GCD Calculation

```
$  curl -X POST http://localhost:3000/gcd      -H "Content-Type: application/json"      -d '{"x": 81, "y": 27}'
{"gcd":27}
$ curl -X POST http://localhost:3000/gcd       -H "Content-Type: application/json"      -d '{"x": 12, "y": 8}'
{"gcd":4}
$ curl -X POST http://localhost:3000/gcd       -H "Content-Type: application/json"      -d '{"x": 48, "y": 180}'
{"gcd":12}
$ curl -X POST http://localhost:3000/gcd       -H "Content-Type: application/json"      -d '{"x": 42, "y": 56}'
{"gcd":14}
$ curl -X POST http://localhost:3000/gcd       -H "Content-Type: application/json"      -d '{"x": 7, "y": 13}'
{"gcd":1}
```

