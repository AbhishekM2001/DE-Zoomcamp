Using Kestra for Workflow Orchestration

Kestra is an all in 1 orchestration too;
- no code,low code and full code options available

Command to install and run kestra
docker run --pull=always --rm -it -p 8080:8080 --user=root -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp kestra/kestra:latest server local