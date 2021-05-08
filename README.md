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

## ELK Stack

Before running the `ELK` stack please be sure to have `vm.max_map_count` variable set to `262144` on all your swarm nodes.

`sudo sysctl -w vm.max_map_count=262144`

### Volumes

By default the `docker-compose` file will search for the `logs`, `fluent-config` and `es-vol` directories as bind volumes in `elk` folder, their path will be marked in the `docker-compose file`. Please make sure you create the directories on your NFS partitions and modify the `source` field that corresponds to the bind volumes. The `fluent-config` contains the 2 config files needed for the log collector to work properly: 1. `fluent-bit.conf` and 2. `parsers.conf`, please make sure to copy them into the newly created directories on your NFS partitions.

All applications that we want to collect the logs from should have their logs directories attached to the `logs` volume of the fluent-bit.

#### ElasticSearch volume

```
  volumes:
    - type: bind
      source: ./es-vol
      target: /usr/share/elasticsearch/data
```

#### Fluent-bit volumes

```
  volumes:
    - type: bind
      source: ./logs
      target: /var/log
    - type: bind
      source: ./fluent-config
      target: /fluent-bit/etc
```

![alt text](readme_img/binding.png?raw=true "Volume Binding")

After this just run docker-compose file

