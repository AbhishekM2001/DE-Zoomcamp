## Docker Development Flow-
- First started postgres in a docker container and ingested the dataset (yellow taxi tripdata) in the database using upload-data.ipynb in jupyter notebook. Here we also used pgcli to connect and query the database from command prompt
- Modified the upload-data file to ingest data from local machine by using ingest_data.py file
- Next we started pgadmin in a separate docker container and connected to the postgres database.
- we dockerized the script by adding info of both images in docker-compose.yaml file

## Docker Process Flow-
- Initially both containers were started using their own docker run commands (present in docker-compose.yaml) and Dockerfile was created that contained some configuration and run the pipeline script (ingesting data).
- After dockerization, both containers were started and ingestion scipt was run using 'docker-compose up' command 


## Terraform Development Flow-
- Create a service account for your project and download its keys
- Create main.tf containing the configuration for required actions (create/change/delete,etc)
- Move to folder containig main.tf in terminal and store relative path to the downloaded keys in the variable- GOOGLE_CREDENTIALS
- Run the 4 terraform commands in sequence (init, plan, apply, destroy) to make required changes
- use variables to store default values of configuration in a separate file called variables.tf

## Connecting to VM using SSH
- Create SSH keys and add to VM metadata
- Use the below command to access the VM
- Create a config file in .ssh folder which allows to access VM using the command- ssh de-zoomcamp (de-zoomcamp is the host/VM name)

## Command to connect to VM instance
ssh -i ./ssh/GCP Abhishek@[VM external IP]

## Configuring the VM
- Install Anaconda by 
    - Download anaconda using wget download_link
    - Install anaconda using bash file_name 
- Install Docker by
    - Install docker using sudo with these commands-
        - sudo apt-get update
        - sudo apt-gate install
    - Since permission denied due to sudo install, run below commands to add user-
        - sudo groupadd docker
        - sudo gpasswd -a $USER docker
        - sudo service docker restart
- Install Docker-compose by 
    - create bin folder in root and download Docker-compose using wget and save as docker-compose
    - change it to executable using 'chmod +x file_name'
    - set PATH environment variable using 'export PATH="${HOME}/bin:${PATH}" ' so that executables in bin folder can be called from anywhere
- Install pgcli using conda as pip throws errors, use below commands-
    - conda install -c conda-forge pgcli
    - pip install -U mycli
    - start postgres and pgadmin using docker-compose then use pgcli to query postgres
    - Forward port 5432 from VM to local machine to run pgcli locally and access the postgres instance
- Run jupyter notebook in VM. Forward its port 8888 to run notebook locally and ingest data in db
- Install terraform using 'wget download_link'
- Use SFTP to put your SSH keys to a .gc folder in VM 
- Authenticate GCP using the below commands-
    - export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/filename.json (no quotes)
    - gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
- Run terraform commands as desired
- Use 'sudo shutdown now' to shutdown VM. All ssh connections will be closed
- Stopping an instance doesn't charge you for running it but still charges for the storage. Deleting won't charge anything





