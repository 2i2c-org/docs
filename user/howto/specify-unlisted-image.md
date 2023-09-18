# Specify your own custom image for the software environment

To start a server on the Hub, you need to go to the hub's home page, then click on the `Start My server button`.

Depending on how your hub was set up, after clicking the button, you will be:

1. either redirected to _"the spawn page"_, where a bunch of logs and a progress bar will indicate that a server will be created. This server will use a software environment, i.e. a docker image, that was pre-configured by the hub admins.

2. or presented first with a list of _"Server Options"_ that will allow you to configure this server before it will be spawned for you.

The first case is straightforward, so let's dive into the one that needs you to choose your server options.

## The Server Options

The `Server Options` is a page that will allow you to configure the server that will be created and started for you.

### Profiles and Options

You can choose from different pre-configured _"profiles"_ and for each profile you can choose from different pre-configured _"options"_.

```{figure} ../../images/server-options.png
:alt: Server Options page example
```

The image above represents a `Server Options` page example, where you can choose:
- either a `"CPU only"` or a `"GPU"` **profile**
- and for each profile, you can select from a list of pre-configured **options**.
  The options are:
   - the docker `Image` that defines the software environment
   - the `Node share` which represents the hardware resources available on the server. 

### The "Other" option

