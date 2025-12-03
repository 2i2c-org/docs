# Custom alerting for your community

Grafana can be used to create *custom alerts* that are specific to your
community to fit into specific workflows you may have. [Grafana Alerting](https://grafana.com/docs/grafana/latest/alerting/)
is very powerful, and upstream grafana has reasonably good documentation on
its various features. This document lists some of the common things you
can do with it, as well as some popular alerts our communities have found
helpful.

## Why?

As admins of a JupyterHub, you may want to be proactively notified when
certain conditions are met so you may intervene with your users. For example,
you may want to know when users are nearing their home directory limit so
you can reach out to them to ask if they need help or to encourage them to
clean up their home directory.

```{note}
2i2c has our own internal alerting system for the underlying infrastructure
we maintain, and we will take action on those ourselves when necessary. These
alerts are entirely distinct from that.
```

## Where can alerts be sent?

Grafana supports sending alerts to [many kinds of *contact points*](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/manage-contact-points/#supported-contact-point-integrations). In this document,
we will use Slack as the example as many of our communities use it. You should
be able to follow upstream Grafana documentation to set up alerting to (almost)
any kind of contact point you may already be using and that fits within your
existing workflows.

```{note}
The one exception to this is the "Email" contact point. Sending email reliably
is unfortunately pretty complicated and our grafana installations do not support
it.
```

## Setting up sample alerts

### 1. Create credentials for Grafana to post to Slack

```{note}
See [grafana's documentation](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/manage-contact-points/#supported-contact-point-integrations)
to connect with a different alerting mechanism instead
```

This is a simplified version of [Grafana's docs](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/manage-contact-points/integrations/configure-slack/)
on connecting with slack. If something here is unclear, consider referring to
their documentation.

Grafana can connect to Slack via an API token or via a webhook URL. For our use
cases, the webhook URL is a better fit so this document guides you through that
process. You will only need to do this once.

1. Login to your slack on your browser.
2. Create a slack channel where alerts will be posted. We suggest a dedicated channel for alerts that is private (as alerts can potentially contain personally identifiable information) and has all the hub admins added. You can re-use an existing channel that is dedicated to alerts if you have one. We strongly recommend against sending alerts to a channel that's used for general discussions.
3. Go to [https://api.slack.com/apps?new_app=1](https://api.slack.com/apps?new_app=1) to create a new "App"
4. Select "From Scratch" in the popup that shows up.
5. Enter "Grafana Community Alerts (2i2c Hub)" (or a similarly descriptive name) under `App Name`. This will be the name of the bot that posts the alerts.
6. Select the slack workspace that should get notifications.
7. Click "Create App" button. This creates a new slack app and redirects you to the configuration page for the new app.
8. On the left sidebar, select "Incoming Webhooks" under "Features". This opens a page that allows you to create a new webhook URL.
9. Toggle the switch from "Off" to "On" position on the top right.
10. Click the "Add New Webhook" button.
11. Select the workspace and channel (created in step 2) where alerts should be posted to.
12. Click the "Allow" button.
13. Copy the webhook URL.

## 2. Connect Grafana to Slack

1. Log-in to your community's Grafana instance with an admin account.
2. In the left panel, select "Alerting" -> "Contact points"

    ```{tip}
    If you don't see this option, it is possible you aren't using an admin
    account! Grafana admin accounts use a username and password you set via
    an invite link. Ask another admin in your community who *does* have
    an admin account [to make you one](https://infrastructure.2i2c.org/sre-guide/support/grafana-account/) or
    reach out to 2i2c support.
    ```

3. Click "Create contact point".
4. Select "Slack" under the "Integration" dropdown.
5. Enter a descriptive name for this contact point under "Name" (such as `2i2c-hub-alerts`).
6. Paste the webhook URL you copied in the previous section under "Webhook URL".
7. Press the "Test" button and validate that you are able to see a message in the appropriate slack channel.
8. Click "Save Contact Point".