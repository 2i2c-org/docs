(object-storage-aws)=
# How-to manage S3 cloud object storage with AWS CLI

This instructional guide shows you how to upload files from your hub to AWS S3 cloud object storage. In this example, we cover some basic AWS CLI commands for managing S3 objects within cloud object storage for your hub.

```{admonition} Who is this guide for?
:class: note

Some community hubs running on AWS infrastructure have scratch and/or persistent S3 storage buckets already configured. This documentation is intended for users with a hub that has this feature enabled.
```

```{warning}
Transferring large amounts of data to the cloud can incur expensive storage costs. Please think carefully about your data requirements and use this feature responsibly. See [](/topic/cloud-costs.md) for further guidance.
```

```{contents}
:depth: 2
:local:
```

## Basic AWS CLI commands in the Terminal

In the Terminal, check that the AWS CLI commands are available in your image with

```{margin}
We recommend using the Pangeo notebook image, which has the AWS CLI package already installed. 
```

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

:::{note}
The following examples are for managing objects in a scratch bucket using the `$SCRATCH_BUCKET` environment variable. For persistent buckets, this can be replaced with the `$PERSISTENT_BUCKET` environment variable. See [Scratch versus Persistent Buckets](index.md/#scratch-versus-persistent-buckets-on-a-2i2c-hub).
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

### Copy files on the hub to and from a bucket

Copy a file on the hub to your prefix in the scratch bucket with the command

```bash
$ aws s3 cp <filepath> $SCRATCH_BUCKET/
upload: ./<filepath> to s3://2i2c-aws-us-scratch-showcase/<username>/<filepath>
```

and copy a file from your prefix in the scratch bucket with the command

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

```{tip}
Consult the [AWS Docs – Use high-level (s3) commands with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-managing-buckets-references) for a more detailed guide of AWS commands for managing S3 objects.
```

```{note}
As mentioned in [Access permissions](index.md#access-permissions), anyone can access each other's files in object storage on the hub. Be careful about which objects you are deleting.
```

## Upload files to an S3 bucket from outside the hub

We outline a workflow for how to transfer datasets to the AWS bucket from outside the hub, such as your local machine or a remote server. This is done by generating a temporary access token that is valid for up to 1 hour.

```{tip}
The following workflow assumes you have a Unix-like operating system from outside the hub.
```

1. Set up a new software environment on your *local machine*

   ```bash
   mamba create --name aws_transfer aws-cli
   ```

1. Activate the environment

   ```bash
   mamba activate aws_transfer

1. Generate a temporary access token from your *2i2c hub*

   ```{margin}
   We recommend using the Pangeo notebook image, which has the AWS CLI package already installed. 
   ```

   ```bash
   aws sts assume-role-with-web-identity --role-arn $AWS_ROLE_ARN --role-session-name $JUPYTERHUB_CLIENT_ID --web-identity-token "$(cat $AWS_WEB_IDENTITY_TOKEN_FILE)" --duration-seconds 1000 
   ```

   ```{tip}
   This access token is valid for 1000 seconds by setting the `--duration-seconds` flag. The maximum value is 3600 seconds (1 hour), but we recommend setting this to the minimum time needed to transfer your data for security reasons. Please see [AWS Docs – aws sts assume-role-with-web-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role-with-web-identity.html) for further information.
   ```

1. Note the key-values returned for `AccessKeyId`, `SecretAccessKey` and `SessionToken`

1. Configure the `~/.aws/credentials` file on your *local machine* with a new profile using the following commands

   ```bash
   aws configure set aws_access_key_id <AccessKeyId> --profile <profile_name>
   aws configure set aws_secret_access_key <SecretAccessKey> --profile <profile_name>
   aws configure set aws_session_token <SessionToken> --profile <profile_name>
   ```

   ```{tip}
   See the [AWS Docs – aws configure set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/set.html) for more information.
   ```

1. Set the `region` in your `~/.aws/config` file on your *local machine* using the following command

   ```bash
   aws configure set region <data_center_location>
   ```

   ```{tip}
   See the [FAQs](#faqs) below for how to find the data center location of your hub.
   ```

1. Define the `AWS_PROFILE` environment variable on your *local machine*

   ```bash
   AWS_PROFILE=<profile_name>
   ```

1. Define the `$SCRATCH_BUCKET` environment variable 

   ```bash
   SCRATCH_BUCKET=s3://<bucket_name>/<username> 
   ```

1. Compress the data to prepare for transfer

   ```bash
   tar -czvf name-of-archive.tar.gz /path/to/directory-or-file
   ```

1. Upload the data to the storage bucket

   ```bash
   $ aws s3 cp name-of-archive.tar.gz $SCRATCH_BUCKET
   upload: ./name-of-archive.tar.gz to s3://<bucket_name>/<username>/name-of-archive.tar.gz
   ```

1. Check the contents of your prefix

   ```bash
   $ aws s3 ls $SCRATCH_BUCKET/
   2024-07-04 17:01:54          4 name-of-archive.tar.gz
   ```

   ```{tip}
   Note the trailing slash `/` after `$SCRATCH_BUCKET`.
   ```

## FAQs

- *How do I know if our hub is running on AWS or not?*

  Check out our [list of running hubs](https://infrastructure.2i2c.org/reference/hubs/) under the column *provider* to see which cloud provider your hub is running on.

- *Where is the location of the data center our hub is running on?*

  Check out our [list of running hubs](https://infrastructure.2i2c.org/reference/hubs/) under the column *data center location*.

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

- *Will 2i2c create additional, new S3 buckets for our community?*

  Please contact contact your hub champion to liaise with {doc}`2i2c support<../../../../support>` to discuss this option.

- *If a our hub is running on GCP or Azure and we have object storage, what are our options?*

  Check out our resources listed in the {doc}`Cloud Object Storage<index>` user topic guide.
