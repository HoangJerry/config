# Project Title

About docker

## Getting Started

This is about docker
[https://www.docker.com/](https://www.docker.com/)

### Prerequisites

[https://docs.docker.com/install/](https://docs.docker.com/install/)

Uninstall old versions

```
sudo apt-get remove docker docker-engine docker.io
```

### Installing

```
sudo apt-get update
```

```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

```
sudo apt-key fingerprint 0EBFCD88
```
```
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

```
sudo apt-get update
sudo apt-get install docker-ce
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

```
sudo docker run hello-world
```

## Commandline 

Images list:

```
sudo docker images
```

Delete a images:

```
sudo docker rmi {image_id/name}
```

Running container list:

```
docker ps
```
Stop container list:
```
docker ps -a
```
Remove a container:
```
docker rm -f {container_id/name}
```

Running a container:
```
docker start {new_container_name}
```
Executive a container (using the image):
```
docker exec -it {new_container_name} /bin/bash
```
### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

### Install new ubuntu:
```
sudo docker pull ubuntu:16.04
```
Running
```
sudo docker run -it ubuntu:16.04 /bin/bash
```

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Hoang TN** - *Project Leader* - [HoangJerry](https://github.com/HoangJerry)

## Version
V1.0 last update: Jul 18,2018

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

