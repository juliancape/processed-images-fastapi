bootstrap:
	docker build -t fastpimage .

stop:
	docker stop mycontainer || true
	docker rm mycontainer || true

start:
	docker run -d --name mycontainer -p 80:80 fastpimage

logs:
	docker logs -f mycontainer

reset:
	docker stop mycontainer || true
	docker rm mycontainer || true
	docker rmi -f fastpimage

requirements:
	docker run --rm fastpimage pip freeze
