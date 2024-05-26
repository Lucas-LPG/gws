# Puhl Gasperin Web Services

## Começando

Esse repositório se refere ao trabalho semestral da matéria **experiência criativa**.

- Grupo:
  - Lucas Puhl Gasperin
  - Tiago de Brito Follador
  - Renan Pamplona
  - Renan Czervinski
- Tema: Controle remoto de portas e dispositivos de ventilação e regulação de temperatura no SUS.

### Requerimentos

Para instalar as depêndencias desse projeto basta executar:

```bash

pip install -r requirements.txt

```

Possívelmente será necessário instalar _pymysql_:

```bash

pip install pymsql

```

**NOTA**: Erros do tipo `modulo x não encontrado` normalmente significam que o _pyhton interpreter_ sendo utilizado não possui acesso ao modulo em questão. Para resolver, tente alterar o _interpreter_ para uma versão mais antiga.

### Estrutura do Projeto

Estrutura do Projeto

```
.
├── controllers
├── db
├── models
├── static
│   ├── css
│   ├── img
│   └── js
└── templates
    ├── actuators
    ├── errors
    ├── layouts
    ├── sensors
    └── users

```

- Controllers: rotas
- Db: Funções e arquivos relacionados ao banco de dados.
- Models: Classes/Tabelas do banco de dados.
- Static: Arquivos estáticos --> Imagens, Css, JavaScript
- Templates: Arquivos _html_

## Execução

Certifique-se de que o _mysql_ esteja rodando no seu dispositivo e execute o arquivo **app.py**, que deve executar todas as operações necessárias para a aplicação automáticamente.
