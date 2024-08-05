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

## First Workflow

`workflow_dispatch` lets to start workflow manually.

```yml
name: First Workflow
on: workflow_dispatch
```

<img src="https://docs.github.com/assets/cb-72692/mw-1440/images/help/actions/overview-github-hosted-runner.webp" width=350>

