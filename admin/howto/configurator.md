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

```{note}
More settings are slowly being made accessible over this
interface, so if you have specific ideas on what should be added here, please
[create an issue](https://github.com/yuvipanda/jupyterhub-configurator/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
```

## Accessing the Configurator

The Configurator is only available to admins, and can be accessed from the
control panel. You can access the Control Panel in the following ways:

1. In classic Jupyter notebook, click the 'Control Panel' button in the top right.
2. In JupyterLab, select 'File -> Hub control panel' from the menu bar.
3. For other interfaces (like RStudio), you can accses it with the following URL:
   `https://<hub-url>/hub/home`.
   
Once you're at the control panel, you can access the configurator under
`Services` in the top navigation bar. It will ask you to authenticate to the
configurator so it knows you are an admin. Once done, you will see the
configurator interface!

## Making changes

This interface should now let you change some settings and save them. They should
take effect next time you or any of your users start a server. 

```{warning}
You **must** click the submit button at the bottom of the form for your changes
to take effect!
```
