# Filesystem and user directory

Your notebook server is a linux "virtual machine" with its own filesystem.
You are not on a shared server; you are on your own private server.

The easiest way to move files in and out of your home directory is via the JupyterLab web interface.
Drag a file into the file browser to upload, and right-click to download back out.
You can also open a terminal via the JupyterLab launcher and use this to ssh / scp / ftp to remote systems.
However, you can’t ssh in!

## Your Home Directory

Your username is ``jovyan``, and your home directory is ``/home/jovyan``.
This is the same for all users, but no one else can see or access the files in *your* home directory.

``/home/jovyan`` is a persistent network-attached drive. Any files you put there will be there when you
log out and log back into the JupyterHub.

The ``/home/jovyan`` space is intended only for notebooks and code. It's **not** an appropriate place to store
datasets, as it can get really expensive (and slow) when used that way.

### Per-User Storage Quotas

All of our hubs have a 10GB storage quota per-user by default, although this may vary depending on the hub.

You can check how much storage you are using by running the `du` command in a terminal:

```bash
$ du -skh ~
196M    /home/jovyan
```

If you go over the quota limit, then you may experience degraded performance on your server. Contact your hub administrator if you run into any problems.

For temporarily storing large datasets, take a look at the {ref}`/tmp directory<filesystem:tmp>` section below.

For storing data in cloud object storage, see the section [Cloud Object Storage](./object-storage/index.md).

### Modify your bash profile

You may edit your bash profile at `~/.bash_profile`.
However, **be careful** because some edits may have unanticipated consequences.
For example, if you change your shell such that it can no longer launch a Jupyter Server, then your session will fail to start.
This may happen if you **change your default shell** to something like [zsh](https://ohmyz.sh/).

If you change your `~/.bash_profile` and something suddenly breaks, try reverting the change to this file.
If your session can no longer start, [email support](support:email) as this file may need to be manually edited or deleted.

## The `shared` Directory

All users have a directory called `shared` in their home directory.
This is a *readonly* directory - anybody on the hub can *access* and *read from* the `shared` directory.
The hub administrator may choose to distribute shared materials via this directory.
The `shared` directory is not intended as a way for hub users to share data with each other.

(filesystem:tmp)=
## The `/tmp` Directory

Any directory outside of ``/home/jovyan`` is ephemeral on cloud-hosted JupyterHubs. This means if you 
add data or scripts under a writeable directory like `/tmp/myfile.txt` *it will not be there when you
log out and log back in*.

Nevertheless, `/tmp` is a convenient location for storing data temporarily 
because it is a fast SSD drive. The space available depends on your server but will generally be much 
larger than ``/home/jovyan`` (50-100s of GB).
