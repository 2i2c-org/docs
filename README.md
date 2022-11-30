# 2i2c Managed Hub Service Documentation

This repository serves as the user-facing documentation and communication space for those who are using 2i2c Hubs.

Most of the infrastructure that we discuss in the documentation is deployed [in the `infrastructure/` repository](https://github.com/2i2c-org/infrastructure).

See [the service documentation](https://docs.2i2c.org) for more information.

## How to preview this documentation

To preview this documentation, use the `Nox` tool.
First install it:

```
pip install nox
```

To build the documentation and place the HTML files in `_build/html`:

```
nox -s docs
```

To build the documentation with a server that **watches for changes and auto-builds the documentation with a preview**, run the following:

```
nox -s docs -- live
```
