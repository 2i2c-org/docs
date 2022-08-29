# Use Git / GitHub

The recommended way to move code in and out of the hub is via git / GitHub.
You should clone your project repo from the terminal and use git pull / git push to update and push changes.
In order to push data to GitHub from the hub, you will need to set up GitHub authentication.
[gh-scoped-creds](https://github.com/yuvipanda/gh-scoped-creds/) should be already setup
on your 2i2c managed JupyterHub, and we shall use that to authenticate to GitHub for
push / pull access.

Open a terminal in JupyterHub, run `gh-scoped-creds` and follow the prompts.

Alternatively, in a notebook, run the following code and follow the prompts:

```
import gh_scoped_creds
%ghscopedcreds
```

You should now be able to push to GitHub from the hub! These credentials will expire after
8 hours (or whenever your JupyterHub server stops), and you'll have to repeat these steps
to fetch a fresh set of credentials. Once you authenticate, you'll be provided with a link
to a [GitHub App](https://docs.github.com/en/developers/apps/getting-started-with-apps/about-apps)
that you have to [install](https://docs.github.com/en/developers/apps/managing-github-apps/installing-github-apps)
on the repositories you want to be able to push to from this particular JupyterHub. You only
need to do this once per JupyterHub, and can revoke access any time. You can always provide
access to your own personal repositories, but might need approval from admins of GitHub
organizations if you want to push to repos in that organization.
