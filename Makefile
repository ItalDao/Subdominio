build:
	docker build -t alcivarimg:1.0.1 .

deploy:
	docker stack deploy --with-registry-auth -c stack.yml alcivar

rm:
	docker stack rm alcivar
