# flask-api

Para criar a imagem:
$ docker image build --tag flask .

Para listar as imagens:
$ docker image ls

Para criar e iniciar o container:
$ docker container run --detach -p 80:5000 --name flask flask
