# Launch a dask-gateway cluster

This guide shows you how to launch a Dask gateway cluster for parallel and distributed computing.

:::{contents}
:depth: 2
:local:
:::

## What is Dask Gateway?

Dask Gateway allows users to launch clusters for scaling computations efficiently with more CPU and memory on cloud resources, without requiring direct access to the underlying Kubernetes backend of the 2i2c hub. Configuration, such as efficient cluster resourcing, authentication and security settings, is automatically handled for users to provide a consistent user experience across the hub.

:::{admonition} What's the difference between Dask and Dask Gateway
:class: note
When using Dask on a local machine, you will often instantiate a cluster using
```python
from dask.distributed import LocalCluster
cluster = LocalCluster()
client = cluster.get_client()
```
For a 2i2c Dask hub, we instantiate a cluster with Dask Gateway that requests cloud resources with Kubernetes from a shared, centrally managed cluster environment.
:::

## Usage

This section roughly follows the [Dask Gateway Docs – Usage](https://gateway.dask.org/usage.html) together with the [Training on Large Datasets](https://examples.dask.org/machine-learning/training-on-large-datasets.html) example.

:::{warning}
Avoid large, long-running, idle clusters, which consume cloud computing resources and costs. Only use a cluster when you need it and shutdown when not in use.
:::

### Connect to a dask-gateway server

Create a gateway client to communicate with the dask-gateway server.

```python
from dask_gateway import Gateway
gateway = Gateway()  # Use values stored in your local configuration (recommended)
```

:::{note}
Leave the argument of the `Gateway()` constructor empty to use the default configuration for your 2i2c Dask hub which automatically supplies parameters such as `address`, `proxy_address`, `auth`, etc.
:::

### Configure cluster options

Specify options for your gateway cluster with the options widget.

```python
options = gateway.cluster_options()
options
```

:::{image} media/dask-options.png
:alt: Screenshot of an interactive options widget to configure gateway cluster options.
:align: center
:::

#### Cluster options

Instance type running worker containers
: This defaults to the machine type `n2-high-mem16` for Google Cloud and `r5.4xlarge` for AWS, with a maximum of 16 CPUs available.

Resources per worker container
: Select 1/2/4/8/16 CPUs and corresponding memory requests from a dropdown menu.

Image
: User image on the client side is automatically defined to match the Dask gateway version on the server side.

Environment variables (YAML)
: Set environment variables for both the workers and schedulers using YAML, e.g. `ENV_VAR: my_environment_variable`.

Idle cluster terminated after (minutes)
: This defaults to 30 minutes. Consider cloud computing resources and costs for your hub when setting this value.

### Create and scale gateway cluster

Pass the cluster options to a new gateway cluster.

```python
cluster = gateway.new_cluster(options)
cluster
```

:::{note}
If a new gateway server needs to be started, then this process can take around 5 minutes to complete.
:::

#### Manual scaling

Manually scale the cluster size to a fixed number of workers.

1. Expand the *Manual scaling* dropdown in the cluster widget.
1. Select the number of workers.
1. Click {guilabel}`Scale` to confirm.

:::{image} media/dask-scaling-manual.png
:alt: Screenshot of an interactive cluster widget to configure manual worker scaling.
:align: center
:::

#### Adaptive scaling

Adapt the cluster size dynamically based on current load. This helps to scale up the number of workers when necessary but scale it down and save resources when not actively computing.

1. Expand the *Adaptive scaling* dropdown in the cluster widget.
1. Select the minimum and maximum number of workers.
1. Click {guilabel}`Adapt` to confirm.

:::{image} media/dask-scaling-adaptive.png
:alt: Screenshot of an interactive cluster widget to configure adaptive worker scaling.
:align: center
:::

(dask:connect-gateway)=
### Connect to the gateway cluster

Connect to the gateway cluster to start doing work with your workers.

```python
client = cluster.get_client()
client
```

Make a note of the dashboard address of the form `service/...` to connect to the Dask dashboard.

### Connect Dask dashboard to Dask JupyterLab extension

Connect to a [Dask dashboard](https://docs.dask.org/en/latest/dashboard.html) to monitor computations with the JupyterLab extension.

1. Copy the dashboard address from {ref}`Connect to the gateway cluster<dask:connect-gateway>` or from running the command `client.dashboard_link`
1. Click the ![Dask icon](media/dask-icon.png) Dask icon in the left sidebar.
1. In the search box at the top of the panel, paste in the full dashboard URL of the form
   ```bash
   https://<hub-name>.<community-name>.2i2c.cloud/<dashboard-address>
   ```
1. Select the diagnostic plots to visualize, e.g. workers memory, CPU, task stream.

### Run computations on the cluster

Import the Python packages for the [Train Models on Large Datasets](https://examples.dask.org/machine-learning/training-on-large-datasets.html) example.

```python
import dask_ml.datasets
import dask_ml.cluster
import matplotlib.pyplot as plt
```

Generate random datasets for k-means clustering analysis.

```python
X, y = dask_ml.datasets.make_blobs(n_samples=10000000,
                                   chunks=1000000,
                                   random_state=0,
                                   centers=3,)
X = X.persist()
X
```

Group the clusters with the k-means algorithm.

```python
km = dask_ml.cluster.KMeans(n_clusters=3, init_max_iter=2, oversampling_factor=10)
km.fit(X)
```

<video width="100%" autoplay loop muted>
  <source src="../../../_static/videos/dask-compute-kmeans.mp4" type="video/mp4" />
  <p>Video showing dask dashboard while computing k-means clustering.</p>
</video>

<br>

Plot the results.

```python
fig, ax = plt.subplots()
ax.scatter(X[::10000, 0], X[::10000, 1], marker='.', c=km.labels_[::10000],
           cmap='viridis', alpha=0.25);
```

:::{image} media/dask-plot-result.png
:alt: Plot of the k-means clustering results.
:align: center
:width: 75%
:::

### Shut down the cluster

Shut down the cluster when in not in use to minimize the waste of computational resources and costs.

```python
cluster.close()
```

## FAQs

- *What are the best practices for using Dask to scale computations?*

  Take a look at the [Dask - Best Practices](https://docs.dask.org/en/latest/best-practices.html) documentation for a guide to using Dask efficiently.

- *Why can't I choose the instance type for my cluster?*

  The default is `n2-high-mem16` for Google Cloud and `r5.4xlarge` for AWS, with a maximum of 16 CPUs available on each machine. These instance types are chosen so that there is a consistent node pool across all 2i2c Dask hubs and more efficient cluster resourcing.

- *Should I use manual or adaptive scaling?*

  We suggest starting with adaptive scaling to dynamically scale up the number of workers when necessary but scale down and save resources when not actively computing. Once you are confident about your code's performance, you can use the manual scaling for fine-grained control over the number of workers needed.

- *How do I choose the number of workers/resources per worker?*

  Like any other scaling problem, the answer to this question is specific to the application code. As suggested in the [Dask - Besk Practices](https://docs.dask.org/en/latest/best-practices.html), start with a small subset of your data and evaluate performance using the Dask dashboard before scaling resources to the full dataset.

- *Why are there limited options for CPU and memory resources per worker?*

  The limited options of 1/2/4/8/16 CPUs and associated memory requests are chosen to enable the most efficient use of the node pool available. Otherwise, for example, a user could accidentally request 51% of a machine's resources per worker so only 1 worker can fit on an entire machine. In this example, if 2 workers were needed for the computation then this increases cloud costs for the 2 machines required while potentially leaving 49% of resources idle per machine.
  
- *Why did my kernel die?*

  There can be many reasons for this, but the most common one when it comes to Dask is an out-of-memory error caused by committing data into memory that exceeds the available RAM limit. Try using Dask to scale computations on smaller datasets and write the intermediate results to disk in the {ref}`/tmp folder<filesystem:tmp>`.

- *Which image should I use for the software environment?*

  There is no need to select which image to use on a 2i2c Dask hub – this choice is automatically made for you when you launch a server to ensure version consistency between the Dask user client and gateway server. If you need to add a few small packages to your environment that are not required by the Dask computations, then consider pip/conda installing them at the start of your session. This installation is temporary and you will need to do this each time you start new server on your hub. If you need extra software packages for all of your Dask workers, then they need to be available in the container specified in the cluster options. Contact [2i2c support](../../../support) in this instance.
