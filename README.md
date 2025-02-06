# Lean Github Actions

## Elements of Github Actions

1. Workflows
   1. Attached to Repo
   2. Contains one or more Jobs
   3. Triggered upon Events
2. Jobs
   1. Defines Runner
   2. Container one or more Steps
   3. Runs in parallel (Default) or Sequential
   4. Can be conditional
3. Steps
   1. 3rd party Action
   2. Steps are executed in order
   3. Can be conditional


## Run GA Locally

1. To run and test locally use `act -P self-hosted=catthehacker/ubuntu:act-latest`
2. [act](https://nektosact.com/introduction.html) lets you run github actions locally
2. To run specific workflow file `act -P self-hosted=catthehacker/ubuntu:act-latest --input name=me -W .github/workflows/chain-jobs.yml`

## Events

1. Repository Related
    1. push
    2. pull request
    3. branch created
    4. issue opened
2. Others
    1. workflow_dispatch
    2. repository_dispatch -> through rest api call
    3. schedule
    4. workflow_call
3. Has Types and Filters
4. Types could be like if pull request is opned
5. Filter could be like like push event for certain branches. Can also be based on paths, which triggers only if changes in certain folders.
6. Paths ca also be triggerd
7. By default, PR raised from fork repo will not trigger the workflow

## Jobs

1. `if: always()` if this field is specified a job will run irrespective of wether other steps failed or not
2. If a job B is dependent on job A and job A fails, job B does not run
3. But if a job B has `if: always()` condition, irrespective of whether job A was successful or not job B runs
4. Job fails even if one step fails
5. Artifacts and Outputs
6. Cache Dependency

## Steps

1. `env` in a step is local to that step only and not available to other steps
2. **env** can be declared at all three levels and priority increases inwards
3. 3 levels -> workflow, jobs, steps

## [Github Context](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs)

> **Note**: In order to skip the workflow trigerr, the following comming message can be followed "some messae [skip ci]"

## Enviroments

1. Attached to Repository
2. Available in Free Plan for Public Repo
3. Workflow jobs can target environment
4. Environments can have specific secrets

## Conditions

1. On both Jobs and steps
    1. `if`
    2. **if** has 4 special functions
        1. failure -> return true if prev step or job failed
        2. always
        3. success -> return true if prev step or job succeded
        4. cancelled -> return true if prev step or job cancelled
    3. `continue-on-error`
    4. Should be specified on the steps which may fail

## Matrix

1. Defined at Job level
2. Can be used in jobs and steps

## Reusable Workflow

1. Can be used in other workflows
2. Can take inputs and provide outputs as well

## Containers
1. Jobs can be ran on the containers on the vms
2. Service Containers
    1. Can be used for testing like database
    2. Job steps can communicate with the service containers
3. If service container and container for job runned together, then communication between them is super simple. It works similar to docker networking where service container can be accessed by its name.
4. If using only service container then to access this container use localhost:port of the service continer