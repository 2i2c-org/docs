(object-storage-aws)=
# How-to manage S3 cloud object storage with AWS CLI

This instructional guide shows you how to upload files from your hub to AWS S3 cloud object storage. In this example, we cover some basic AWS CLI commands for managing S3 objects within cloud object storage for your hub.

```{admonition} Who is this guide for?
:class: note

Some community hubs running on AWS infrastructure have scratch and/or persistent S3 storage buckets already configured. This documentation is intended for users with a hub that has this feature enabled.

```

```{contents}
:depth: 2
:local:
```

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

## FAQs

- *How do I know if our hub is running on AWS or not?*

  Check out our [list of running hubs](https://infrastructure.2i2c.org/reference/hubs/) to see which cloud provider your hub is running on.

- *How do I determine if a scratch and/or persistent bucket is already available?*

  Check whether the environment variables for each bucket are set. See {ref}`Scratch buckets<object-storage:env-var-scratch>` and {ref}`Persistent buckets<object-storage:env-var-persistent>`

- *If S3 buckets are supposed to be available but the environment variables for AWS credentials are not defined, what should I do?*

  If environment variables for the relevant AWS credentials for your hub are not defined, then you may encounter the following error

  ```bash
  An error occurred (AccessDenied) when calling the AssumeRoleWithWebIdentity operation: Not authorized to perform sts:AssumeRoleWithWebIdentity.
  ```

  Please contact your hub champion so that they can open a {doc}`2i2c support<../../../../support>` ticket with us to resolve this issue on your behalf.

- *If S3 buckets are not set up but I want them for my community what should the I do?*

  This feature is not enabled by default since there are extra cloud costs associated with providing S3 object storage. Please speak to your hub champion, who can then open a {doc}`2i2c support<../../../../support>` ticket with us to request this feature for your hub.

- *Is our S3 bucket accessible outside of the hub so I can upload files from elsewhere?*

  Yes, this requires configuring AWS credentials from your machine, however we currently do no have documentation for this.  Please contact {doc}`2i2c support<../../../../support>` for guidance.

- *Is our S3 bucket accessible outside of the hub so users can download files to elsewhere?*

  The same answer to the question above applies in this instance.

- *Will 2i2c create additional, new S3 buckets for our community?*

  Please contact contact your hub champion to liaise with {doc}`2i2c support<../../../../support>` to discuss this option.

- *If a our hub is running on GCP or Azure and we have object storage, what are our options?*

  Check out our resources listed in the {doc}`Cloud Object Storage<index>` user topic guide.
