# What is a typical hub start-up time that I should expect?

The time it takes for a user server to start, can be anywhere from a few seconds to 10min. It depends on some factors:

## The user server can fit on a node/machine that already exists and has enough resources available to serve it.
1. If it can't fit or such a node doesn't exits, then the autoscaler will trigger the creation of a new node.
  This can take up from a couple of minutes, to even 10 min or more. When the 10 minutes cap is hit, the server creation will throw a `TimeoutError` and you'll have to re-trigger the server creation process so you'll be assigned to the newly created node. Although not impossible, this is not common and we don't see it happing that often. In practice, we've noticed higher node startup times, with larger machines, like the ones with GPUs.

  The exact time it will take doesn't depend on 2i2c. Usually, it has to do with the cloud provider, machine type availability, etc.
1. If the node is already present and has enough resources, then the server creation will be much faster, taking only a few seconds.

## The user environment, i.e. the user image chosen from the profile options, is already present on the node.
1. If the image is not present, then it will first need to be pulled on the node.
  This can take a couple of minutes also, and is depending on the image size and network conditions.
  When a new node has to come up, image pulling will always happen and this will add to the overall time it takes for the server to be ready.

1. If the image is already present, then the server startup will be much faster, as it won't need to pull the image from the container registry.

```{important}
The startup time can be reduced though different strategies, like always having a minimum number of nodes available, pre-pulling images on nodes, etc. But this will increase costs, so it's a trade-off that needs to be evaluated on a per-hub basis. More about balancing these trade-offs can be found in [](community-lead:billing:responsiveness).
```