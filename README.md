# Passo a passo para o projeto rodar

## DATABASE

No MySQL Workbench, com o MySQL rodando, rode o script:

```sql
DROP DATABASE IF EXISTS puhl_gasperin_health;
CREATE DATABASE puhl_gasperin_health;
USE puhl_gasperin_health;
DROP USER IF EXISTS 'lucas'@'%';
CREATE USER lucas IDENTIFIED BY "lucas";
GRANT ALL ON *.* TO lucas WITH GRANT OPTION;
```

## Rodando a aplicação

Basta executar o app.py. Pode ser necessário utilizar uma versão Python3 mais antiga
