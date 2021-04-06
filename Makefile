docker-run: 
	docker run --name camcont --net=host --env="DISPLAY" -it -d --device /dev/dri:/dev/dri --device-cgroup-rule='c 189:* rmw' -v /dev/bus/usb:/dev/bus/usb --privileged --volume="$$HOME/.Xauthority:/root/.Xauthority:rw" opencv-image

docker-stop:
	docker stop camcont
docker-remove:
	docker stop camcont
	docker rm camcont
my-app:
	xhost +
	docker-compose up -d
stop-app:
	docker-compose down
