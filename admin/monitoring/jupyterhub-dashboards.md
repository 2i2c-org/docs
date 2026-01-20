# JupyterHub Default Dashboards

:::{figure} images/grafana-dashboard.png
:alt: Screenshot of a JupyterHub Grafana dashboard
The "Activity" Grafana dashboard.
:::

The `JupyterHub Default Dashboards` folder shows dashboards deployed from the upstream [https://github.com/jupyterhub/grafana-dashboards](https://github.com/jupyterhub/grafana-dashboards) project.

1. **Activity**

  This dashboard contains information about the number of running servers, daily, weekly and monthly active users.

1. **Cluster Information**

   Contains panels with node-level usage such as:
   - node count
   - memory
   - cpu
   - running users per hub in cluster
   - pod health

1. **Home Directory Usage**

   See the disk space occupied by user home directories, as well as last modified and number of files.

1. **JupyterHub Dashboard**

   Hub usage stats and hub diagnostics, such as
   - software images pulled by user pods
   - user CPU usage distribution
   - user memory usage distribution
   - server start times
   - hub response latency

  There is also a Panel section about `Anomalous user pods` where pods with high CPU usage or high memory usage are tracked.

1. **NFS usage, NFS server and Prometheus server diagnostics**

   This provides info about the NFS usage diagnostics, such as iops, and monitors things like CPU, memory, disk and network usage of the NFS server and Prometheus instance.

1. **Usage Report**

   This provides a report about the memory requests, grouped by username, for notebook nodes and dask-gateway nodes. It also provides a graph that monitors GPU requests per user pod.

1. **User Diagnostics**

   This displays cpu and memory usage and requests per user, as well as home directory usage.

1. **User Group Diagnostics**

   This displays cpu and memory usage and requests per user group, as well as home directory usage. Only applies if users are assigned user groups at the authentication layer.

## Making changes to Grafana dashboards

If you make any changes to the pre-configured dashboards in the *JupyterHub Default Dashboards* and *Cloud Cost Dashboards* folders, then they will not be saved.

We encourage you to create new dashboards outside of these folders (however the configurations will not be backed up), or even contribute to:

- the upstream [https://github.com/jupyterhub/grafana-dashboards](https://github.com/jupyterhub/grafana-dashboards) project for *JupyterHub Default Dashboards*
- the [https://github.com/2i2c-org/jupyterhub-cost-monitoring](https://github.com/2i2c-org/jupyterhub-cost-monitoring) project for *Cloud Cost Dashboards*

## Resources

Grafana is a powerful open source data visualization tool with many features. For more information on how to use Grafana, refer to the [Grafana documentation](https://grafana.com/docs/grafana/latest/).