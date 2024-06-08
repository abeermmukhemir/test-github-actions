# test-github-actions
This is a personal project to learn and test what can be done with [Github Actions](https://docs.github.com/en/actions).
The goal is to build a basic CI/CD pipeline, that will include build, test, package, and deploy stages. these stages are performed on a simple "hello world" web app written in python.

Note: currently, only the build, test, and release package is implemented, deployment is not implemented yet.

## Workflows implemented
### build-pipeline
This workflow is responsible for two stages: build and test
- **build**: include linting and building the source code for the app, then upload the generated packages to GitHub artifactory.
- **test**: includes downloading the packages we want to test from the artifactory and installing them in the testing environment, then running pytest and coverage.
This pipeline is triggered automatically with every push to the repository.
### release
This workflow is responsible for creating releases of the app. It is run manually whenever we want to cut a new release, we just need to provide the release version and the commit SHA we are targeting.

Running this workflow includes triggering the [build-pipeline](#build-pipeline), then after the testing is done it will create a new release branch and a draft release that includes the tested packages as assets. For better control over releases, the workflow will generate only a draft release which will require manual review and publishing.

...

***For details about the app see [it's README](hello-app/README.md)***
