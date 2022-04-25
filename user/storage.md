# Files and Data in the Cloud

This page describes how files and data storage are handled in 2i2c Hubs.
The high-level summary of recommendations is:
- Use your home directory to store code, notebooks, and small data files (<1 GB)
  for personal use
- Use cloud object storage to store larger datasets and to share data across your team
- Consider whether your project would benefit from other cloud-native data storage
  solutions such as a database, data warehouse, or data lake

:::{admonition} Attribution
The following material was adapted from the
[Pangeo Cloud User Guide](https://pangeo.io/cloud.html)
:::

## Your Home Directory

Your notebook server is a linux "virtual machine" with its own filesystem.
Your are not on a shared server; you are on your own private server.
Your username is ``jovyan``, and your home directory is ``/home/jovyan``.
This is the same for all users.

Your home directory is intended only for notebooks, analysis scripts, and small datasets (< 1 GB).
It is not an appropriate place to store large datasets.
No one else can see or access the files your home directory.

The easiest way to move files in and out of your home directory is via the JupyterLab web interface.
Drag a file into the file browser to upload, and right-click to download back out.
You can also open a terminal via the JupyterLab launcher and use this to ssh / scp / ftp to remote systems.
However, you can’t ssh in!

## The `shared` Directory

All users have a directory called `shared` in their home directory.
This is a *readonly* directory - anybody on the hub can *access* and *read from* the `shared` directory.
The hub administrator may choose to distribute shared materials via this directory.
The `shared` directory is not intended as a way for hub users to share data with each other.

## Using Git / GitHub

The recommended way to move code in and out of the hub is via git / GitHub.
You should clone your project repo from the terminal and use git pull / git push to update and push changes.
In order to push data to GitHub from the hub, you will need to set up GitHub authentication.
[gh-scoped-creds](https://github.com/yuvipanda/gh-scoped-creds/) should be already setup
on your 2i2c managed JupyterHub, and we shall use that to authenticate to GitHub for
push / pull access.

Open a terminal in JupyterHub, run `gh-scoped-creds` and follow the prompts.

Alternatively, in a notebook, run the following code and follow the prompts:

```
import gh_scoped_creds
%ghscopedcreds
```

You should now be able to push to GitHub from the hub! These credentials will expire after
8 hours (or whenever your JupyterHub server stops), and you'll have to repeat these steps
to fetch a fresh set of credentials. Once you authenticate, you'll be provided with a link
to a [GitHub App](https://docs.github.com/en/developers/apps/getting-started-with-apps/about-apps)
that you have to [install](https://docs.github.com/en/developers/apps/managing-github-apps/installing-github-apps)
on the repositories you want to be able to push to from this particular JupyterHub. You only
need to do this once per JupyterHub, and can revoke access any time. You can always provide
access to your own personal repositories, but might need approval from admins of GitHub
organizations if you want to push to repos in that organization.

## Cloud Object Storage

Your hub lives in the cloud.
The preferred way to store data in the cloud is using [cloud object storage](https://aws.amazon.com/what-is-cloud-object-storage/), such as Amazon S3 or Google Cloud Storage.
Cloud object storage is essentially a key/value storage system.
They keys are strings, and the values are bytes of data.
Data is read and written using HTTP calls.

The performance of object storage is very different from file storage.
On one hand, each individual read / write to object storage has a high overhead (10-100 ms), since it has to go over the network.
On the other hand, object storage “scales out” nearly infinitely, meaning that we can make hundreds, thousands, or millions of concurrent reads / writes.
This makes object storage well suited for distributed data analytics.
However, data analysis software must be adapted to take advantage of these properties.

### Cloud-Native Formats

Cloud-native file formats are formats that are designed from the beginning to
work well with cloud object storage.
These formats permit exploration of data and metadata without downloading of the
entire file / dataset and work well with distributed parallel computing.
Here we enumerate some popular cloud-native formats and their use cases:

| Format | Use Case | Python Libraries |
|--|--|--|
| [Apache Parquet](https://parquet.apache.org/) | Column-oriented data file format designed for efficient data storage and retrieval. Suitable for tabular-style data (rows and columns). | pandas, dask.dataframe, vaex, pyarrow |
| [Zarr](http://zarr.dev/) | Storage of large multidimensional arrays | zarr, numpy, dask.array, xarray |
| [Cloud Optimized Geotiff](https://www.cogeo.org/) | Geospatial raster data | rasterio, rio-xarray |

There are other more specialized cloud-optimized formats for specific scientific domains.

It is recommended to use cloud-native formats when working with big data in cloud object storage.

### Working with Object Storage

From a user perspective, the main challenge of working with object storage is the need
to use more specialized tools, rather than just simple files / filenames, to manage data.
Fortunately, excellent tools exist to make working with object storage easy and familiar.

For python users, the main tool is [filesystem spec](https://filesystem-spec.readthedocs.io/en/latest/)
(fsspec), a set of packages which enable us to work with many different types of storage.
Separate fsspec packages exist for each type of object storage:

- **[s3fs](https://s3fs.readthedocs.io/en/latest/)** - for working with AWS S3
  (Simple Storage Service) and compatible APIs. Most third-party object storage
  services (e.g. [Wasabi](https://wasabi.com/) and [Open Storage Newtork](https://openstoragenetwork.org/))
  are compatible with S3.
- **[gcsfs](https://gcsfs.readthedocs.io/en/latest/)** - for working with Google
  Cloud Storage.
- **[adlfs](https://github.com/fsspec/adlfs)** - for working with Azure Data Lake
  and Azure BLOB Storage.

Each system has its own unique mechanisms for authentication and authorization;
consult the documentation links above for more details.

#### Reading Data

When reading data from cloud object storage, you have two general options:
- Download the data to the local filesystem; this is fine for small data, but not suitable for
  large data or cloud-optimized datasets. Downloads can be managed with
  [Pooch](https://www.fatiando.org/pooch/latest/) or fsspec.
- Open the data with an application that understands how to stream data data
  over HTTP directly from object storage. This is suitable for large data and
  cloud-native formats.

As an example of the latter use case, here is how you would open the
[NASA  Multi-Scale Ultra High Resolution (MUR) Sea Surface Temperature (SST)](https://registry.opendata.aws/mur/)
dataset from the AWS Public Data program using Xarray:

```python
import xarray as xr
ds = xr.open_dataset("s3://mur-sst/zarr/", engine="zarr", storage_options={"anon": True})
```

#### Writing Data

Writing data (and reading private data) requires credentials for authentication.
2i2c does not provide credentials to individual users.
Instead, 2i2c customers should manage their own cloud storage directly.
See [the Amazon S3](https://aws.amazon.com/s3/getting-started/), [Google Cloud Storage](https://cloud.google.com/storage), and [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) instructions for information on getting started.

:::{note}
This section refers to "S3 Storage" in a generic sense.
Amazon S3 is the most well-known form of S3 storage, but something like it exists across each major cloud provider as well.
:::


On S3-type storage, you will have a client key and client secret associated with you account.
The following code creates a writeable filesystem:

```python
import s3fs
fs = s3fs.S3FileSystem(key='<YOUR_CLIENT_KEY>', secret='<YOUR_CLIENT_SECRET')
```

Non-AWS S3 services (e.g. Wasabi Cloud) can be configured by passing an argument
such as `client_kwargs={'endpoint_url': 'https://s3.us-east-2.wasabisys.com'}`
to `S3FileSystem`.

For Google Cloud Storage, the best practice is to create a
[service account](https://cloud.google.com/iam/docs/service-accounts) with
appropriate permissions to read / write to your private bucket.
You upload your service account key (a `.json` file) to your hub
home directory and then use it as follows:

```python
 import json
 import gcsfs
 with open('<your_token_file>.json') as token_file:
     token = json.load(token_file)
 gcs = gcsfs.GCSFileSystem(token=token)
```

You can then read / write private files with the ``gcs`` object.

### Scratch Bucket

Some 2i2c environments are configured with a "scratch bucket," which
allows you to temporarily store data (for example, when you need to store intermediate files during data transformations).
Credentials to write to the scratch
bucket are pre-loaded into your Hub's user environment.

:::{warning}
Any data in scratch buckets will be deleted once it is 7 days old.
Do not use scratch buckets to store data permanently.
:::

The location of your scratch bucket is contained in the environment variable ``SCRATCH_BUCKET ``.

For example, here is how you would write Xarray data to the scratch bucket
in Zarr format.


```python
import os
import xarray as xr
SCRATCH_BUCKET = os.environ['SCRATCH_BUCKET'] 
ds = xr.tutorial.open_dataset("rasm")  # load example data
ds.to_zarr(f'{SCRATCH_BUCKET}/rasm.zarr')  # write data
```

:::{warning}
A common set of credentials is currently used for accessing scratch buckets.
This means users can read, and potentially remove / overwrite, each others'
data. You can avoid this problem by always using ``SCRATCH_BUCKET`` as a prefix.
Still, you should not store any sensitive or mission-critical data in
the scratch bucket.
:::

### Data Catalogs

To make it easier to discover share data in your project, it is recommended to use
data catalogs.
[Intake](https://intake.readthedocs.io/en/latest/) is a popular tool for making
data catalogs in python.

Below is an example of an intake data catalog for loading Zarr data in Xarray from
OpenStorageNetwork.
(This example is borrowed from the [Ocean Eddy CPT project](https://github.com/ocean-eddy-cpt/cpt-data/blob/master/catalog.yaml).)

```yaml
plugins:
  source:
    - module: intake_xarray

sources:

  neverworld_five_day_averages:
    description: Five-day-average fields from Neverworld2
    driver: zarr
    args:
      urlpath: s3://Pangeo/ocean-eddy-cpt/5-day-averages/
      consolidated: True
      storage_options:
        anon: True
        client_kwargs:
          endpoint_url: 'https://ncsa.osn.xsede.org'

  neverworld_quarter_degree_snapshots:
    description: snapshots of fields from Neverworld2
    driver: zarr
    args:
      urlpath: s3://Pangeo/ocean-eddy-cpt/quarter-degree/snapshots/
      consolidated: True
      storage_options:
        anon: True
        client_kwargs:
          endpoint_url: 'https://ncsa.osn.xsede.org'
```

To use this catalog, place it online and share the URL with your team.

Here is an example of how to use this catalog file:

```python
import intake
cat_url = "https://raw.githubusercontent.com/ocean-eddy-cpt/cpt-data/master/catalog.yaml"
cat = intake.open_catalog(cat_url)
list(cat)  # discover what is in the catalog
ds = cat['neverworld_five_day_averages'].to_dask()  # open lazily with Xarray
```
