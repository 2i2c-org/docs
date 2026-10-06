# Filesystem and user directory

Your notebook server is a linux "virtual machine" with its own filesystem.
Other users can't see your files or what you're running in your session.

The easiest way to move files in and out of your home directory is via the web interface. Drag a file into the file browser to upload, and right-click to download back out.

```{note}
With JupyterLab, there is a maximum file size transfer limit of 250MB. This is because the entire file is read into memory and cannot be streamed.
```

You can also open a terminal via the UI and use this to ssh / scp / ftp to remote systems.

You can ssh into the hub if your hub admin has enabled [Remote SSH access](../../admin/environment/ssh-access.md). This can be used for large file transfers.

```{warning}
Downloading files out of the hub incurs cloud costs, known as a [data egress fee](https://infrastructure.2i2c.org/topic/billing/chargeable-resources/#ingress-and-egress-fees).
```

## Your Home Directory

Your username is `jovyan`, and your home directory is `/home/jovyan`.
This is the same for all users, but no one else can see or access the files in *your* home directory.

`/home/jovyan` is a persistent network-attached drive.
The files you put there will persist after you log out and log back in.
Use your home directory for notebooks and code, but we **discourage storing data in your home drive**.
Storing data in your home drive can become expensive and slow.

For storing temporary data, use [the `/tmp` folder](#filesystem:tmp). For data you want to keep, use [cloud object storage](./object-storage/index.md).

(filesystem:storage-quotas)=
### Per-User Storage Quotas

All of our hubs have a 10GB storage quota per-user by default, although this may vary depending on the hub.

You can check how much storage you are using by running the `du` command in a terminal.
Since many hubs link a `~/shared` folder, we exclude that from our file size tally:

```bash
$ du -sh --exclude='shared*' $HOME
196M    /home/jovyan
```

If you go over the quota limit, then you may experience degraded performance on your server. Contact your hub administrator if you run into any problems.

```{note}
`df -h` shows the *total size* of each disk, not your home directory quota.
```

:::{seealso}
- If your hub has a **Usage** dashboard, it shows your home storage usage and quota. See [](../usage-quota-dashboard.md).
- **For hub administrators:** see [](#monitoring:disk-usage) for quotas on shared directories and usage across all users.
:::

### Modify your bash profile

You may edit your bash profile at `~/.bash_profile`.
However, **be careful** because some edits may have unanticipated consequences.
For example, if you change your shell such that it can no longer launch a Jupyter Server, then your session will fail to start.
This may happen if you **change your default shell** to something like [zsh](https://ohmyz.sh/).

If you change your `~/.bash_profile` and something suddenly breaks, try reverting the change to this file.
If your session can no longer start, [email support](#support) as this file may need to be manually edited or deleted.

## The `shared` Directory

All users have a directory called `shared` in their home directory.
This is a *readonly* directory - anybody on the hub can *access* and *read from* the `shared` directory.
The hub administrator may choose to distribute shared materials via this directory.
The `shared` directory is not intended as a way for hub users to share data with each other.

(filesystem:tmp)=
## The `/tmp` Directory

`/tmp` is fast, temporary storage for files that will be deleted when your server stops.
It is useful for things like generating intermediate data as part of a pipeline, storing temporary large files, etc.

By default, `/tmp` is on a disk on the same machine where your server runs.
The space available varies by community, but is usually around `20-30GB` per user.
If you hit your limit in `/tmp`, your server may restart and you'll lose what's in `/tmp`.

If you need more space in `/tmp`, [contact support](#support).

(filesystem:tmp-dedicated)=
### Dedicated `/tmp` disk

Some hubs let you pick a dedicated `/tmp` disk when you start your server.
When your server starts, the hub will create a new cloud disk that is *just for you*, and mounts it at `/tmp`. 
This is useful when your work needs more temporary space than the standard `/tmp` provides.

For example, the uw-escience hub has a {gui}`Scratch Disk on /tmp` option with a {gui}`Dedicated 500GB` choice ([see its configuration](https://github.com/2i2c-org/infrastructure/blob/3278bfdb5258c806feeac5a7c7eb4e6ea8fc9f2c/config/clusters/uw-escience/common.values.yaml#L97-L131)).

:::{seealso}
**For hub administrators:** see [](#admin:tmp-dedicated) to offer dedicated `/tmp` disks on your hub.
:::
