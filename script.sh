# Script para instalar e configurar commitlint com commitizen

npm i husky --save-dev
npx husky init

npm i @commitlint/cli @commitlint/config-conventional --save-dev
touch commitlint.config.js && echo 'module.exports = { extends: ["@commitlint/config-conventional"] };' >commitlint.config.js

rm .husky/pre-commit
touch ./.husky/commit-msg && echo '#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

npx --no -- commitlint --edit 
' >./.husky/commit-msg && chmod +x ./.husky/commit-msg

touch ./.husky/prepare-commit-msg && echo '#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

exec < /dev/tty && npx cz --hook || true
' >./.husky/prepare-commit-msg && chmod +x ./.husky/prepare-commit-msg

echo '{
  "name": "<project-name>",
  "version": "1.0.0",
  "description": "project-description",
  "repository": "git@github.com:Lucas-PG/<project-name>",
  "author": "Lucas Puhl Gasperin",
  "license": "GPL-3.0-or-later",
  "devDependencies": {
    "@commitlint/cli": "^17.5.1",
    "@commitlint/config-conventional": "^17.4.4",
    "commitizen": "^4.3.0",
    "cz-conventional-changelog": "^3.3.0",
    "husky": "^8.0.3"
  },
  "config": {
    "commitizen": {
      "path": "./node_modules/cz-conventional-changelog"
    }
  },
  "scripts": {
    "prepare": "husky install"
  }
}
' >package.json

npm install
