# nipybuilder
Automated NiFi flow design in Python

Initial version development is in progress.






## Getting Started





## Setting Up NiFi Sandbox

### Running NiFi in a Docker Container

The easiest way to setup a NiFi sandbox is to create a Docker container. 

```bash
docker run --rm -d -p 8080:8080 --name nifi apache/nifi:1.8.0 -c 'env | grep NIFI'
```

To stop NiFi Docker container:

```bash
docker stop nifi
```

Alternatively you could stop NiFi and the docker container will exit:

```bash
docker exec nifi /opt/nifi/nifi-current/bin/nifi.sh stop
```

### Install and Run NiFi

You could also install NiFi on a machine, e.g. your local computer or virtual machine on the cloud. Follow the instructions the [Getting Started with Apache NiFi](http://nifi.apache.org/docs/nifi-docs/html/getting-started.html) page from the NiFi website.

