# FA-GB

## Prerequisites

The following packages must be present:

- Docker 1.10
- docker-compose 1.70

## Unzip the file

Run `tar -zxvf [FA-GB-Framework filename]

## Install

Change the permissions on the `install.sh` so it can be run as a script: Run `chmod 775 install.sh`
Run `./install.sh` to load the Docker images from the bundled `images.tar.gz` file. 
Modify `.env` as required. Look at this file to see what port the UI will be running on.

## Run

Run `docker-compose up -d` to start the application. You can view the logs by running `docker-compose logs -f`.
On your browser, visit `http://localhost:[port number from .env file]`
Use `admin` as the username and `admin` as the password when prompted
