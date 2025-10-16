# Download your data from the hub

You might want to download your entire home directory for many
reasons - to get data off a hub that is closing, to migrate to
a different service, for archival purposes, etc. Your home directory
will contain all your data *and* your notebooks.
Hubs managed by 2i2c make this easy.

## Download from the hub interface

1. **Open the classic Jupyter Notebook file browser.** If you are
   using another interface, navigate to the classic interface by changing your
   URL path to `/tree`. e.g.,
   `<your-hub>.pilot.2i2c.cloud/user/<your-username>/tree`

2. Click on **`Download Directory`**.

   ```{figure} ../../images/download-directory.png
   :alt: The download directory button
   ```

This will zip up the contents of your user file system and download them to your machine.

:::{note}
If your hub is using a [custom user environment](../../admin/environment/customize), it needs the
[jupyter-tree-download](https://github.com/ryanlovett/jupyter-tree-download) package
installed to make this feature available. As it is a Jupyter Notebook extension, you
*must* install this in your image - manually installing with `!pip` inside your notebook
will *not* work.
:::

## Download the archive of your home directory from an S3 bucket

If you have requested that 2i2c archive all the home directories of the hub users and store them to an S3 bucket, you can follow the instructions below to download them.

1. Make sure the user has an AWS account created for them and they can successfully authenticate from the command line.
   See the [AWS guide](https://docs.aws.amazon.com/cli/v1/userguide/cli-authentication-short-term.html) for more details.

2. Assign the `AssumeHomedirsArchiveAccess` policy to their AWS IAM user, which allows them to access the S3 bucket where the home directories are archived.
   Replace `<username>` with the user's name and `<account-number>` with the AWS account number.

    ```bash
    aws iam attach-user-policy \
      --user-name "<username>" \
      --policy-arn "arn:aws:iam::<account-number>:policy/AssumeHomedirsArchiveAccess"
    ```
3. Run an `aws s3 ls` to make sure you can see the S3 bucket where the home directories are archived.
    ```bash
    aws s3 ls s3://<cluster-name>-<hub-name>-homedirs-archive/<username>/
    ```

4. Download the archive of your home directory from the S3 bucket.
   ```bash
   aws s3 cp s3://<cluster-name>-<hub-name>-homedirs-archive/<username>/archive-<some-date>.tar.gz /path/to/download/
   ```
