## Configurando o ambiente no seu note

Primeiramente instale Pyenv e Poetry (Pode ver no vídeo: https://www.youtube.com/watch?v=-Pi5AmOfL2s&t=1587s)

Vamos instalar o python 12 com o pyenv:

```bash
pyenv update
pyenv install 3.12:latest
```

O Poetry já cria uma estrutura automática para nosso preto

```bash
poetry new fast_zero
```

A estrututa fica:

```bash
├── fast_zero
│   └── __init__.py
├── pyproject.toml
├── README.md
└── tests
    └── __init__.py

```

Entre no diretório:

```bash
cd fast_zero
```

No pyproject.toml, é preciso trocar a versão para `3.12.*`:

```bash
  GNU nano 6.2                pyproject.toml                          
[tool.poetry]
name = "fast-zero"
version = "0.1.0"
description = ""
authors = ["Vinícius <vini8cs@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "3.12.*"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

```

E agora vamos utilizar o pyenv com a versão do python que o pyenv baixou. No nosso caso foi 3.12.4:

```bash
pyenv local 3.12.4
```

## Criando o ambiente

No diretório onde estiver nosso pyproject.toml. vamos fazer o próximo passo:

```bash
poetry install
```

## Intalando o FastAPI

Como instalar o FastAPI usando o poetry:

```bash
poetry add fastapi
```

Agora nosso `pyproject.toml` vai estar atualizado com o fastapi e suas dependências:

```bash
[tool.poetry]

name = "fast-zero"

version = "0.1.0"

description = ""

authors = ["Vinícius <vini8cs@gmail.com>"]

readme = "README.md"

  

[tool.poetry.dependencies]

python = "3.12.*"

fastapi = "^0.111.0"

  
  

[build-system]

requires = ["poetry-core"]

build-backend = "poetry.core.masonry.api"
```

Todas as dependências foram instaladas no arquivo `poetry.lock`

Quando for comitar, o .lock tem sempre que estar junto

## Começando com o FastAPI

Agora a primeira coisa que vamos fazer é criar um script em python `app.py`:

```python
def read_root():
	return {"message": "Hello Zwardoooo!"}
```

e executar no terminal de forma interativa:

```bash
python -i fast_zero/app.py
```

La dentro, conseguimos chamar o read_root()