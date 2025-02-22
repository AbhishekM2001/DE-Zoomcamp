## Module Development Flow-
- First started postgres in a docker container and ingested the dataset (yellow taxi tripdata) in the database using upload-data.ipynb in jupyter notebook. Here we also used pgcli to connect and query the database from command prompt
- Modified the upload-data file to ingest data from local machine by using ingest_data.py file
- Next we started pgadmin in a separate docker container and connected to the postgres database.
- we dockerized the script by adding info of both images in docker-compose.yaml file

## Module Process Flow-
- Initially both containers were started using their own docker run commands (present in docker-compose.yaml) and Dockerfile was created that contained some configuration and run the pipeline script (ingesting data).
- After dockerization, both containers were started and ingestion scipt was run using 'docker-compose up' command 

## Important Docker commands-
- docker ps -> show running containers
- docker ps -a -> show all containers (running/terminated)
- doker network create -> run 2 containers in same network
- docker build -> To build docker image on a folder that will use Dockerfile
- docker run -> To run docker image, use -i for continuing to use terminal after command run
- use --entrpoint=bash for using bash terminal in container
- docker-compose up -> To run docker image using docker-compose.yaml file (use -d to continue to use terminal)
- docker-compose down -> To stop containers


## What is Terraform
Terraform is a Infrastructure as Code tool to manage resources in cloud

## Why Terraform
- Simplicity in keeping track of infrastructure
- Easier collaboration
- Reproducibility
- Ensure resources are removed

## What Terraform is not
- Does not manage and update code on infrastructure
- Does not give you ability to change immmutable resources
- Not used to manage resources not defined in your terraform files

The videos are not full course on terrform but just an introduction to terraform

## What are providers
Code that allows terraform to commmunicate and manage resources

## Key Terraform commands
- Init- Get me the providers I need
- Plan- What I am about to do
- Apply- Do what is in the tf files
- Destroy- Remove everything in the tf files
