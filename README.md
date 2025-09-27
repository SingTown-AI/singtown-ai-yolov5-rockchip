## Test

```
# test
python -m singtown_ai.runner --task task.json

# train
python -m singtown_ai.runner --host http://127.0.0.1:8000 --task 6ba7b810-9dad-11d1-80b4-00c04fd430c8 --token 1234567890 --config singtown-ai.json
```

## Docker

```
docker build -t yolov5-rockchip .

docker run -it --rm --network="host" --gpus all yolov5-rockchip:latest python -m singtown_ai.runner --host http://127.0.0.1:8000 --task 6ba7b810-9dad-11d1-80b4-00c04fd430c8 --token 1234567890 --config singtown-ai.json
```
