# Get started contributing

Most of this repository is structured for **Sphinx**, a documentation engine in Python.

## Build the documentation locally

The easiest way to build the documentation in this repository is to use `nox`, a tool for quickly building environments and running commands within them.
This ensures that your environment has all the dependencies needed to build the documentation.

To do so, follow these steps:

1. Install `nox`

   ```
   pip install nox
   ```
2. Build the documentation:

   ```
   nox -s docs
   ```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `_build/html`.

To build live documentation that updates when you update local files, run the following command:

```
nox -s docs -- live
```

## Documentation deployment

This documentation is automatically deployed to [docs.2i2c.org](https://docs.2i2c.org) using [Read the Docs](https://readthedocs.org/).

The build process is configured in [`.readthedocs.yml`](../.readthedocs.yml)
