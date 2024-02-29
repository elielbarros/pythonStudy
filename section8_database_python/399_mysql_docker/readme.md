### How run MySQl using docker-compose ?
- Inside the directory where is the file docker-compose.yml run:
- docker compose up
- To run the container and release terminal use the following command:
- docker compose up -d

#### How stop container?
- docker container stop <container_id>

#### How start container?
- docker container start <container_id>

#### How use env file inside docker compose file?
- First it is necessary to create the file .env
- Write into the .env file the configurations that will be used
- Following the yml structure, after the mysql-server name add the key-value:
```
  mysql-server:
    env_file:
      - .env
```