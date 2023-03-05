## FastAPI + MongoDB

Starting the app:
1) install Git, Docker, Docker-compose and all docker requirements

2) clone repo
   ```commandline
   git clone https://github.com/RautaruukkiPalich/Pali.ch
   ```
3) use command to create and start containers
    ```commandline
    IDE: docker-compose up -d --build
   
    VDS: docker compose up -d --build
    ```

You can stop and start containers with commands:
```commandline
docker-compose start

docker-compose stop
```

be careful with command
```commandline
docker-compose down
```  