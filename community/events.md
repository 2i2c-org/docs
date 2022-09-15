# Events and workshops

It is common to use your infrastructure as part of running a synchronous event.
For example, with a hackathon or as part of a conference workshop.
Here are some best practices and policies to follow in order to ensure that the event goes smoothly.

## Notify the 2i2c team about the event

As a general rule, please **notify the 2i2c team at least 3 weeks before an event** so that we can prepare accordingly.
To do so, email `support@2i2c.org` with at least these pieces of information:

- Start date for the event
- End date for the event
- The active times for the event (e.g., 9am to 5pm US/Pacific)
- How many people will attend the event
- Do you need to need hub infrastructure to be [pre-initialized before the event](events:pre-initialized)?
- Any other information that will help us prepare for the extra usage during the event.

Once you've notified us, a 2i2c team member will create a GitHub issue for your event so that we can track when it is going to happen.
You should check the information in this issue and ensure that it is correct!

(events:pre-initialized)=
## Infrastructure preparation for an event

Events provide a different pattern of usage for infrastructure compared with day to day use.
Instead of a trickle of people coming on and off, events tend to trigger spikes in log-ins and activity.
If many people start a session at the same time, this may slow down the start times of several users, because the cluster has to "scale up" to accommodate the extra people.

If you wish, it is possible to "pre-initialize" the infrastructure for an event.
This requests extra cloud resources in anticipation of a spike in user activity.
It will speed up your user session start times, but will also increase your cloud costs.
It is most-useful if you anticipate large spikes in users all starting sessions at the same time.

If you wish to pre-initialize your infrastructure before an event, make sure to let the 2i2c team know when you notify us about the event (see the list above).
This will take extra attention from the 2i2c engineering team.

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
