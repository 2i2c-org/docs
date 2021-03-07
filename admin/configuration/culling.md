# User server culling

To ensure efficient resource usage, user servers without interactive usage for a
period of time (default 1h) are automatically stopped (via
[jupyterhub-idle-culler](https://github.com/jupyterhub/jupyterhub-idle-culler)).
This means your notebook server might be stopped for inactivity even if you have
a long running process in the notebook. This timeout can be configured.

This has the same effect as a user stopping their own server. User servers stopping doesn't lose any data in your home directories. However, any packages temporarily installed via `!pip` or `!conda` are cleared, to make sure that everyone in the hub is operating from the same clean environment as much as possible. Active notebooks have their kernel killed as well.

There is currently no maximum time limit for a user's notebook.
