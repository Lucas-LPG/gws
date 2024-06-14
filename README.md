# ∞ Gasperin Web Services

## Começando

### Sobre o Projeto

Este repositório refere-se ao trabalho semestral da matéria **Experiência Criativa**. O projeto visa desenvolver uma solução inovadora para o controle remoto de portas, dispositivos de ventilação e sistemas de regulação de temperatura, com foco inicial no Sistema Único de Saúde (SUS).

### Grupo

- Lucas Puhl Gasperin
- Tiago Follador
- Renan Pamplona
- Renan Czervinski

### Tema

Controle remoto de portas e dispositivos de ventilação e regulação de temperatura no SUS.

### Nossa Empresa

Para concretizar este projeto, criamos a **Gasperin Web Services**, uma empresa dedicada a fornecer soluções inovadoras para a gestão remota de atuadores e sensores via web. Nosso objetivo é oferecer uma plataforma robusta e intuitiva que permita a automatização e o controle eficiente de diversos dispositivos, beneficiando não só o SUS, mas também outros setores que necessitam de soluções similares.

### Objetivos da Gasperin Web Services

- **Inovação:** Desenvolver tecnologias avançadas que facilitem o controle remoto de diversos dispositivos.
- **Eficiência:** Melhorar a gestão e o uso de recursos em instituições de saúde e outros clientes.
- **Segurança:** Garantir que todos os sistemas operem de forma segura e confiável, protegendo os dados e a privacidade dos usuários.
- **Sustentabilidade:** Promover soluções que contribuam para a redução do consumo energético e o impacto ambiental.

### Público-Alvo

Embora o foco inicial seja o SUS, as soluções da Gasperin Web Services são versáteis e podem ser aplicadas em diferentes setores, como:

- Hospitais e clínicas
- Instituições educacionais
- Edifícios comerciais e residenciais
- Indústrias

Esperamos que este projeto contribua significativamente para a modernização e melhoria dos serviços oferecidos pelo SUS, bem como inspire outras instituições a adotar tecnologias inovadoras para a gestão eficiente de seus recursos.

## Requisitos

Para instalar as depêndencias desse projeto basta executar:

```bash

pip install -r requirements.txt

```

**NOTA**: Erros do tipo `modulo x não encontrado` normalmente significam que o _pyhton interpreter_ sendo utilizado não possui acesso ao modulo em questão. Para resolver, tente alterar o _interpreter_ para uma versão mais antiga.

## Estrutura do Projeto

O projeto segue a arquitetura _MVC_: _Models_, _Views_, _Controllers_. A estrutura de diretórios é a seguinte:

```text
.
├── controllers
├── db
├── models
├── static
│   ├── css
│   ├── img
│   └── js
└── views
    ├── actuators
    ├── errors
    ├── layouts
    ├── sensors
    └── users

```

- Controllers: rotas da aplicação
- Db: Funções e arquivos relacionados ao banco de dados.
- Models: Classes/Tabelas do banco de dados.
- Static: Arquivos estáticos: Imagens, Css, JavaScript
- views: Templates _html_ integrados com jinja2.

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

## Contriubuindo

### Configurando seu ambiente de trabalho

1. Clone este repositório para sua máquina
2. Opcionalmente, ative o [commitlint](https://github.com/conventional-changelog/commitlint) e
   o [commitzen](https://github.com/commitizen/cz-cli) no repositório:

   1. Instale [`npm e node`](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm);
   2. Na pasta do repositório, rode:

      ```shell
      npm install
      ```

   3. Esta configuração não é obrigatória, mas **fortemente** recomendada;
   4. O commitzen não integra com o VS Code, para uso no editor considere
      [instalar uma extensão](https://github.com/commitizen/cz-cli#adapters).

[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)

## Nomenclatura

**Nota**: esse bloco é somente uma informação extra, ou uma curiosidade sobre nosso nome e logo.

O nome _Gasperin_ é derivado de _Gaspar_ ou _Caspar_, um dos Três Reis Magos na tradição cristã. Este nome está geralmente associado à palavra persa "Gizbar" (גִּזְבָר), que significa "portador de tesouros" ou "guardião". Em hebraico, a palavra também possui o mesmo significado, reforçando a ideia de proteção e cuidado.

Assim, o nome _Gasperin_, por sua conexão com um dos Reis Magos, evoca sabedoria e generosidade. Estes valores são centrais para nossa empresa, que busca constantemente inovar para beneficiar a todos. O símbolo do infinito (∞), que escolhemos para nos representar, também está associado à sabedoria e ao espiritualismo, complementando perfeitamente nossa missão e visão.

Portanto, _Gasperin_ é um nome que reflete nosso compromisso com a inovação, sabedoria e generosidade, valores que estão no coração de tudo o que fazemos.
