# Guia de Uso da API com Docker

Este documento apresenta instruções detalhadas sobre como executar a API de Pessoas usando Docker.

## Pré-requisitos

- Docker instalado (versão 19.03.0+)
- Docker Compose instalado (versão 1.27.0+)

## Execução com Docker Compose (recomendado)

O Docker Compose facilita a execução da aplicação, gerenciando a construção da imagem e a execução do container.

### Iniciar a API

```bash
# No diretório raiz do projeto
docker-compose up -d
```

O parâmetro `-d` permite executar o container em segundo plano.

### Visualizar logs

```bash
docker-compose logs -f
```

O parâmetro `-f` permite acompanhar os logs em tempo real.

### Parar a API

```bash
docker-compose down
```

## Execução com Docker diretamente

Caso prefira usar o Docker sem o Compose, siga as instruções abaixo:

### Construir a imagem

```bash
docker build -t pessoas-api .
```

### Iniciar o container

```bash
docker run -d -p 8000:8000 --name pessoas-api pessoas-api
```

Parâmetros:
- `-d`: Executa o container em segundo plano
- `-p 8000:8000`: Mapeia a porta 8000 do container para a porta 8000 do host
- `--name pessoas-api`: Define um nome para o container

### Visualizar logs

```bash
docker logs -f pessoas-api
```

### Parar e remover o container

```bash
docker stop pessoas-api
docker rm pessoas-api
```

## Acessando a API

Após iniciar o container, a API estará disponível em:

- Documentação Swagger: http://localhost:8000/docs
- Documentação ReDoc: http://localhost:8000/redoc
- Endpoints da API: http://localhost:8000/api/...

## Desenvolvimento com Docker

Para desenvolvimento, use o volume definido no docker-compose.yml, que permite alterar o código sem reconstruir a imagem:

```yaml
volumes:
  - .:/app
```

As alterações no código serão refletidas imediatamente graças ao parâmetro `reload=True` usado no Uvicorn.

## Solução de problemas

### Porta já em uso

Se a porta 8000 já estiver em uso, você pode alterá-la no docker-compose.yml:

```yaml
ports:
  - "8001:8000"  # Altera para porta 8001 no host
```

### Container não inicia

Verifique os logs para identificar o problema:

```bash
docker-compose logs
# ou
docker logs pessoas-api
```

### Permissões de arquivo

Em sistemas Linux/macOS, pode ser necessário ajustar permissões:

```bash
chmod -R 755 .
``` 