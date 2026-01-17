# Custom alerting for your community

Grafana can be used to create *custom alerts* that are specific to your
community to fit into specific workflows you may have. [Grafana Alerting](https://grafana.com/docs/grafana/latest/alerting/)
is very powerful, and upstream grafana has reasonably good documentation on
its various features. This document lists one of the most common things our
communities have been using it for (home directory alerts), and eventually
we hope to add other examples.

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
it, even though it is listed in the UI.
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

### 2. Connect Grafana to Slack

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

### 3. Create a new dashboard folder

The default JupyterHub dashboards, available under the "JupyterHub Default Dashboards" folder
in your grafana, is managed automatically via the upstream [jupyterhub grafana dashboards](https://github.com/jupyterhub/grafana-dashboards)
project. So we can't make manual changes or alerts in there, as updates to the
upstream dashboards may overwrite them.

So we will make a new folder and create new alerts inside it. You can also put
custom dashboards into this in the future, and those will not be affected when
we update the default dashboards.  Different communities will have different
needs, and can maintain their dashboards / alerts as they wish! We'll provide some
guidance for common alerts and dashboards in this page, but customize it as you
see fit.

1. Select "Dashboards" on the left sidebar
2. Click "New" on the top right
3. Select "New folder" in the dropdown
4. Name the folder "Community Maintained Dashboards" and click the "Create" button.
   This creates a new folder within which you can create dashboards as you need.

### 4. Create your first alert

Let's create our first alert! As an example, we'll create an alert
for when any user is over 80% of their total usage quota.

```{note}
[PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/)
is a query language used for looking at time series metrics, performing
efficient calculations on them and querying them for visualization with
Grafana. You'll need to learn *some* promql to be able to fully use the
Grafana features for visualizations, but you can get along far by copy
pasting some and tweaking them.
```

1. Select "Alerting -> Alert Rules" in the left sidebar.
2. Click the "New alert rule" button on the top right
3. Enter a descriptive name for this rule, like "Users approaching home directory limit"
4. Under "Define query and alert condition", you'll have a space to
   enter a PromQl query. If you don't see such a space, you may have to toggle the
   switch on the right from "Builder" to "Code".
   You can play with different promql queries here, but for our use case,
   use `max(dirsize_total_size_bytes) by (directory) / max(dirsize_hard_limit_bytes) by (directory)`.

   This query calculates the % of home directory size for each user of the
   total limit available to them, as a fraction between 0 and 1.

   You can press the "Run Queries" button to preview the data
   that comes from running this query. You'll see one entry
   for each user, with the value being the % of their limits they
   have used so far.
5. Under "Alert condition", specify "0.8" for the text box so it
   reads "When query is above 0.8". Press the "Preview alert rule
   condition" button to see what users this alert would fire for.
   Adjust the % at which you'd like alerts by changing this value
   from 0.8 to whatever feels convenient for your community.
6. Under "Add folder and labels", select the folder we created
   earlier ("Community Maintained Dashboards") so we can keep
   our alerts organized.
7. Under "Set evaluation behavior", select "New evaluation group".
   Give it the name "default", and hit "Create". You'll only
   have to do this once - for future alerts, you can simply select
   this group from the dropdown. This tells grafana to evaluate
   the rule every minute and alert if it sees issues.
8. Under "Configure notifications", select the slack contact point
   you created in the earlier step.
9. Expand the "Muting, grouping and timings (optional)" section and toggle
   "Override grouping" to be on. By default, Grafana will generate *one* alert
   for *all* users that are over the limit. This is unwieldy,
   and we want one alert per user.

   To do so, add `directory` as another item to the dropdown
   describing various things each alert will be grouped by. We
   add `directory` because the Prometheus metric uses `directory`
   to refer to each user's home directory, and you can see
   it in the preview of the alert if you scroll up.

10. Click "Save".

That's it, you have a new alert set up! It should fire for users
who are close to their limit in a minute, and post messages
to the slack channel!

## Further documentation

Grafana's alerting system is fairly powerful and extensive, and
reasonably [well documented](https://grafana.com/docs/grafana/latest/alerting/)
upstream.