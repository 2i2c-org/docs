(object-storage-gcp)=
# How-to manage GCP cloud object storage with Google Cloud SDK

This instructional guide shows you how to manage files in Google Cloud storage using Google Cloud SDK. The SDK is a set of libraries and tools that can interact with GCP. In this example, we cover some basic commands for managing objects within cloud object storage for your hub.

```{admonition} Who is this guide for?
:class: note

Some community hubs running on GCP infrastructure have scratch and/or persistent S3 storage buckets already configured. This documentation is intended for users with a hub that has this feature enabled.

```

```{contents}
:depth: 2
:local:
```

## Basic Google Cloud SDK commands in the Terminal

In the Terminal, check that the Google Cloud SDK commands are available in your software environment with

```bash
$ which gcloud
/opt/conda/bin/gcloud
```

If this returns nothing, then you can temporarily install the package with

```bash
mamba install google-cloud-sdk
```

```{tip}
If installing the package kills your server, then try using a server with a more RAM.
```

```{note}
The following examples are for managing objects in a scratch bucket using the `$SCRATCH_BUCKET` environment variable. For persistent buckets, this can be replaced with the `$PERSISTENT_BUCKET` environment variable.
```

### List prefixes within a GCP bucket

Prefix
: There is no concept of "folders" in flat cloud object storage and every object is instead indexed with a key-value pair. Prefixes are a string of characters at the beginning of the object key name used to organize objects in a similar way to folders.

Storage buckets on a 2i2c hub are organized into prefixes named after a hub user's username. Check the name of your bucket by running the command

```bash
$ echo $SCRATCH_BUCKET
gs://<bucket_name>/<username>
```

*Recursively* list all the files in your bucket by running the command

```bash
gcloud storage ls --recursive $SCRATCH_BUCKET
```

Remember that cloud storage is flat and therefore [Access permissions](index.md#access-permissions) means that anyone can access each other's files. You can therefore list the prefixes of the entire bucket with

```bash
$ gcloud storage ls gs://<bucket_name>
gs://<bucket_name>/<username1>/
gs://<bucket_name>/<username2>/
```

```{tip}
See [Google Cloud Docs – List objects](https://cloud.google.com/storage/docs/listing-objects) for more information.
```

### Copy files on the hub to and from a bucket

Move a file on the hub to your prefix in the scratch bucket with the command

```bash
$ gcloud storage cp <filepath> $SCRATCH_BUCKET/<filepath>
Copying file://<filepath> to gs://<bucket_name>/<username>/<filepath>
  Completed files 1/1 | 14.0B/14.0B
```

and copy a file from your prefix in the scratch bucket with the command

```bash
$ gcloud storage cp $SCRATCH_BUCKET/<source_filepath> <target_filepath>
Copying gs://<bucket_name>/<username>/<source_filepath> to file://<target_filepath>
  Completed files 1/1 | 14.0B/14.0B
```

```{tip}
See [Google Cloud Docs – Copy, rename, and move objects](https://cloud.google.com/storage/docs/copying-renaming-moving-objects) for more information.
```

### Delete a file from a bucket

Delete a file from your prefix in a bucket with the command

```bash
$ gcloud storage rm $SCRATCH_BUCKET/<filepath>
Removing objects:
Removing gs://<bucket_name>/<username>/<filepath> 
  Completed 1/1                
```

```{tip}
See [Google Cloud Docs – Delete objects](https://cloud.google.com/storage/docs/deleting-objects) for more information.
```

## Upload files to a GCP bucket from outside the hub

We outline workflows for two scenarios:

- [Small datasets from your local machine](#small-datasets-from-your-local-machine) is suitable for data transfer from your PC or laptop
- [Large datasets from a remote server](#large-datasets-from-a-remote-server) is suitable for data transfer from places like a supercomputer

```{tip}
The following workflows assume you are operating a Unix-like operating system from outside the hub.
```

### Small datasets from your local machine

For small datasets that can be uploaded from your local machine, e.g. laptop or PC, you can generate a temporary access token on the hub to upload data to the GCP bucket.

1. Set up a new software environment on your *local* machine

   ```bash
   mamba env create --name gcp_transfer google-cloud-sdk
   ```

1. Activate the environment

   ```bash
   mamba activate gcp_transfer
   ```

1. Generate a temporary access token from your *2i2c hub*

   ```bash
   gcloud auth print-access-token
   ```

   ```{tip}
   This access token is valid for 60 minutes by default. This can be extended by up to 12 hours, but we recommend setting this to the minimum time needed to transfer your data for security reasons. Please see [Google Cloud Docs – gcloud auth application-default print-access-token](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) for further information.
   ```

1. Copy and paste the output of the above command to your *local* machine and save this to a `token.txt` file

1. Authorize the Google Cloud CLI

   ```bash
   gcloud config set auth/access_token_file token.txt
   ```

1. Define the `$SCRATCH_BUCKET` environment variable on your *local* machine

   ```bash
   SCRATCH_BUCKET=gs://<bucket_name>/<username> 
   ```

1. Compress the data.

   ```bash
   tar -czvf name-of-archive.tar.gz /path/to/directory-or-file
   ```

1. Upload the data to the storage bucket

   ```bash
   $ gcloud storage cp name-of-archive.tar.gz $SCRATCH_BUCKET
   Copying file://name-of-archive.tar.gz to gs://<bucket_name>/<username>/name-of-archive.tar.gz
     Completed files 1/1 | 23.3MiB/23.3MiB                                                     

     Average throughput: 8.9MiB/s
   ```

1. Check the contents of your prefix

   ```bash
   $ gcloud storage ls $SCRATCH_BUCKET/
   gs://<bucket_name>/<username>/name-of-archive.tar.gz
   ```

   ```{tip}
   Note the trailing slash `/` after `$SCRATCH_BUCKET`.
   ```

### Large datasets from a remote server

## FAQs

- *How do I know if our hub is running on GCP or not?*

  Check out our [list of running hubs](https://infrastructure.2i2c.org/reference/hubs/) to see which cloud provider your hub is running on.

- *How do I determine if a scratch and/or persistent bucket is already available?*

  Check whether the environment variables for each bucket are set. See {ref}`Scratch buckets<object-storage:env-var-scratch>` and {ref}`Persistent buckets<object-storage:env-var-persistent>`

- *If storage buckets are not set up but I want them for my community what should the I do?*

  This feature is not enabled by default since there are extra cloud costs associated with providing object storage. Please speak to your hub champion, who can then open a {doc}`2i2c support<../../../../support>` ticket with us to request this feature for your hub.

- *Will 2i2c create additional, new storage buckets for our community?*

  Please contact contact your hub champion to liaise with {doc}`2i2c support<../../../../support>` to discuss this option.

- *If a our hub is running on AWS or Azure and we have object storage, what are our options?*

  Check out our resources listed in the {doc}`Cloud Object Storage<index>` user topic guide.

## Acknowledgements

Thank you to the [LEAP-Pangeo community](https://leap-stc.github.io/intro.html) for authoring the original content that inspired this section.
