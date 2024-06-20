# Cloud Object Storage

This section gives an overview of storing data in the cloud, as well as how-to guides for using specific tools to manage your cloud data.

```{toctree}
:maxdepth: 1
manage-object-storage-aws
```

## Overview

Your hub lives in the cloud.
The preferred way to store data in the cloud is using [cloud object storage](https://aws.amazon.com/what-is-cloud-object-storage/), such as Amazon S3 or Google Cloud Storage.
Cloud object storage is essentially a key/value storage system.
They keys are strings, and the values are bytes of data.
Data is read and written using HTTP calls.

The performance of object storage is very different from file storage.
On one hand, each individual `read / write` to object storage has a high overhead (10-100 ms), since it has to go over the network.
On the other hand, object storage “scales out” nearly infinitely, meaning that we can make hundreds, thousands, or millions of concurrent reads / writes.
This makes object storage well suited for distributed data analytics.
However, data analysis software must be adapted to take advantage of these properties.

## Scratch versus persistent buckets on a 2i2c hub

Bucket
: A *bucket* is a container for objects.

Object
: An *object* is a file and any metadata that describes that file.

(object-storage:env-var-scratch)=
### Scratch buckets

[Scratch buckets](https://infrastructure.2i2c.org/topic/features/#scratch-buckets-on-object-storage) are designed for storage of *temporary* files, e.g. intermediate results. Objects stored in a scratch bucket are purged after 7 days.

Check the name of your scratch bucket by opening a Terminal in your hub and running the command

```bash
$ echo $SCRATCH_BUCKET
s3://2i2c-aws-us-scratch-showcase/<username>
```

(object-storage:env-var-persistent)=
### Persistent buckets

[Persistent buckets](https://infrastructure.2i2c.org/topic/features/#persistent-buckets-on-object-storage) are designed for storing data that is consistently used throughout the lifetime of a project and the data is not purged after a set number of days.

Check the name of your persistent bucket by opening a Terminal in your hub and running the command

```bash
$ echo $PERSISTENT_BUCKET
s3://2i2c-aws-us-persistent-showcase/<username>
```

## Storage costs

See [2i2c Infrastructure Guide – What exactly do cloud providers charge us for?](https://infrastructure.2i2c.org/topic/billing/chargeable-resources/#object-storage) for a detailed overview of cloud object storage costs. 

:::{warning}
It is the responsibility of the hub admin and hub users to delete objects in `$PERSISTENT_BUCKET` when no longer needed to minimize cloud billing costs. 2i2c takes no responsibility for managing storage costs and objects stored in `$PERSISTENT_BUCKET`.
:::

## File permissions

By default there are no permission controls to prevent hub users from accessing each others' objects stored in scratch or persistent bucket storage.

It is possible to configure read-only access for objects stored in cloud storage on your hub. Please consult {doc}`2i2c support<../../../support>` to enable this feature.

## Cloud-Native Formats

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

## Working with Object Storage

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

### Reading Data

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

### Writing Data

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

## Scratch Bucket

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

## Data Catalogs

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
