# The 2i2c status page

```{warning}
Both the status page and the information in this section is a work in progress and subject to change.
```

2i2c has a status page provided by [Pagerduty](https://www.pagerduty.com/), the platform we use to track our automatic alerts.
It is currently running at https://2i2c-hubs.trust.pagerduty.com

```{figure} /images/status-page-pagerduty.png
```

The status page can currently track automatic outages related to three main services:

- **the Hub**
  this will trigger when the Hub URL is unavailable
- **the User Server**
  this will trigger when a user server can't start because of a system problem we're investigating
- **the Storage**

Read more about outages at [](outages).

## Subscribing

You can subscribe to the status page so that you are automatically informed about any outages that happen across _all_ hubs that 2i2c manages and all maintenance work we are planning so that you can plan your work accordingly.

```{figure} /images/subscribe-to0status-page.png
```