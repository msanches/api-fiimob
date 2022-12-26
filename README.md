# flask-api - Docker container
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

### Para criar a imagem:
```ruby
$ docker image build --tag flask .
```
### Para listar as imagens:
```ruby
$ docker image ls
```
### Para criar e iniciar o container:
```ruby
$ docker container run --detach -p 80:5000 --name flask flask
```

![GitHub Org's stars](https://img.shields.io/github/stars/camilafernanda?style=social)
