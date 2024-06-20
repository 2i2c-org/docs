# Cloud Object Storage

This section gives an overview of storing data in the cloud, as well as how-to guides for using specific tools to manage your cloud data:

```{toctree}
:maxdepth: 1
working-with-object-storage
manage-object-storage-aws
```

## Overview

Your hub lives in the cloud, therefore the preferred way to store data is using [object storage](https://aws.amazon.com/what-is-cloud-object-storage/), such as Amazon S3 or Google Cloud Storage. Cloud object storage is essentially a key/value storage system.
The keys are strings and the values are bytes of data. Data is read and written using HTTP calls.

The performance of object storage is very different from file storage.
On one hand each individual `read / write` to object storage has a high overhead (10-100 milliseconds) since it has to go over the network, while on the other hand object storage “scales out” nearly infinitely, meaning that we can make hundreds, thousands, or millions of concurrent read / write requests. *This makes object storage well suited for distributed data analytics*. However, data analysis software must be adapted to take advantage of these properties.

## Scratch versus persistent buckets on a 2i2c hub

Bucket
: A *bucket* is a container for objects.

Object
: An *object* is a file and any metadata that describes that file.

(object-storage:env-var-scratch)=
### Scratch buckets

[Scratch buckets](https://infrastructure.2i2c.org/topic/features/#scratch-buckets-on-object-storage) are designed for storage of *temporary* files, e.g. intermediate results.

:::{tip}
Any data in a scratch bucket is deleted after 7 days.

**Do not use scratch buckets to permanently store critical data.**
:::

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

:::{tip}
It is the responsibility of the hub admin and hub users to delete objects in `$PERSISTENT_BUCKET` when no longer needed to minimize cloud billing costs. 2i2c takes no responsibility for managing storage costs and objects stored in `$PERSISTENT_BUCKET`.
:::

## File permissions

A common set of credentials is used for accessing storage buckets. 

```{tip}
Hub users can access each others' objects stored in scratch or persistent bucket storage and accidentally modify or delete them.
```

It is possible to configure read-only access for objects stored in cloud storage on your hub, though this is not a standard feature of our hubs. Please consult {doc}`2i2c support<../../../../support>` to discuss enabling this feature.


