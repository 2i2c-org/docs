# Manage files on AWS S3 cloud object storage

This instructional guide shows you how to upload files to AWS S3 cloud object storage for your hub. In this example, we cover the difference between scratch versus persistent buckets and some basic AWS CLI commands for managing S3 objects within cloud object storage for your hub.

```{contents}
:depth: 2
:local:
```

## Scratch versus persistent buckets on a 2i2c hub

Bucket
: A *bucket* is a container for objects.

Object
: An *object* is a file and any metadata that describes that file.

### Scratch buckets

[Scratch buckets](https://infrastructure.2i2c.org/topic/features/#scratch-buckets-on-object-storage) are designed for storage of *temporary* files, e.g. intermediate results. Objects stored in a scratch bucket are purged after 7 days.

Check the name of your scratch bucket by opening a Terminal in your hub and running the command

```bash
$ echo $SCRATCH_BUCKET
s3://2i2c-aws-us-scratch-showcase/<username>
```

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

It is possible to configure read-only access for objects stored in cloud storage on your hub. Please consult [2i2c support](https://docs.2i2c.org/support/) to enable this feature.

## Basic AWS CLI commands in the Terminal

In the Terminal, check that the AWS CLI commands are available in your image with

```bash
$ which aws
/srv/conda/envs/notebook/bin/aws
```

If this returns nothing, then you can temporarily install the package with

```bash
curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o $HOME/.local/awscliv2.zip
unzip $HOME/.local/awscliv2.zip
export PATH=$HOME/.local/aws/dist:$PATH
```

:::{tip}
The following examples are for managing objects in a scratch bucket using the `$SCRATCH_BUCKET` environment variable. For persistent buckets, this can be replaced with the `$PERSISTENT_BUCKET` environment variable.
:::

(object-storage:list-prefixes)=
### List prefixes within an S3 bucket

Prefix
: There is no concept of "folders" in flat cloud object storage and every object is instead indexed with a key-value pair. Prefixes are a string of characters at the beginning of the object key name used to organize objects in a similar way to folders. 

Storage buckets on a 2i2c hub are organized into prefixes named after a hub user's username. To list the prefixes of users that have stored files in cloud object storage, use the command 

```bash
$ aws s3 ls $SCRATCH_BUCKET
                           PRE <username1>/
                           PRE <username2>/

```

where the label `PRE` indicates the item listed is a prefix and not an object.

:::{tip}
[AWS Docs – Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) for more information.
:::

### List the contents of your prefix

List the contents of files stored under your own prefix with the command

```bash
aws s3 ls $SCRATCH_BUCKET/
```

:::{note}
Note the trailing slash `/` after `$SCRATCH_BUCKET` compared to the command specified in {ref}`List prefixes within an S3 bucket<object-storage:list-prefixes>`.
:::

### Upload and download files to and from a bucket

Upload a file to your prefix in the scratch bucket with the command

```bash
$ aws s3 cp <filepath> $SCRATCH_BUCKET/
upload: ./<filepath> to s3://2i2c-aws-us-scratch-showcase/<username>/<filepath>
```

and download a file from your prefix in the scratch bucket with the command

```bash
$ aws s3 cp $SCRATCH_BUCKET/<source_filepath> <target_filepath>
download: s3://2i2c-aws-us-scratch-showcase/<username>/<source_filepath> to ./<target_filepath>
```

### Delete a file from a bucket

Delete a file from your prefix in a bucket with the command

```bash
$ aws s3 rm $SCRATCH_BUCKET/<filepath>
delete: s3://2i2c-aws-us-scratch-researchdelight/<username>/<filepath>
```

:::{tip}
Consult the [AWS Docs – Use high-level (s3) commands with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-managing-buckets-references) for a more detailed guide of AWS commands for managing S3 objects.
:::

