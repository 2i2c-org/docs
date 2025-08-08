# Software environment and resources

JupyterHub can be configured to allow users to select their own environments before launching an interactive session.
There are a few ways that hub administrators can expose custom environments to their users. Below are a few sections that describe each one.

```{toctree}
:maxdepth: 1
choose.md
dynamic-imagebuilding.md
```

:::{admonition} Ask a hub administrator if these are not enabled
These guides will only work for community hubs that have this functionality enabled.
:::

## Why environment choice is useful

- Choosing from custom environments gives users more flexibility to in their use of tools without requiring a new JupyterHub
- Communities can define their own domain-specific environments.
- Communities can re-use and collaborate with other environment maintainers to avoid the burden of maintaining your own environment.
- Administrators can reduce cloud costs by asking users to request environments with more resources only when they really need it.
