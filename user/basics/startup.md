(user:faq:startup-time)=
# What is a typical hub start-up time?

User server startup time ranges from **a few seconds** to **10 minutes**, depending on two main factors:

## Factor 1: Resources available on a node

When a server starts, it requests resources from a node.

**If a node already exists with sufficient resources:**
- Server creation takes only a few seconds

**If a suitable node doesn't exist or lacks resources:**
- The autoscaler creates a new node, which takes 2 to 10+ minutes
- Node creation time depends on the cloud provider and machine type (larger machines like GPUs often take longer)
- If startup exceeds 10 minutes, you'll see a `TimeoutError` and need to restart your server to use the newly created node
- This timeout is uncommon but can occur with certain machine types


## Factor 2: Environment image availability

When a user server starts, JupyterHub then finds and loads the **environment image**, which contains all the tools available to the user.

**If the image is already on the node:**
- Server startup is much faster since no download is needed

**If the environment image isn't on the node:**
- The image must be pulled from the container registry
- This takes a few minutes depending on image size and network conditions
- Image pulling always happens if a new node was just created


```{important}
Startup time can be reduced through strategies like maintaining minimum node counts or pre-pulling images, but these increase costs. Learn more about balancing responsiveness and cost in [](community-lead:billing:responsiveness).
```