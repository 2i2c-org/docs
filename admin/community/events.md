# Events

It is common to use your infrastructure as part of running a synchronous event. Based on experience, we've learned that there are multiple event patterns, which need different kinds of preparation & support, eg. workshops, courses/exams and conferences.

Here are some common best practices and policies to ensure that the event goes smoothly.

## Make sure you are familiar with the hub admin and user guides

Make sure you are familiar with the [Hub Admin guide](https://docs.2i2c.org/admin/) and potentially the [Hub User guide](https://docs.2i2c.org/user/), as they contain important information about how to use the hub, common best practices as well as the features available.

Reading the admin guide is also particularly useful to answering the questions in the next section. 

### Notify the 2i2c team about the event at least 3 weeks before an event

```{important}
As a general rule, please **notify the 2i2c team at least 3 weeks before an event** so that we can prepare accordingly.
```

To notify us, email `support@2i2c.org` with at least these pieces of information:

1. General info:
- Event type (workshop/course/exam/conference):
- Event start and end date:
- The active times for the event (e.g., 9am to 5pm US/Pacific):
- How many people will attend the event:
- Has a similar event (number of users and pattern) happened on the hub before (yes/no)?

2. Quotas:
- Should the current per-user usage quotas be increased for the event (if not explicitly requested, they default to 10GB)?
- Should the `shared` and `shared-public` quotas be increased?
- How much data you expect the users to be storing in their home directories (if known)?

3. If this is a shared password hub:
- What would you like the password to be for the event?
- When should we change the password?
- When should we change the password back?
- How long should user home directories be kept after the event?

4. Any other information that will help us prepare for the extra usage during the event:

```{note}
Once you've notified us, a 2i2c team member will create a GitHub issue for your event so that we can track when it is going to happen.
You should check the information in this issue and ensure that it is correct!
```

## Have the event content 'ready' at least one week before the event

Get your event content 'ready'. It doesn't need to be final, but make sure the large scale structural pieces are in place. Pay particular attention to:

1. Filesystem access (reading or writing data)
2. Size of the datasets you are reading (this affects memory usage and potentially disk usage)
3. Multiprocessing / CPU intensive work

Run through the workshop material on the hub, and make sure it works for the one user. Try to do this at a specific time when other users aren't on the hub, so we can more easily isolate what the effects of the test run is for metrics that are harder to isolate (such as disk throughput).

Communicate to 2i2c support the following information:

    The start time of the workshop material test run
    The end time of the workshop material test run
    The name of the user who did the test run
    How many total users you expect to be at your workshop

This lets us look at this dashboard, understand the total usage, and figure out if we need to make any tweaks.


##  Infrastructure testing and preparation for an event

Events provide a different pattern of usage for infrastructure compared with day to day use. Instead of a trickle of people coming on and off, events tend to trigger spikes in log-ins and activity. If many people start a session at the same time, this may slow down the start times of several users, because the cluster has to "scale up" to accommodate the extra people.

If an event follows a different usage pattern that your norm (many more people, more computing or data intensive work, users from different locations), we can help you plan ahead and test in advance. 

You typically won't need to "pre-initialize" the infrastructure to make start up easier for users at an event, but it can be useful in certain circumstances. This requests extra cloud resources in anticipation of a spike in user activity. It will speed up your user session start times, but will also increase your cloud costs.

It is most-useful if you anticipate large spikes in users all starting sessions at the same time.

We can recommend testing approaches and assess whether pre-initializing your infrastructure is necessary. If you need some extra advice, make sure to let the 2i2c team know when you notify us about the event (see the list above).
This will take additional attention from the 2i2c engineering team so is key to plan ahead by 3 or more weeks. 

## Before the event

Once a JupyterHub is set up for the community, try the following:

- **Define your hub's environment in a repository**. Follow the steps in [](#environment:image) to build a user image from that repository, and connect it with your hub.
   This ensures that your user environment is human-readable and reproducible.
- **Put content in a repository**. All of the materials for your workshop (e.g., Jupyter Notebooks, markdown files, etc) can be placed in a public repository.
- **Test your content and environment ahead of time**. You should run your content from top to bottom on your JupyterHub, or on a service like mybinder.org, to ensure that it works as expected.
   If you are using [nbgitpuller](#content:nbgitpuller), generate a link and click it yourself to make sure that it resolves properly.
- **Let the 2i2c team know that you're about to have an event**. We are likely already keeping track of when the event begins, but it is always a good idea to give a heads up so that the engineering team knows to expect an influx of users. Send an email to `support@2i2c.org` letting them know what to expect.
- **(optionally) Triage event participants with a sample workflow**. Many event organizers find it useful to ask potential participants to complete some basic exercises to make sure they have the right background. Create [a Binder link](https://mybinder.org) for your event's content (or for a subset of content you want people to try out) and ask them to complete it before the event begins.

## During the event

- **Use `nbgitpuller` to distribute content to attendees**. The [nbgitpuller tool](#content:nbgitpuller) to generate links that your hub's users can click, and automatically pull in content into their user session. Go to [nbgitpuller.readthedocs.io/en/latest/link.html](https://nbgitpuller.readthedocs.io/en/latest/link.html) to generate your own links.
- **Ask your users to log-in at the start of the day**. It can take a few moments for the JupyterHub to scale up when many users log in at once. For this reason, we recommend asking users to log into the hub **before they need to start running code**, in case it takes some time for the hub to begin.

## After the event

- **Send your attendees links to your source materials**. Because you've defined your user environment and content in a public repository, your attendees can see what software is needed to run the code on their own if they wish.
  In addition, your event repository is likely [a Binder-ready repository](https://mybinder.org) and attendees can build on top of your work and share via mybinder.org.
