# Gameflip API

Uma **API wrapper em Python** para utilização com a plataforma Gameflip.
Facilita a integração via script, para automatizar operações, consultar dados e interagir com a Gameflip de forma programática.

## 🧰 Funcionalidades

* Conexão autenticada com a Gameflip via chave e segredo (`API_KEY`, `API_SECRET`)
* Métodos para executar operações comuns (por exemplo: listagem de produtos, criação de ofertas, consulta de histórico)
* Interface simples em Python para agilizar automações
* Código open-source, fácil de estender para necessidades específicas

## 🚀 Começando

### Pré-requisitos

* Python (versão compatível — idealmente 3.7+)
* Conta na Gameflip e acesso à API (chave + segredo)
* Variáveis de ambiente configuradas:

  ```bash
  export GFAPI_KEY=<sua_chave_aqui>
  export GFAPI_SECRET=<seu_segredo_aqui>
  ```

  (No Windows: `set GFAPI_KEY=<…>`, `set GFAPI_SECRET=<…>`)

### Instalação

```bash
pip install -r requirements.txt
```

### Uso básico

Exemplo no arquivo `example.py` (ajuste conforme a sua necessidade):

```python
import datetime
import os
from pprint import pprint

from gameflip_api import GameflipAPI

listing = GameflipAPI.listing_search(digital=True, seller_online_until=datetime.datetime.now())

gameflip_api = GameflipAPI(os.getenv('key_api'), os.getenv('secret'))
pprint(gameflip_api.profile())
```

## 📦 Estrutura do Projeto

* `src/gameflip_api/` — código-fonte da biblioteca
* `example.py` — script de demonstração de uso
* `test.py` — arquivo para testes rápidos
* `requirements.txt` — dependências do Python
* `setup.py` — para empacotamento/distribuição

## 🤝 Contato

Se tiver dúvidas, sugestões ou quiser colaborar:

* Crie uma *issue* no próprio repositório
* Envie um pull request com descrições claras das alterações
