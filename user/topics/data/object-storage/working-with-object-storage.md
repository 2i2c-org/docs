# How-to work with object storage in Python

```{warning}
Transferring large amounts of data to the cloud can incur expensive storage costs. Please think carefully about your data requirements and use this feature responsibly. See [](/topic/cloud-costs.md) for further guidance.
```

## Cloud-Native Formats

Cloud-native file formats are designed to work well with cloud object storage. These formats permit exploration of data and metadata without downloading the entire file / dataset and work well with distributed parallel computing. Here are some popular cloud-native formats and their use cases:

| Format | Use Case | Python Libraries |
|--|--|--|
| [Apache Parquet](https://parquet.apache.org/) | Column-oriented data file format designed for efficient data storage and retrieval. Suitable for tabular-style data (rows and columns). | pandas, dask.dataframe, vaex, pyarrow |
| [Zarr](http://zarr.dev/) | Storage of large multidimensional arrays | zarr, numpy, dask.array, xarray |
| [Cloud Optimized Geotiff](https://www.cogeo.org/) | Geospatial raster data | rasterio, rio-xarray |

There are other more specialized cloud-optimized formats for specific scientific domains.

It is recommended to use cloud-native formats when working with big data in cloud object storage.

## Tools

From a user perspective, the main challenge of working with object storage is the need
to use more specialized tools, rather than just simple files / filenames, to manage data.
Fortunately, excellent tools exist to make working with object storage easy and familiar.

For python users, the main tool is [filesystem spec](https://filesystem-spec.readthedocs.io/en/latest/)
(`fsspec`), a set of packages which enable us to work with many different types of storage.
Separate `fsspec` packages exist for each type of object storage:

::::{tab-set}
:::{tab-item} AWS
:sync: AWS
**[s3fs](https://s3fs.readthedocs.io/en/latest/)** - for working with AWS S3 (Simple Storage Service) and compatible APIs. Most third-party object storage services (e.g. [Wasabi](https://wasabi.com/) and [Open Storage Newtork](https://openstoragenetwork.org/)) are compatible with S3.
:::
:::{tab-item} GCP
:sync: GCP
**[gcsfs](https://gcsfs.readthedocs.io/en/latest/)** - for working with Google Cloud Storage.
:::
:::{tab-item} Azure
:sync: Azure
**[adlfs](https://github.com/fsspec/adlfs)** - for working with Azure Data Lake and Azure BLOB Storage.
:::
::::

Each system has its own unique mechanisms for authentication and authorization; see the links below for more details:

::::{tab-set}
:::{tab-item} AWS
:sync: AWS
[](manage-object-storage-aws.md)
:::
:::{tab-item} GCP
:sync: GCP
[](manage-object-storage-gcp.md)
:::
::::

### Reading Data

When reading data from cloud object storage, you have two general options:
- Download the data to the local filesystem; this is fine for small data, but not suitable for
  large data or cloud-optimized datasets. Downloads can be managed with
  [Pooch](https://www.fatiando.org/pooch/latest/) or `fsspec`.
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

Writing data (and reading private data) requires credentials for authentication from outside the hub. 2i2c does not provide credentials to individual users. For information on getting started, see

::::{tab-set}
:::{tab-item} AWS
:sync: AWS
[AWS Docs – Getting Started](https://aws.amazon.com/s3/getting-started/)
:::
:::{tab-item} GCP
:sync: GCP
[Google Cloud Docs – Storage](https://cloud.google.com/storage)
:::
:::{tab-item} Azure
:sync: Azure
[Azure Docs – Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/)
:::
::::

The following code snippets show how to write data to a storage bucket with Python

::::{tab-set}
:::{tab-item} AWS
:sync: AWS
Generate a temporary access token following the instructions in [Upload files to an S3 bucket from outside the hub](manage-object-storage-aws.md/#upload-files-to-an-s3-bucket-from-outside-the-hub) and make a note of the profile name.

```python
import s3fs
fs = s3fs.S3FileSystem(profile=<profile_name>)
```
You can then manage files with the `fs` object.
:::
:::{tab-item} Non-AWS S3
Non-AWS S3 services (e.g. Wasabi Cloud) can be configured by passing an argument
such as `client_kwargs={'endpoint_url': 'https://s3.us-east-2.wasabisys.com'}`
to `S3FileSystem`.
:::
:::{tab-item} GCP
:sync: GCP
Generate Application Default Credentials (ADC) following the instructions in [Upload files to a GCP bucket from outside the hub](manage-object-storage-gcp.md/#large-datasets-from-a-remote-server) and make a note of where the `application_default_credentials.json` file is located.

```python
import json
import gcsfs
with open('<path>/application_default_credentials.json') as token_file:
 token = json.load(token_file)
fs = gcsfs.GCSFileSystem(token=token)
```
You can then manage files with the `fs` object.
:::
::::

#### Example – Writing to a Scratch Bucket

Here is how you would write Xarray data to the scratch bucket in Zarr format.

```python
import os
import xarray as xr
SCRATCH_BUCKET = os.environ['SCRATCH_BUCKET'] 
ds = xr.tutorial.open_dataset("rasm")  # load example data
ds.to_zarr(f'{SCRATCH_BUCKET}/rasm.zarr')  # write data
```

:::{tip}
For more example workflows, checkout the [NASA Earthdata Cloud Cookbook](https://nasa-openscapes.github.io/earthdata-cloud-cookbook/how-tos/using-s3-storage.html).
:::

## Data Catalogs

To make it easier to discover share data in your project, it is recommended to use
data catalogs. [Intake](https://intake.readthedocs.io/en/latest/) is a popular tool for making
data catalogs in python.

Below is an example of an intake data catalog for loading Zarr data in Xarray from
OpenStorageNetwork. (This example is borrowed from the [Ocean Eddy CPT project](https://github.com/ocean-eddy-cpt/cpt-data/blob/master/catalog.yaml).)

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
