# Prometheus API access

## Overview

It is possible to directly query the Prometheus API from the outside world at `https://prometheus.<cluster_name>.2i2c.cloud`.

Use cases include configuring Prometheus as a datasource for your own monitoring systems, such as [AWS CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_MultiDataSources-Connect.html#MultiDataSources-Prometheus) or another Grafana instance.

## Steps

Sharing credentials to access your Prometheus instance from the outside world needs to be done securely. This is because Personally Identifiable Information (PII) is at risk if the credentials are compromised.

```{warning}
Please do not share these credentials through any insecure channels, and notify us immediately if you need to renew them.
```

1. Send a [support request](/support.md) to 2i2c
   - Ask for credentials to be provisioned for access to `https://prometheus.<cluster_name>.2i2c.cloud`

1. 2i2c will respond with a secure [Bitwarden Send](https://bitwarden.com/products/send/) link that will expire in 7 days. Click the link to see the username and password. Store this securely, using Bitwarden or other similar secure password managers.

1. You can now access `https://prometheus.<cluster_name>.2i2c.cloud` with the username and password.

```{warning}
Personally Identifiable Information (PII) is at risk if the credentials are compromised. Please report this immediately to 2i2c to revoke and renew any compromised credentials.
```
