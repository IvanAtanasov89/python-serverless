# python-serverless

A simple endpoint that returns a red hello. Uses the colorama library just to test using
third party dependencies.

Uses pipenv to create an environment to run tests and uses a serverless plugin to package it up.

e.g.

```shell
# Install serverless and required plugins
npm install
# creates your python env with all packages in it (--dev means to include dev-packages)
pipenv install --dev
# run tests (see scripts section in Pipfile)
pipenv run test
# deploy to aws
pipenv run deploy
```
