# Sharing and reporting Grafana dashboards

Grafana dashboards can be shared with other community members and stakeholders so they can understand usage and cost patterns. Community Champions can

- export data to a CSV file
- generate a snapshot of the Grafana dashboard and share a public link
- or even [Programmatically access Prometheus data](prometheus-access.md) themselves.

## Generate a CSV file

1. Click on the three dots {material-regular}`more_vert`, in the top-right corner of the panel you wish to generate a CSV file for.
1. From the dropdown menu select *{octicon}`info` Inspect > Data*.
1. Click on the {bdg-primary}`Download CSV` button to download the data as a CSV file.

## Share a snapshot of the dashboard or panel

This function is available to Grafana admins only. A snapshot is a frozen view of data that can with others without the need to login with a Grafana account.

1. If you wish to share the *entire dashboard*, click on the {bdg-primary}`Share` button to the left of the time-range selector.
1. If you wish to share a *single panel*, click on the three dots {material-regular}`more_vert`, in the top-right corner of a panel. From the dropdown menu select *Share*.
1. From the pop-up *Share Panel* dialog, select the *Snapshot* tab and fill out the details.
1. Click the {bdg-primary}`Publish Snapshot` button to generate a public link that you can share with others.

:::{figure} images/cost-attribution-snapshot.png
:alt: Snapshot of the share panel dialog, with Snapshot name, Expire and Timeout fields.
:::
