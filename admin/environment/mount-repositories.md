(environment:mount-repositories)=
# Mount content to a local folder at startup

You can configure your hub to automatically mount content in a Git repository to every user's home directory when they start their server. This ensures users always have access to the latest version of shared content like documentation, teaching materials, or example notebooks.

## Example

Here's what this looks like in practice. When a user logs into their hub, they see a folder in their home directory that contains content from a GitHub repository:

```
📁 /home/jovyan/                          ← User's home directory
├── 📁 my-analysis/                       ← User's own work
├── 📁 mounted-docs/                      ← ⭐ Mounted from GitHub
│   ├── 📄 README.md
│   └── 📁 user-guide/
│       ├── 📄 getting-started.ipynb
│       └── 📄 advanced-analysis.ipynb
└── 📄 notebook.ipynb                     ← User's own work
```

The `mounted-docs/` folder is automatically synced from the GitHub repository, so when the repository is updated, users get the latest content on their next login.

## What is this useful for?

Automatically mounting repositories at startup is valuable for:

- **Research workflows**: Making documentation or analysis templates immediately accessible without requiring users to clone repositories manually
- **Educational content**: Distributing textbooks, demo files, or course materials that are always up-to-date
- **Shared resources**: Providing a source of truth for documentation that updates regularly without users needing to take action

Users don't need to know `git` or run any commands - the content is simply there when they log in.

## When to use this vs. nbgitpuller links

There are two ways to distribute Git repository content to hub users: **mounting repositories at startup** (this page) or **nbgitpuller links** (see [](#content:nbgitpuller)). Here's when to use each approach:

**Use nbgitpuller links when:**
- Different users or groups need access to **different repositories**
- Repository content varies by course, project, or use case
- You want users to access content on-demand by clicking a link
- You need flexibility to distribute multiple different repositories
- ⭐ Try this approach first, it is more lightweight and flexible

**Use repository mounting at startup when:**
- The same repository should be available to **all users** on the hub
- The repository is a fixed, known resource (like hub documentation or shared datasets)
- You want content available regardless of how users access the hub (direct login, custom links, etc.)
- Repository failures shouldn't prevent users from accessing their servers

## Request this feature

To request repository mounting for your hub:

1. Identify the Git repository you want to mount (must be publicly accessible)
2. Choose a folder name where it should appear in users' home directories
3. [Open a support ticket](../../support.md) with this information:
   - Repository URL
   - Target folder name
   - Which hub(s) should have this enabled

A 2i2c engineer will configure the repository mounting for you.

## How it works

This feature uses a Kubernetes init container that runs before a user's Jupyter server starts. The init container uses [nbgitpuller](https://nbgitpuller.readthedocs.io/) to clone the specified Git repository into the user's home directory.

An important safety feature: if the repository clone or update fails for any reason, the init container still allows the user's server to start. This ensures that problems with the repository don't prevent users from accessing their hub.

```{admonition} This will appear for all users of a hub
Mounted repositories will appear for **all users** on the hub, regardless of which server profile they choose. This is because the configuration is done at the Kubernetes level, rather than within JupyterHub's environment selection functionality.
```

## Configuration example

Here's what the configuration looks like (this is handled by 2i2c engineers), taken from the [NASA VEDA community hub](https://github.com/NASA-IMPACT/veda-hub-infrastructure). Feel free to open a PR to update your hub's configuration following a similar pattern:

```yaml
kubespawner_override:
  init_containers:
  - name: jupyterhub-gitpuller-init
    image: public.ecr.aws/nasa-veda/jupyterhub-gitpuller-init:97eb45f9d23b128aff810e45911857d5cffd05c2
    env:
    - name: TARGET_PATH
      value: veda-docs
    - name: SOURCE_REPO
      value: https://github.com/NASA-IMPACT/veda-docs
    volumeMounts:
    - name: home
      mountPath: /home/jovyan
      subPath: '{escaped_username}'
    securityContext:
      runAsUser: 1000
      runAsGroup: 1000
```

The configuration requires:
- **TARGET_PATH**: The folder name where the repository will be mounted (relative to the user's home directory)
- **SOURCE_REPO**: The URL of the Git repository to clone

## Related resources

- [](#environment:image) - Customize the software environment
- [](#environment/default) - Learn about the default environment
- [2i2c infrastructure docs on git-pull](https://infrastructure.2i2c.org/howto/features/git-pull/) - Technical documentation for 2i2c engineers
