# GitHub Actions Playground (Discovery)
 GitHub Actions Playground (R&D Purposes)

 ## Table Of Content
- [GitHub Actions Playground (Discovery)](#github-actions-playground-discovery)
  - [Table Of Content](#table-of-content)
  - [Purpose](#purpose)
  - [How-To](#how-to)
  - [Findings](#findings)
  - [Pros & Cons](#pros--cons)
    - [Pros](#pros)
    - [Cons](#cons)
  - [Results](#results)
  - [Acknowledgement](#acknowledgement)

## Purpose

* Deploy to Google Cloud Function by using Serverless Framework
* Deploy to specific environment depending on the branch: environment secrets are on the github action settings itself
* Deploy only for the path where file changes occur
* Deployment would not occur for negligible file changes

## How-To 

- Build, Test, Deploy.
- More scenarios need to be discovered: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows

## Findings

- What happens after commits can be automated with "Events", this triggers a workflow, it can be at the scheduled time or when an event outside of GitHub occurs.

## Pros & Cons

### Pros

* Open for 3rd party

### Cons

* Limited to Github

## Results

- Github Action Workflow Result:

![github](/assets/workflow_results.png)

## Acknowledgement

- Thank you Awesome Actions https://github.com/sdras/awesome-actions 