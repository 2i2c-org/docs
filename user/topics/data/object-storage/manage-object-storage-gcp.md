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

## List prefixes within a GCP bucket

