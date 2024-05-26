# ∞ Gasperin Web Services

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

## Nomenclatura

**Nota**: esse bloco é somente uma informação extra, ou uma curiosidade sobre nosso nome e logo.

O nome _Gasperin_ é derivado de _Gaspar_ ou _Caspar_, um dos Três Reis Magos na tradição cristã. Este nome está geralmente associado à palavra persa "Gizbar" (גִּזְבָר), que significa "portador de tesouros" ou "guardião". Em hebraico, a palavra também possui o mesmo significado, reforçando a ideia de proteção e cuidado.

Assim, o nome _Gasperin_, por sua conexão com um dos Reis Magos, evoca sabedoria e generosidade. Estes valores são centrais para nossa empresa, que busca constantemente inovar para beneficiar a todos. O símbolo do infinito (∞), que escolhemos para nos representar, também está associado à sabedoria e ao espiritualismo, complementando perfeitamente nossa missão e visão.

Portanto, _Gasperin_ é um nome que reflete nosso compromisso com a inovação, sabedoria e generosidade, valores que estão no coração de tudo o que fazemos.
