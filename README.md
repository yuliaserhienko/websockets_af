## Python websockets
##### Django channels 2

```text
Websocket server in python continuously sends number (and it's sequence number) sampling from a normal distribution with parameters (0, 1) to websocket client. For each value that over 2 standard deviation range client creates log message that includes a current timestamp, number and and its sequence number. Log masseges reseived by another client and accumulates on web page.
```

```bash
docker-compose build
docker-compose up
```
```http request
http://127.0.0.1:8000/notify/
```
