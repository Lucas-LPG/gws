# ∞ Gasperin Web Services

## Começando

Esse repositório se refere ao trabalho semestral da matéria **experiência criativa**.

- Grupo:
  - Lucas Puhl Gasperin
  - Tiago de Brito Follador
  - Renan Pamplona
  - Renan Czervinski
- Tema: Controle remoto de portas e dispositivos de ventilação e regulação de temperatura no SUS.

### Requirements

Para instalar as depêndencias desse projeto basta executar:

```bash

pip install -r requirements.txt

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

## Requisitos de entrega do Projeto

O que deverá ser entregue:

- Deverá ser uma continuação da aplicação Web apresentada no PJBL2.
- Deve ser utilizado o SQL Alchemy para realizar a interação com o banco de dados MySQL.
- A aplicação deve conter:

  - Flask Login com autenticação de seção para todas as páginas.
  - Classificação de usuário com Flask Role ou condições com pelo menos 3 tipos diferentes de usuário com operações distintas: Admin, Estatístico, Operador.
  - Usuário admin poderá:
    - Cadastrar usuários;
    - Cadastrar kits;
    - Editar usuários;
    - Editar kits;
    - Deletar Usuários;
    - Deletar kits;
  - Usuário Admin/Estatístico poderá:
    - Visualizar dados em tempo real vindo do MQTT broker;
    - Acesso a tela com dados históricos dos sensores;
  - Usuário Admin/Operador:
    - Acesso a tela de comandos remotos;
    - Acesso a tela de dados históricos de atuações remotas;
  - Usuário Admin/Estatístico/Operador:
    - Pode fazer o logout do sistema.

- Requisitos adicionais:

  - Nas telas de aplicações, o usuário poderá selecionar um período de tempo, e o sistema deverá retornar informações dos sensores/atuadores selecionados para este período. O sistema deverá demonstrar os valores em forma de tabela ou gráfico.
  - Haverá conexão com algum MQTT broker para recebimento e envio de informações
  - Ao cadastrar sensores/atuadores/kits, o sistema deverá salvar automaticamente os valores na tabela de dados brutos.

## Nomenclatura

**Nota**: esse bloco é somente uma informação extra, ou uma curiosidade sobre nosso nome e logo.

O nome _Gasperin_ é derivado de _Gaspar_ ou _Caspar_, um dos Três Reis Magos na tradição cristã. Este nome está geralmente associado à palavra persa "Gizbar" (גִּזְבָר), que significa "portador de tesouros" ou "guardião". Em hebraico, a palavra também possui o mesmo significado, reforçando a ideia de proteção e cuidado.

Assim, o nome _Gasperin_, por sua conexão com um dos Reis Magos, evoca sabedoria e generosidade. Estes valores são centrais para nossa empresa, que busca constantemente inovar para beneficiar a todos. O símbolo do infinito (∞), que escolhemos para nos representar, também está associado à sabedoria e ao espiritualismo, complementando perfeitamente nossa missão e visão.

Portanto, _Gasperin_ é um nome que reflete nosso compromisso com a inovação, sabedoria e generosidade, valores que estão no coração de tudo o que fazemos.
