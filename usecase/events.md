# Events and workshops

These are some best-practices for running event-based workshops with a 2i2c JupyterHub.

## Before the event

Once a JupyterHub is set up for the community, try the following:

- **Define your hub's environment in a repository**. Follow the steps in [](environment:image) to build a user image from that repository, and connect it with your hub.
   This ensures that your user environment is human-readable and reproducible.
- **Put content in a repository**. All of the materials for your workshop (e.g., Jupyter Notebooks, markdown files, etc) can be placed in a public repository.
- **Test your content and environment ahead of time**. You should run your content from top to bottom on your JupyterHub, or on a service like mybinder.org, to ensure that it works as expected.
   If you are using [nbgitpuller](content:nbgitpuller), generate a link and click it yourself to make sure that it resolves properly.
- **Let the 2i2c team know that you're about to have an event**. We are likely already keeping track of when the event begins, but it is always a good idea to give a heads up so that the engineering team knows to expect an influx of users. Send an email to `support@2i2c.org` letting them know what to expect.
- **(optionally) Triage event participants with a sample workflow**. Many event organizers find it useful to ask potential participants to complete some basic exercises to make sure they have the right background. Create [a Binder link](https://mybinder.org) for your event's content (or for a subset of content you want people to try out) and ask them to complete it before the event begins.

## During the event

- **Use `nbgitpuller` to distribute content to attendees**. The [nbgitpuller tool](content:nbgitpuller) to generate links that your hub's users can click, and automatically pull in content into their user session. Go to [nbgitpuller.link](http://nbgitpuller.link) to generate your own links.
- **Ask your users to log-in at the start of the day**. It can take a few moments for the JupyterHub to scale up when many users log in at once. For this reason, we recommend asking users to log into the hub **before they need to start running code**, in case it takes some time for the hub to begin.

## After the event

- **Send your attendees links to your source materials**. Because you've defined your user environment and content in a public repository, your attendees can see what software is needed to run the code on their own if they wish.
  In addition, your event repository is likely [a Binder-ready repository](https://mybinder.org) and attendees can build on top of your work and share via mybinder.org.
