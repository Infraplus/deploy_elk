# ELK docker POC

## Docker Swarm cluster init

https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/

## GlusterFS install

https://www.scaleway.com/en/docs/how-to-configure-storage-with-glusterfs-on-ubuntu/

## Sample app

### Build

In app folder you will find the `helloworld.py` file, the `Dockerfile` to build our test app and the docker-compose file for the swarm cluster. For the testing purpose, tag the application `hellostranger` when building it.


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

By default the `docker-compose` file inside `elk` folder will search for the `logs`, `fluent-config` and `es-vol` directories as bind volumes, their path must be marked in the `docker-compose file`. Please make sure you create the directories on your NFS/GlusterFS partitions and modify the `source` field that corresponds to the bind volumes. The `fluent-config` contains the 2 config files needed for the log collector to work properly: 1. `fluent-bit.conf` and 2. `parsers.conf`, please make sure to copy them into the newly created directories on your NFS/GlusterFS partitions.

All applications that we want to collect the logs from should have their logs directories attached to the `logs` volume of the fluent-bit.

#### ElasticSearch volume

```
  volumes:
    - type: bind
      source: <GlusterFS mount directory>
      target: /usr/share/elasticsearch/data
```

#### Fluent-bit volumes

```
  volumes:
    - type: bind
      source: <GlusterFS mount directory>
      target: /var/log
    - type: bind
      source: <GlusterFS mount directory>
      target: /fluent-bit/etc
```

![alt text](readme_img/binding.png?raw=true "Volume Binding")


## Deploy

`docker stack deploy -c elk/docker-compose.yml elk`


## Test

For the testing purposes we will run two instances of our test application, check that the source of logs volume is the same as your `fluent-bit` logs volume (see volumes section).

```
  volumes:
    - type: bind
      source: <GlusterFS mount directory>
      target: /home/salmen/logs
```
