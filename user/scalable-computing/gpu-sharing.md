# GPU sharing

On GCP, hubs can split a single GPU into smaller time-sliced shares, so more people get GPU access at once instead of needing a dedicated GPU per user. It's a good fit for teaching and other light GPU workloads.

See [2i2c's blog post](https://2i2c.org/blog/more-users-fewer-gpus/) and the [GPU time-sharing setup guide](https://infrastructure.2i2c.org/howto/features/gpu/) for details.

:::{admonition} For hub administrators
:class: seealso
To enable GPU sharing on your hub, [open a support request](../../support.md).
:::

:::{admonition} Example use by communities
:class: seealso
2i2c's [CloudBank Classroom hub config](https://github.com/2i2c-org/infrastructure/blob/49af1ed86c9819ecc6d29e9874030ba6ac862634/terraform/gcp/projects/cloudbank.tfvars#L398-L410) splits a T4 GPU node pool into 2 time-sliced shares, giving a whole class GPU access from a single node.
:::
