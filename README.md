# StrongLink
A smarter way of supplying, manufacturing and assuring quality.


# Getting Started: Simulate A Sensor

# Follow these Steps:

* Build the container image
```
    cd sensor
    docker build -t sensor .
```

* Initialize docker swarm orchestrator
```
    docker swarm init
```

* Deploys the sensors on to the swarm (set to 8 sensors). Give a ***<name>*** to the stack of containers.
```
    docker stack deploy -c docker-compose.yaml <name>
```

* View the containers are running
```
    docker stack ps <name>
```

* View the events on the IoT Hub Event watch. Requires you to be logged into the ***avaax7*** account on the az cli.
```
    az iot hub monitor-events --hub-name StrongLink-IoT-Hub --output json
```

* Stop the containers
```
    docker stack rm <name>
```