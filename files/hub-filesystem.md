# The JupyterHub Filesystem

Your notebook server is a linux "virtual machine" with its own filesystem.
You are not on a shared server; you are on your own private server.

The easiest way to move files in and out of your home directory is via the JupyterLab web interface.
Drag a file into the file browser to upload, and right-click to download back out.
You can also open a terminal via the JupyterLab launcher and use this to ssh / scp / ftp to remote systems.
However, you can’t ssh in!

## Your Home Directory

Your username is ``jovyan``, and your home directory is ``/home/jovyan``.
This is the same for all users, but no one else can see or access the files in *your* home directory.

``/home/jovyan`` is a persistant network-attached drive. Any files you put there will be there when you
log out and log back into the JupyterHub. 

The ``/home/jovyan`` space is typically limited to 10 GB. Consequently, your home directory is intended 
only for notebooks, analysis scripts, and small datasets (< 1 GB). It is not an appropriate place to store 
large datasets.

## The `shared` Directory

All users have a directory called `shared` in their home directory.
This is a *readonly* directory - anybody on the hub can *access* and *read from* the `shared` directory.
The hub administrator may choose to distribute shared materials via this directory.
The `shared` directory is not intended as a way for hub users to share data with each other.

## The `/tmp` Directory

Any directory outside of ``/home/jovyan`` is emphemeral on Cloud-hosted JupyterHubs. This means if you 
add data or scripts under a writeable directory like `/tmp/myfile.txt` *it will not be there when you
log out and log back in*. 

Nevertheless, `/tmp` is a convenient location for storing data temporarily 
because it is a fast SSD drive. The space available depends on your server but will generally be much 
larger than ``/home/jovyan`` (50-100s of GB).
