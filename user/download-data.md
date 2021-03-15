# Download your home directory

You might want to download your entire home directory for many
reasons - to get data off a hub that is closing, to migrate to
a different service, for archival purposes, etc. Your home directory
will contain all your data *and* your notebooks.
Hubs managed by 2i2c make this easy.

1. **Open the classic Jupyter Notebook file browser.** If you are
   using another interface, navigate to the classic interface by changing your
   URL path to `/tree`. e.g.,
   `<your-hub>.pilot.2i2c.cloud/user/<your-username>/tree`

2. Click on **`Download Directory`**.

   ```{figure} ../images/download-directory.png
   :alt: The download directory button
   ```

This will zip up the contents of your user file system and download them to your machine.

:::{note}
If your hub is using a [custom user environment](environment/custom), it needs the
[jupyter-tree-download](https://github.com/ryanlovett/jupyter-tree-download) package
installed to make this feature available.
:::
