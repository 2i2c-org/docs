# User server culling

To ensure efficient resource usage, user servers without interactive usage for a
period of time (default `1h`) are automatically stopped (via
[jupyterhub-idle-culler](https://github.com/jupyterhub/jupyterhub-idle-culler)).
This means your notebook server might be stopped for inactivity even if you have
a long running process in the notebook. This timeout can be configured.

% TODO: Add link to SRE guide on how to configure this, once it exists

Culling has the same effect as [stopping a user's server](user-server/stopping).

There is currently no maximum time limit for a user's notebook.
