(unlisted-image)=
# Starting and customizing the software environment of a user server

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
   - the docker `Image`, where you can choose from a list of pre-configured choices which image to use for the software environment
   - the `Node share` which represents the hardware resources available on the server. 

### The "Other" choice

If it was enabled, in the dropdown list of pre-configured choices of an option, there might be an entry called `Other`.

```{figure} ../../images/other-choice.png
:alt: The "Other" choice
```

Selecting this choice, will allow you to input a free-form text value for that particular option, other than the pre-configured choices.

(unlisted-image:specify-custom-image)=
## Specify your own custom image for the software environment

```{important}
Some important takeaways from previous section, that are relevant for the software environment customization.

1. The software environment that runs on a user server is defined by a docker image. By using a docker image, your are enabled to reproduce your work on other machines more easily.

2. The docker image of a user server can be:

- pre-defined by hub admins
- a list of choices that you can select from
- a special `Other` choice that enables you to input your own custom option choice
```

The special `Other` choice of the `Image` option allows you to specify your own image for the software environment, in the form of `docker_registry/organization/image_name:image_version`.

As an example, we can get the 2023.09.11 version of the pangeo notebook (that's not in the list of pre-configred choices) to run on a server with ~16GB of memory and ~2CPU (that's not the default node share) by:
1. selecting the `CPU only` profile
2. selecting the `Other` choice of the `Image` option (because 2023.09.11 version of the pangeo notebook is not available in the pre-configured list)
3. pasting `quay.io/pangeo/pangeo-notebook:2023.09.11` in the input field that appeared
4. selecting the pre-configured choice of `~16GB, ~2CPU` of the `Node Share` option
5. clicking the `Start` button

```{image} ../../images/new-server-custom-image.gif
```