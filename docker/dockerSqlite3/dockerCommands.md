
Here are some additional commands that you may need to run when using Docker:

* `docker info`: display information about how Docker runs on your workstation
* `docker images`: show the Docker images installed on your workstation
* `docker container list`: list the active images running on your workstation
* `docker system prune`: remove many types of "dangling" components from your workstation
* `docker image prune`: remove all "dangling" docker images from your workstation
* `docker container prune`: remove all stopped docker containers from your workstation
* `docker container stop ID`: stop the running container with specified ID
* `docker rmi $(docker images -q) --force`: remove all docker images from your workstation
* `sudo docker image prune -a` : remove all images without at least one container associated to them.
