# User server management

## Take control of a user's server

Hub admins can unilaterally perform actions on a user's server via the
**Administrator's Panel**. These are primarily used to debug a user's session
easily.

You can access the admin panel by clicking the {guilabel}`Admin` button in the top bar
in your hub control panel.  Alternatively, you can go to this URL in your
browser: `https://<your-hub-url>/hub/admin`.

(user-server:access)=
### Access a user's server

Accessing a user's server is useful when trying to debug or reproduce an issue they might have. This facility is available to admins via the admin panel.

1. In the admin panel, you can click {guilabel}`access server` to gain control of a user's
   currently running server. If it isn't running, you can click {guilabel}`start server`
   first and wait for it to start.

   ```{figure} ../../images/access-server.png
   Clicking "access server" will allow you to control the user's session.
   ```

2. This will bring you to the default interface that the user would have seen if they had just logged into the hub. From here, you can navigate to the notebook the user has reported issues with, and help them debug.

   :::{warning}
   If you both work on the same notebook at the same time, you will just
   overwrite each other's code! The state of the notebook will be that of
   whoever saved the notebook last. There is no Google Docs' style
   real-time collaboration yet, although [it is coming](https://github.com/jupyterlab/rtc)
   :::

   :::{warning}
   When you control a user's server, all of your actions will be run *as
   if the user ran it themselves*. This can be confusing for some users
   and is generally not best-practice. We recommend telling users when
   you are taking over their session, and using this feature mostly to understand what the user was trying to do, rather than to make major
   changes to their code or notebook outputs.
   :::
   
### Access user logs

The logs for each user server are located in their home directory, at `~/.jupyter-server-log.txt`.
These contain information about every event that occurred as a part of a user's session, and are useful for debugging unexpected errors and problems.

For example, to print the contents of your own user server log:

1. Open a terminal (e.g., in JupyterLab)
2. Run the command:

   ```console
   $ cat ~/.jupyter-server-log.txt
   ```

To access a **different user's** server logs, you can [access their server](user-server:access) and run the same command above to print their logs.

(user-server/stopping)=
### Stop or start a user's server

Sometimes, you need to just turn a user's server on and off. You can
also do this from the admin interface, by hitting the {guilabel}`Stop server`
button, waiting for the server to stop, and the {guilabel}`Start server` button
again.

This is particularly useful when their session might have gotten
out of whack by packages they've installed temporarily that screwed up
the default, since a restart will wipe the slate clean.

:::{important}
When a user's server is stopped (by an admin, or by the user themselves), no data is lost in the user's home directory.
However, any packages temporarily installed via `!pip` or `!conda` are cleared, to make sure that everyone in the hub is operating from the same clean environment as much as
possible.
Active notebooks have their kernel killed as well.
:::

## Stop user servers after inactivity

To ensure efficient resource usage, user servers without interactive usage for a
period of time (default `1h`) are automatically stopped (via
[jupyterhub-idle-culler](https://github.com/jupyterhub/jupyterhub-idle-culler)).
This means your notebook server might be stopped for inactivity even if you have
a long running process in the notebook. This timeout can be configured.

% TODO: Add link to SRE guide on how to configure this, once it exists

Culling has the same effect as [stopping a user's server](user-server/stopping).

There is currently no maximum time limit for a user's notebook.

## Stop user kernels after inactivity

In addition to the user _server_, there may also be culling at the _kernel_ level.
The kernel is the thing that actually "runs code", and a kernel without any activity for some time means that somebody has not executed code in that time.

By default, kernels will be checked for activity **every `5 minutes`**.
All kernels that haven't shown activity in **in the last hour** will be stopped by the [jupyterhub-idle-culler](https://github.com/jupyterhub/jupyterhub-idle-culler).

This window can be configured if you'd like to change the window of inactivity needed before user kernels will be stopped.
See the [Hub Engineer's guide](infra:configure:culling) for some documentation on this.

% TODO: Add link to SRE guide on how to configure this, once it exists

## Disable hub access for all users

In some cases, you may want to temporarily disable hub access for all users.
For example, if you are concerned that users on your hub are taking inappropriate actions, and you wish to stop all activity before investigating.

**To prevent all user sessions from starting**, you can use [the configurator UI](configurator.md) to choose a user image that does not start.

1. Go to your hub's configurator menu (at `{{ your hub URL }}/services/configurator`).
2. Under {guilabel}`User Docker Image`, paste the following text:

   ```
   busybox:latest
   ```

   This specifies a user image that is not compatible with JupyterHub, and will prevent user sessions from starting.
   You can revert this change by deleting the text and hitting {guilabel}`Submit` again (or changing it back to its previous value).

3. Hit {guilabel}`Submit`
4. **Stop all user sessions** from you Administrator panel.
   
   Go to `{{ your hub URL }}/hub/admin` and click {guilabel}`Stop All`.

   This will stop all user sessions, and they will no longer be able to log in after doing so.

If you do this, you should [notify the 2i2c support team](https://docs.2i2c.org/en/latest/support.html) as they may need to follow up with some changes to your infrastructure.
