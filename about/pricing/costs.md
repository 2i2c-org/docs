# Our cost breakdown

This page is a short description of the basic costs that go into the fees that our communities pay to sustain this service.

There are two major factors that go into the cost of 2i2c's services: **human costs** and **cloud costs**. We consider these costs separately below.

(costs:human)=
## Human costs

Our biggest cost is paying salaries for team members that carry out the services we provide.
This includes cloud operations and development, open source support, guidance and support for our communities, etc.

:::{seealso}
You can find more about our compensation philosophy in our [compensation and benefits page](https://team-compass.2i2c.org/en/latest/hr/compensation.html).
:::

At present, we choose monthly hub fees based on assumptions about _how many hubs an engineer can operate and support_.
We assume this is the primary bottleneck that limits our capacity.
This gives us an "engineering cost per hub" and we use this as a base to estimate the extra fees we need to charge to cover the non-engineering roles that are needed for the service.

- **Cost of a 2i2c engineer**. If we assume that a 2i2c engineer is paid `$140,000/year`, with a `30%` benefits markup. This covers the design, development, and ongoing operation of cloud infrastructure for 2i2c's hubs.
- **Community support fees**. We add a `10%` markup to cover 2i2c's extra costs in providing ongoing support and community guidance for our hubs. This includes communications and guidance for community representatives as well as support for hub issues.
- **Open source support fees**. We add a `10%` markup to cover 2i2c's extra costs in ongoing open source engagement and support. This includes upstreaming contributions to open source projects, community engagement and leadership, and collaboration and planning.
- **Fiscal sponsor fees**. We add a `15%` markup to cover the fee of our fiscal sponsor, [Code for Science and Society](https://codeforscience.org/) (for see [](tc:structure:fiscal-sponsor) for information about the services that CS&S provides).

The result is roughly `$250,000` annually for each engineering position.
The fees for each hub are thus determined by dividing this annual cost by the estimated number of hubs of a given type that we can realistically support.

## Cloud costs

We pass through cloud costs directly to our communities in a transparent manner.
This encourages us to continually reduce the cloud costs for our communities, and helps them understand how their decisions affect their cloud bill.

### What components make up my cloud bill

There are a few kinds of infrastructure that make up your cloud bill.
Here is a short summary:

- **Nodes for user sessions**: A "node" is kind-of like a virtual machine or a dedicated computer. It is reserved cloud infrastructure that you can use as you wish. Nodes have resources allocated to them (e.g., `100GB` of RAM). JupyterHub uses dedicated nodes for user sessions, so more users == more nodes. You generally pay cloud providers by the minute for each node used. 
- **Storage costs**: In order for users to persist their work over time, we must pay for filesystem storage. This is used to store user notebooks and content, data, etc. You generally pay cloud providers by the `GB` over time.
- **Nodes for hub infrastructure**: In addition to the cloud nodes for user sessions, there are also nodes to run the JupyterHub and supporting infrastructure to manage user log-ins, do monitoring and reporting of activity, etc.
- **Nodes for specialized computing**: For hubs that have scalable computing resources like a Dask Gateway, these generally request special nodes _on the fly_. When a scalable computation is executed, the cloud quickly requests many new nodes to complete the computation, and then removes them when it is done. You pay for the time used for each node during this computation.

There are some other components that go into your cloud bill (e.g., "networking costs") but these are the major pieces.

### User actions that impact cloud costs

Cloud costs depend on a few key factors that you and your community has control over.
Here we list some major considerations (in decreasing order of importance):

- **Base user resources needed**: The power and complexity of the user environment is the biggest driver of "base cost per user". This is largely driven by the amount of memory (RAM) each user needs. See below for a more in-depth explanation.
- **Community usage over time**: Resources are requested from the cloud "on-demand", meaning that your cloud costs will scale up and down with number of active users at any given moment.
- **User storage over time**: User storage is different from on-demand resources, because it's "always being used" even when you're not logged-in. We recommend storing large datasets and such in cloud object storage, which is much cheaper.
- **Dedicated vs. shared infrastructure**: If your community requires their own dedicated cloud infrastructure (for example, a dedicated Kubernetes cluster) then this will boost your cloud costs because you will not be sharing this cost with other communities.
- **Cloud optimizations**: There are many ways to make cloud infrastructure more efficient and scalable, and the 2i2c engineering team is constantly experimenting with ways to lower costs for communities. For many non-2i2c hubs, inefficiency is a large source of cloud cost, though the 2i2c hubs are already well-optimized.

### Estimate my cloud costs

The following is a very rough guideline to follow in order to understand and estimate what your cloud costs might be.
These are similar whether you're using 2i2c to manage your hub, or running it yourself.

Generally speaking, **the biggest technical driver of cloud costs is user memory (RAM)**.
This is because RAM must be "reserved" on a node, and each node has a finite amount of memory available to it.

Let's say a user node costs `$100.00` an hour, and comes with `100GB` total RAM.
If each user is guaranteed `1GB` of RAM, then the node can theoretically fit `100` users at a time.
`100` simultaneous users will cost `$100.00` an hour, or roughly `$1 / user / hour`.

If we double the guaranteed RAM available to users, then the node can now fit `50` users at once (`100 GB / 2 GB per user = 50 users total`).
We now need twice the number of nodes to handle the same number of users.
`100` simultaneous users will now cost `$200.00` an hour, or roughly `$2 / user / hour`.

In practice, the cost per node depends heavily on the cloud provider, and is constantly in-flux.
**To estimate your own cloud costs**, follow these steps:

1. **Estimate memory available to each user**. The amount of RAM needed for each user is often the biggest driver of cloud cost. Decide the "maximum" amount of RAM that a user % will generally need, and multiply that by 1.5x.
2. **Determine how many average simultaneous users you'd like a hub to support**. This isn't necessarily the total size of your community, but how many people you think will be % using the hub *at the same time*.
3. **Look up the monthly price for an `n1-highmem-4` node**. This is a basic node type that serves most use-cases and can be used as a benchmark for comparison.
   1. [Go to the Google Cloud pricing page](https://cloud.google.com/compute/vm-instance-pricing). This lists prices for many kinds of nodes with Google Cloud Platform.
   2. Go to the `N1 high-memory machine types` section. This contains prices for all `N1` node types with high memory.
   3. Look at the hourly price for `n1-highmem-4`.
   4. Divide this amount by `n_simultaneous_users_per_hour * GB_per_user`.
   5. This is your estimated extra cost per hour per user.
4. **Estimate storage costs**. Estimate your storage costs based on the expected storage each user will take up. 2i2c's hubs use a standard NFS File Storage for most hubs, which has very fast latency for interactive computing. [Here are Google's file storage prices](https://cloud.google.com/storage/pricing#price-tables), for example. You can estimate these costs based on the expected storage used across all of your users.  

:::{seealso}
We recommend checking out the following resources to learn more about cloud costs.
None of these are guarantees about costs, but should give you a general idea.

- For general information and explanation, see [the Zero to JupyterHub cost projection documentation](z2jh:cost).
- For educational or "lightweight resources" hubs, see [this rough cost analysis notebook from the UC Berkeley DataHub](https://nbviewer.jupyter.org/github/berkeley-dsep-infra/datahub-usage-analysis/blob/master/notebooks/03-visualize-cost-and-usage.ipynb).
- For data- and compute-intensive hubs, see the Pangeo two-part series on their Kubernetes costs. ([part 1 link](https://medium.com/pangeo/pangeo-cloud-costs-part1-f89842da411d), [part 2 link](https://medium.com/pangeo/pangeo-cloud-cluster-design-9d58a1bf1ad3))
:::

### How we estimate cloud costs for communities

The previous sections give a high-level overview of how to think about cloud costs and how they'll reflect your community's usage.
This section describes how the 2i2c team calculates cloud costs and passes this on to communities.

Over time, we will refine this process to make it more precise and (as much as possible) directly tied to the usage a community incurs.

#### Shared kubernetes clusters

For hubs that run on **shared Kubernetes clusters**, we estimate their cloud costs via the following process:

1. Calculate the monthly cloud bill for this cluster.
2. Calculate the % usage for a specific community, based on the % of RAM requested throughout the month.
3. Estimate a community's cloud costs for that month by calculating `(monthly_cloud_bill_for_cluster * %_usage_for_this_community)`.

#### Dedicated kubernetes clusters

For hubs that run on a **dedicated Kubernetes cluster**, a cloud bill will be generated by the cloud provider, 2i2c will pay it in advance, and we will include this cost in the next month's invoice.
This will exactly reflect the cloud charges incurred by the hub in that time.
