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

## Jobs

1. `if: always()` if this field is specified a job will run irrespective of wether other steps failed or not
2. If a job B is dependent on job A and job A fails, job B does not run
3. But if a job B has `if: always()` condition, irrespective of whether job A was successful or not job B runs

## Steps

1. `env` in a step is local to that step only and not available to other steps
2. **env** can be declared at all three levels and priority increases inwards
3. 3 levels -> workflow, jobs, steps