# Prometheus API access

## Overview

It is possible to directly query the Prometheus API from the outside world at `https://prometheus.<cluster_name>.2i2c.cloud`.

Use cases include configuring Prometheus as a datasource for your own monitoring systems, such as [AWS CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_MultiDataSources-Connect.html#MultiDataSources-Prometheus) or another Grafana instance.

## Steps

Sharing credentials to access your Prometheus instance from the outside world needs to be done securely. This is because Personally Identifiable Information (PII) is at risk if the credentials are compromised.

```{tip}
Please do not share these credentials through any insecure channels, and notify us immediately if you need to renew them.
```

We use `age` to encrypt and decrypt information securely.

1. Install [age](https://age-encryption.org).

1. In a terminal, run the command `age-keygen -o key.txt`.

1. This should create a `key.txt` file containing your private key, and return an output of the form

   ```bash
   Public key: <public_key>
   ```

   Make a note of this public key for the next step.

   ```{tip}
   Never share your private key with anyone. This is used to decrypt data encrypted with the public key. You can share the public key.
   ```

1. Send a [support request](/support.md) to 2i2c
   - Ask for credentials to be provisioned for access to `https://prometheus.<cluster_name>.2i2c.cloud`
   - Share the public key with 2i2c

1. 2i2c will respond with a message with a file attachment called `credentials.txt.age`. Use `age` to decrypt it by running the following command in your terminal from the same directory that contained the `key.txt` file generated in Step 1.

   ```bash
   age --decrypt -i key.txt -o credentials.txt credentials.txt.age
   ```

   The credentials are contained in the decrypted `credentials.txt` file.

1. You can now access `https://prometheus.<cluster_name>.2i2c.cloud` with the username and password shared in the `credentials.txt` file.

```{warning}
Personally Identifiable Information (PII) is at risk if the credentials are compromised. Please report this immediately to 2i2c to revoke and renew any compromised credentials.
```
