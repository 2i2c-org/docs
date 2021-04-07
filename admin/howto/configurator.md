# Configure the hub as an admin with the Configurator

The [JupyterHub configurator](https://github.com/yuvipanda/jupyterhub-configurator)
allows admins to change a subset of hub settings without requiring involvement
from 2i2c engineers.

```{warning}
Be careful while changing these settings! We don't expose anything that can
make the hub inaccessible to *admins*, but you can still change things that
break user server starts. You can always fix it by undoing the change that broke
it, and a way to see the 'version history' of your config changes is in the
works.
```

## Access the Configurator

The Configurator is only available to admins, and can be accessed from the
control panel. You can access the Control Panel in the following ways:

1. In classic Jupyter notebook, click the `Control Panel` button in the top right.
2. In JupyterLab, select `File -> Hub control panel` from the menu bar.
3. For other interfaces (like RStudio), you can accses it with the following URL:
   `https://<hub-url>/hub/home`.
   
Once you're at the control panel, you can access the configurator under
`Services` in the top navigation bar. It will ask you to authenticate to the
configurator so it knows you are an admin. Once done, you will see the
configurator interface!

## Make and save changes

This interface should now let you change some settings and save them. They should
take effect next time you or any of your users start a server. 

```{warning}
You **must** click the submit button at the bottom of the form for your changes
to take effect!
```

## Available settings

The following settings are currently available via the Configurator.

```{note}
More settings are slowly being made accessible over this
interface, so if you have specific ideas on what should be added here, please
[create an issue](https://github.com/yuvipanda/jupyterhub-configurator/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
```

### User docker image

The docker image that will be launched for each user. This controls the languages,
libraries and interfaces accessible to the user. You can leave it blank to use the
default image maintained by 2i2c. We also have [more information](environment) on
how to manage your user environment.

### Default interface

Sets the [default interface](../configuration/default-interface.md) your users
will see when they log in.

```{note}
If you are using a custom docker image, you should make sure these interfaces are
available in your docker image! If you used [repo2docker](https://repo2docker.readthedocs.io) to
build your images (which [we recommend](environment/custom)), the
interfaces should be automatically available.
```

```{note}
There's a 'interface selector' in the hub home page, but unfortunately that
does not reflect this option. So if your user selects an interface there, they
will be put in that interface but just for the first time after they log in. After
that, your selection here will determine what UI they will see.
```
