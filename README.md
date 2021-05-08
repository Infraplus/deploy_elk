# ELK docker POC

## Sample app

### Build

In docker folder you will find the `helloworld.py` file and the `Dockerfile` to build our test app.


### How it works

We will use a simple flask app that listens `GET` requests on port `:5000`.

Example:

Let's say our swarm manager node ip is 192.168.10.10 and the application bind port is 5000:5000

1.

`curl 192.168.10.10:5000/helloworld` -> return -> `Hello Stranger`

2.

`curl 192.168.10.10:5000/helloworld?name=SalmenHitana` -> return -> `Hello Salmen Hitana`
