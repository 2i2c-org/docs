# Features

This page lists all the features our hubs can provide you. 

## Authentication

These login methods are supported currently:

- Google Auth
- GitHub Auth

2i2c maintains a list of 'admins' for each hub, and they can manage
the active list of users who can log in at any time.

We also support *ephemeral* hubs, which are mybinder.org-like - they
let anyone log in without needing any authentication, and provide no
persistence.

## Admin access

Each hub has a list of 'admins', who can do the following actions:

1. Add / remove users who can log in
2. Write to `~/shared-readwrite` folder, which is then readable at `~/shared` for everyone else
3. Access any user's home directory & notebook server via the admin panel

## User Environment

We have a basic one fit for education, and you can bring your own -
any docker image would do. Currently, any updates to the docker image
used will need to be changed as a PR in the 2i2c repo.

## Home directories

Each user gets a persistent directory at `$HOME`.

## Shared directory

Each hub has a `~/shared` readonly directory where common datasets & code can be provided to all users. Admins also have a `~/shared-readwrite` directory that is writeable. Anything admins put in `~/shared-readwrite` will show up immediately in `~/shared`

## Hub home page

Currently, you can customize the following in your home page:

1. Logo
2. Link to your project
3. Information about who is funding the hub, running the hub & designing the hub

## dask-gateway

Available only on 'dask' hubs.

A [dask-gateway](https://gateway.dask.org/) cluster, backed by a pre-emptible node pool for your dask workers.

## Scratch Bucket

Available only on 'dask' hubs.

A GCS bucket is provisioned for each hub, and all users can use it as a
'scratch' space for intermediate results. It's wiped every 7 days automatically. Can be accessed via the env variable `$SCRATCH_BUCKET` or `$PANGEO_SCRATCH`
