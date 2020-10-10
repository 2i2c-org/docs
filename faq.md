# Frequently Asked Questions

## Will my files and work persist between sessions?

Yes! Each user of a 2i2c Hub has their own filesystem that will persist between sessions.

## What guarantees do I have for this pilot?

We know it is really frustrating to rely on infrastructure that is undependable or often breaks. For this reason, we've designed 2i2c Hubs to be as fault-tolerant as possible. If things break, they should break for only one person rather than for an entire hub. If things must be changed, they should be changeable easily and quickly.

In addition, JupyterHub is designed to give you a degree of administrative control over what's going on inside. For example, you can [add your own users](add-users) and even help them debug their problem by [taking over their interactive session](access-server).

That said, this is a pilot being run with limited resources. You should not expect someone to respond to your questions and problems *immediately*. However, we'll do our best to get back to you quickly. Moreover, the 2i2c Hubs are not currently provided with a guarantee around site reliability (though we will informally tell you that they are generally very reliable).

## What happens if I want to move off of a 2i2c Hub?

2i2c Hubs are designed to use entirely open-source tools that work in other contexts. You can take your workflows elsewhere if you wish, and you can even deploy your own JupyterHub that recreates the same cloud-based experience. For more information, see [](migration-guide).

## Wait, you really want it to be easy for people to _leave_ 2i2c Hubs?

Yes! We are a non-profit organization with a mission to make open infrastructure for interactive computing more accessible for the research and education community. We believe that using tools that are interoperable, open-source, and owned by the community will most-benefit research and education and make it more equitable and inclusive. For this reason we are committed to deploying open source infrastructure that you can both take elsewhere or even deploy on your own.
