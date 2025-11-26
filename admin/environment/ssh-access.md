# Remote SSH access

You can let users connect to their hub session with SSH for terminal work, VS Code Remote, or file transfer with `scp`/`rsync`. This runs an SSH server inside the same user container and exposes it over HTTPS.

## How it works

- [`jupyter-sshd-proxy`](https://github.com/yuvipanda/jupyter-sshd-proxy) starts `sshd` inside the user server and publishes it through [`jupyter-server-proxy`](https://jupyter-server-proxy.readthedocs.io/) at `/sshd/` over WebSockets.  
- Authentication and authorization come from JupyterHub - no extra inbound ports or firewall changes are needed.  
- The SSH session uses the same CPU, memory, and storage limits as the Jupyter server.

## User image requirements

Install the following in the user image (see [](customize.md)):

- `openssh-server`
- `jupyter-sshd-proxy`
- `jupyter-server-proxy`

Example `values.yaml` profile:

```
jupyterhub:
  singleuser:
    profileList:
      - display_name: "SSH enabled"
        slug: "ssh"
        kubespawner_override:
          image: "quay.io/yuvipanda/pangeo-jupyter-sshd-proxy:latest"  # includes jupyter-sshd-proxy
```

You can also add these packages to your own image instead of using the example image above.

## Local setup (users)

1. Install a WebSocket helper for your SSH client (recommended: [`websocat`](https://github.com/vi/websocat/releases)).
2. Create a JupyterHub API token from `/hub/token` on your hub.
3. Add an SSH config entry in `~/.ssh/config` (replace placeholders):

```
Host myhub
  HostName <your-hub-hostname>        # e.g., myhub.pilot.2i2c.cloud
  User jovyan
  ProxyCommand websocat --binary -H="Authorization: token <API_TOKEN>" asyncstdio:wss://%h/user/<JUPYTERHUB_USERNAME>/sshd/
```

Then connect with `ssh myhub` or point VS Code Remote - SSH at the `myhub` host. The ProxyCommand is reused by `scp` and `rsync`.

:::{admonition} Keep these tokens private!
Keep the API token private and rotate it from `/hub/token` if it is exposed.
:::

## Community examples

* Openscapes (https://openscapes.org/) uses this workflow for VS Code Remote and large data transfers: https://github.com/Openscapes/openscapes.cloud/blob/main/ssh-into-hub.qmd  
* Configuration pull request: https://github.com/Openscapes/openscapes.cloud/pull/67

:::{seealso}

* [jupyter-sshd-proxy repository](https://github.com/yuvipanda/jupyter-sshd-proxy) - setup and troubleshooting  
* [VS Code Remote - SSH](https://code.visualstudio.com/docs/remote/ssh) - connect the VS Code client to the SSH host  
* [Not Just for Notebooks: JupyterHub in 2025](https://www.youtube.com/watch?v=vsbHMvvsFw8) - talk covering SSH access and other interfaces for JupyterHub
:::

## Acknowledgements

- This guide was originally [written by Andy Teucher for OpenScapes](https://github.com/Openscapes/openscapes.cloud/pull/67) and its content was modified for these docs.
