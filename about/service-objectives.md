# Service Level Objectives and Principles

This page describes the **Service Level Objectives** (SLOs) of 2i2c's infrastructure services[^slos].
These describe our goals in running infrastructure for the communities that we serve.
They indicate what our users can expect when using the infrastructure we support.

We design our infrastructure, and consistently hone our practices, to meet these objectives.
They evolve over time as we get feedback from communities we serve, and learn more about how to best deliver impact via our services.

:::{note}
2i2c does not currently have a **Service Level Agreement** (SLAs), as this is generally a legally-binding document that involves calculation of risk via revenue lost during service outages.
We currently do not have the capacity to design and litigate strict SLAs, and believe that we will have the most impact by instead committing to service **objectives** that are transparent and follow best practices.[^zenodo]

We may revisit this in the future depending on the feedback we get from other communities!
:::

## High availability

The infrastructure that 2i2c runs should be available to its communities 24/7, and with minimal human intervention needed to maintain this level of performance.
We invest in continous development to improve the resiliency and efficiency of the infrastructure that we run, following best-practices in service design and engineering in the cloud.

:::{admonition} To be refined...
It is a known anti-pattern to define an ambiguous SLO like "24/7".
Truly meeting such an objective is nearly impossible and extremely costly.
In the future, we plan to run an audit of our infrastructure and practices, and design quantifiable uptime targets for our SLOs.
:::

## Balance speed and cost

There is an inherent tension between doing things quickly (which generally requires using extra resources to encourage speed) and cost efficiency (because you pay for those extra resources).
This is particularly relevant during **scaling events**.
These are moments when the infrastructure has enough usage that it must grow the cloud resources available to handle the new load.

2i2c strives to build infrastructure that strikes a balance that depends on the particular use-case.
If infrastructure requires steady, but semi-random usage, we should prioritize cost efficiency.
If infrastructure will have known spikes of activity at the same time, we may temporarily favor speed over cost by asking for extra resources from the cloud provider.

:::{note}
If your community requires a change in the infrastructure that occurs over a weekend, we will generally try to do this on the Friday beforehand, rather than over the weekend, even if this means it will cost marginally more in cloud infrastructure.
If we anticipate the cost to be significant, we will discuss with you ahead of time.
:::

## Support responsiveness

We have a dedicated communications channel for support at `support@2i2c.org`, and somebody on the engineering team is always tasked with monitoring this channel.

When questions come in on the support channel, we triage them based on whether they cover a major problem for the community (e.g., if there is a major hub outage).

If this is the case, we strive to respond as quickly as possible to mobilize the right team members and fix the problem.
We will communicate with the Community Representative throughout this process, and let them know when the problem has been resolved.
In general, we aim to respond to all support questions within 24 hours - though we strive for more quick responses if the issue is critical.

## Intentional downtime

In some cases there may be intentional downtime for the infrastructure that we run.
For example, if we need to undergo major maintenance of infrastructure transitions, it may necessitate bringing down the infrastructure for a few hours.

In these cases, we will communicate with the Community Representative ahead of time, to inform them of our intentions and give an opportunity for them to tell us when this will be least disruptive.
We will then carry out our maintenance as quickly as possible, with minimal downtime, and notify the community representative(s) when this has been complete. 

## Holidays, weekends, and expected downtime

Expected downtime are periods of time when there is generally less availability from the team (as well as from the communities we serve).
This includes weekends and heavy holiday periods like the end of the year.

While we strive for our services to be available 24/7, we also believe in the importance of protecting weekends and holiday time for our team.
During expected downtime periods, you should expect reduced responsiveness in our support channels, and no promises about our ability to respond to questions or issues with your infrastructure.
We may agree to perform some of these operations during expected downtime, but this should be the exception, not the rule.

If this is disruptive to your community's activies, please reach out and we can discuss.
However, we encourage you to avoid planning mission-critical events or actions during periods of expected downtime.

[^slos]: For more about the difference between Service Level Objectives, Agreements, and Indicators, see [the Google SRE handbook](https://sre.google/sre-book/service-level-objectives/).

[^zenodo]: This practice is inspired by [Zenodo's intentional lack of Service Level Agreements](https://about.zenodo.org/principles/).