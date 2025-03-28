bootstrap:
	docker-compose up -d --build

start:
	docker-compose up -d

stop:
	docker-compose down

restart:
	docker-compose restart

logs:
	docker-compose logs -f

reset:
	docker-compose down -v

requirements:
	docker-compose run --rm app pip freeze

shell:
	docker exec -it mycontainer sh 