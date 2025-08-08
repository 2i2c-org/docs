# Move code in and out of the hub with GitHub

The recommended way to move code in and out of the hub is with [GitHub](https://github.com/about).

A typical pull request git workflow ([GitHub flow docs](https://docs.github.com/en/get-started/using-github/github-flow)) for collaborating on code consists of:

1. Pulling code from a remote repository on GitHub to a local repository on your hub
1. Creating a new branch from your local repository for working on your changes
1. Recording your changes with new commits to your branch
1. Pushing the branch with changes to the remote repository on GitHub
1. Repeating steps 3. and 4. until your work is ready to be reviewed 
1. Creating a pull request on the remote repository on GitHub for review.

:::{note}
Git clone using the HTTPS protocol and not SSH, since on the hub HTTPS will always work behind a firewall or proxy.
:::

When you pull and push code to the remote repository on GitHub, you will need to provide your GitHub credentials. 

:::{warning}
*We do not recommend entering your GitHub credentials (GitHub password, personal access tokens or otherwise) on any kind of shared infrastructure (e.g. private and public cloud, HPC, any remote machine)* as this information will be at risk.

We highly advise using `gh-scoped-creds` for authentication on our hubs.
:::

## Using `gh-scoped-creds`

Authorisation to pull and push to GitHub is handled with [`gh-scoped-creds`](https://github.com/yuvipanda/gh-scoped-creds/).

1. Open a Terminal.
1. Run the command `gh-scoped-creds`.
1. The following prompt will appear
   ```shell
   jovyan@jupyter-username:~/my-repo$ gh-scoped-creds
   You have 15 minutes to go to https://github.com/login/device and enter the code: XXXX-XXXX
   Waiting....
   ```
   Copy the code from the prompt and paste into [https://github.com/login/device](https://github.com/login/device) as instructed.
1. Authorise the hub to access GitHub by clicking the green button with the label *Authorize <name of hub>*.
   ```{note}
   You only need to do this once per JupyterHub, and can revoke access any time. You can always provide access to your own personal repositories, but might need approval from admins of GitHub organizations if you want to push to repos in that organization.
     ```     
1. [Install the hub's GitHub App](https://docs.github.com/en/developers/apps/managing-github-apps/installing-github-apps) to allow `gh-scoped-creds` for all or specific repositories you would like to push to that are owned by your GitHub account/organisation, and check that `Read and write access to code` option is enabled.
1. You should now be able to pull and push to GitHub from the hub without entering your credentials.

Authorisation will automatically expire after 8 hours (or when your JupyterHub server stops), and you'll have to repeat these steps
to renew.

:::{hint}
If you receive a `Permission denied` error after following these steps, then `gh-scoped-creds` has not been enabled for your hub. Please contact your hub administrator to request this feature.
:::

## Enabling `gh-scoped-creds` for your hub

There are some extra steps for Hub Administrators to enable `gh-scoped-creds` for their hub (requires GitHub organisation owner permissions).

1. Check that `gh-scoped-creds` is not already enabled for your hub by opening a Terminal and running
   ```shell
   jovyan@jupyter-username:~$ echo $GH_SCOPED_CREDS_CLIENT_ID
   ```
   
   If this returns nothing, then follow the next step. If this returns a client ID of the form `Iv1.xxxxxxxxxxxxxxxx`, then go to Step 3.
1. Send a ticket to the [2i2c support desk](https://docs.2i2c.org/support/) and log a feature request for `gh-scoped-creds`. 2i2c will create a GitHub App and update the hub configuration to make the `GH_SCOPED_CREDS_CLIENT_ID` and `GH_SCOPED_CREDS_APP_URL` environment variables available in your hub.
1. [Install the GitHub App](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party) to your GitHub organisation (requires GitHub organisation owner permissions).
   - Navigate to the GitHub App URL provided by 2i2c, which looks like `https://github.com/apps/<gh-app-name>`.
   - Click on the grey *Configure* button to install the GitHub app.
   - Select the GitHub organisation that you would like to enable `gh-scoped-creds` for
     ```{image} media/git-install-app-1.png
     :width: 50%
     :align: center
     :alt: Screenshot of the page to install a GitHub App showing how you can select the organisation to enable `gh-scoped-creds` for.
     ```
     ```{note}
     You only need to do this once per JupyterHub, and can revoke access any time. You can always provide access to your own personal repositories, but might need approval from admins of GitHub organizations if you want to push to repos in that organization.
     ```     
   - Choose whether to [install](https://docs.github.com/en/developers/apps/managing-github-apps/installing-github-apps) `gh-scoped-creds` for all repositories in your organisation or for only specific repositories, and check that `Read and write access to code` is enabled.
     ```{image} media/git-install-app-2.png
     :width: 50%
     :align: center
     :alt: Screenshot of the page to install a GitHub App showing where to select the repositories you want to install `gh-scoped-creds` for and check for which read-write permissions there are.
     ```
   - Click the green button labelled *Install*.
1. `gh-scoped-creds` is now enabled for your hub.

```{note}
If you wish to review the GitHub App settings, then you can locate your organization's installed apps at `https://github.com/organizations/<your-org-name>/settings/installations`.
```