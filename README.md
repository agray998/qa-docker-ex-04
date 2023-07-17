# QA-DOCKER-EX-04

This repository is the starting point for exercise 04: building images from a dockerfile  

Included in this repository are a simple flask app which reads some records from an sqlite database and returns them, as well as two sqlite files containing two different datasets  

## Instructions
* Run a container from the image agray998/qa-docker-ex-04:latest - make sure to publish container port 5000 to VM port 80 - curling localhost or navigating to the VM in the browser should then show the data contained in the default database
* Stop and remove this container
* Clone this repository onto a Ubuntu 20.04 VM with Docker installed and configured
* Edit the Dockerfile and add an ENV directive which assigns the value 'test' to a variable called 'DATABASE'
* Re-build the image from the modified dockerfile and run a new container based on the modified image
* Check the data returned by the container again - the app should now be reading from the second dataset, contained in the test database
* Clean up: stop and remove the new container and remove all images
