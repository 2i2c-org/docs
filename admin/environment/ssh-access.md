# Enable SSH Access

For advanced workflows, users often prefer working from their local terminal or connecting local IDEs (like [VS Code Remote](https://code.visualstudio.com/docs/remote/ssh)) directly to their cloud environment. You can enable this by running a lightweight SSH server inside the user's container, accessible via a secure websocket tunnel.

## How it works

The tool [jupyter-sshd-proxy](https://github.com/yuvipanda/jupyter-sshd-proxy) runs an SSH server (sshd) inside the user's session. It uses [jupyter-server-proxy](https://jupyter-server-proxy.readthedocs.io/) to expose this server over the standard JupyterHub web connection.  
**Benefits:**

* **No Firewall Changes:** It works entirely over HTTPS/Websockets.  
* **Secure:** Authentication is handled by JupyterHub; no separate SSH keys are required to *reach* the server (though keys are used for the SSH session itself).  
* **File Transfer:** Enables scp and rsync for easy data movement.

## Prerequisites

### 1\. For Administrators (Hub Configuration)

You must ensure your single-user Docker image includes:

* openssh-server (see [OpenSSH](https://www.openssh.com/))  
* jupyter-sshd-proxy

**Example values.yaml:**  
jupyterhub:  
  singleuser:  
    profileList:  
      \- display\_name: "SSH Enabled Environment"  
        description: "Standard environment with SSH support"  
        kubespawner\_override:  
          \# Ensure this image has jupyter-sshd-proxy installed  
          image: "quay.io/yuvipanda/pangeo-jupyter-sshd-proxy:latest" 

### 2\. For Users (Local Configuration)

Connecting requires a one-time setup on the user's local machine.  
Step A: Install a WebSocket Client  
Your local SSH client needs a helper tool to pipe data to the hub's websocket. We strongly recommend websocat because it handles binary streams natively and supports all major operating systems.

* **Mac:** brew install websocat  
* **Linux:** Download the binary from [GitHub releases](https://github.com/vi/websocat/releases).  
* **Windows:** Use winget install websocat or download the binary.

*(Note: Other tools like [wscat](https://github.com/websockets/wscat) or custom Python scripts can be used if they support binary piping to stdin/stdout, but websocat is the standard).*  
Step B: Configure SSH  
Add the following block to your local \~/.ssh/config file.  
Host myhub  
  User jovyan  
  \# The %h token is replaced by the hostname (hub.example.com)  
  \# The %p token is ignored but kept for compatibility  
  ProxyCommand websocat \--binary \-H="Authorization: token \<YOUR-API-TOKEN\>" asyncstdio:wss://\<HUB-URL\>/user/\<YOUR-USERNAME\>/sshd/

:::{important}  
Users must generate an API Token from their JupyterHub Control Panel (/hub/token) and paste it into the ProxyCommand.  
:::

## Community Examples

[**Openscapes**](https://openscapes.org/) uses this workflow to allow researchers to use VS Code Remote and transfer large datasets efficiently.

* [**Openscapes SSH Documentation**](https://www.google.com/url?sa=E&source=gmail&q=https://openscapes.github.io/series/core-lessons/jupyterhub/ssh.html): A user-facing guide on setting up the connection.  
* [**Infrastructure Config**](https://github.com/Openscapes/openscapes.cloud/pull/67): See the Pull Request where SSH support was refined.

:::{seealso}

* [Not Just for Notebooks: JupyterHub in 2025](https://www.youtube.com/watch?v=vsbHMvvsFw8) — Yuvi Panda's talk covering SSH access and other interfaces.  
* [jupyter-sshd-proxy Repository](https://github.com/yuvipanda/jupyter-sshd-proxy) — Official documentation and troubleshooting.  
* VS Code Remote \- SSH — Documentation on connecting VS Code to a remote server.  
  :::