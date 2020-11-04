Docker commands

# Build
docker build -t "uol-awd:latest" .

docker build -r "name:tag" [location of dockerfile]

# Start a container

docker run --publish 8000:8080 --name bb bulletinboard:1.0

docker run --publish INPORT:OUTPORT --name [NAME] [CONTAINER NAME:TAG]
--detach if you want this daemonised
-t allocate tty for interactivity and don't halt on completed commands (don't immediately exit)

# List all conatiners

docker ps -a

# Start a stopped container

docker container start [CONTAINER ID]

# stop a CONTAINER

docker container stop [CONTAINER ID]

# remove a CONTAINER

docker container rm [CONTAINER ID]

# attach a shell to a running container

docker exec -ti 844e90af09ef /bin/bash
docker exec -ti [CONTAINER ID] /bin/bash


# List images that could start
docker image list

# remover docker image
docker image rm awd-test-image:latest
docker image rm [NAME:TAG]

# Remove dangling or unused images
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
