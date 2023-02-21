up:
	cd ci && docker-compose up -d

send_10:
	docker exec -it fib_consumer_1 ./sender.py 10

send_100:
	docker exec -it fib_consumer_1 ./sender.py 100

send_56:
	docker exec -it fib_consumer_1 ./sender.py 56

logs:
	docker logs fib_consumer_1 --tail=20

logsf:
	docker logs fib_consumer_1 --tail=20 -f

restart:
	cd ci && docker-compose restart