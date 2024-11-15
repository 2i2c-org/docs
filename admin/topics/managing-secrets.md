(managing-secrets)=
# Secrets, passwords and access tokens

You may require access to secrets, passwords and access tokens for managing your hub in a local development environment, or during deployment using GitHub actions or Read the Docs. This section documents the recommended workflows for each of these cases.

## Access a secret locally in a .env file

Access your secret as an environment variable in a local development environment by storing it in a `.env` file. A `.env` file is a popular language-agnostic solution for secrets management and can be parsed with the `python-dotenv` package.

:::{caution}
Keep your secret secure and do not upload the `.env` file to a Git repo. Add `.env` to your `.gitignore` list.
:::

1. Create a new `.env` file in the root folder of your project.
1. Edit the `.env` file to include

   ```bash
   SECRET_NAME=<enter your secret here>
   ```

1. Save and close.

Access your secret in a Python code with

```python
pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()
SECRET_NAME = os.environ["SECRET_NAME"]
```

### Access organization-level secrets in GitHub actions

Add your secret as a GitHub an organizational-level repository secret to be used in GitHub actions.

:::{note}
To create a secret for the GitHub organization for multiple users, see the [GitHub Docs – Using secrets in GitHub actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-an-organization). We recommend organization-level secrets against individual-level secrets to minimize the need to create duplicate secrets for multiple repositories.
:::

1. Navigate to the GitHub organization.
1. In the *{octicon}`gear` Settings* menu, click on *{octicon}`key-asterisk` Secrets and Tokens > Actions* in the left-side menu. 
1. Under the *Organization Secrets* section, click on the {guilabel}`New organization secret` button.
1. Enter the name of your secret in the *Name* field and paste in the value of your secret in the *Secret* field.
1. Scope the secret to the relevant select repositories under the *Repository access* dropdown.
1. Click {guilabel}`Add secret` to confirm.

Following this, adjust your GitHub action workflow file to make the secret available to your job with the `env` key value. See the [GitHub Docs – Using secrets in GitHub actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#using-secrets-in-a-workflow) for a full guide. Here is an example snippet of a GitHub secret configuration below:

```yaml
jobs:
  test-docs:
    steps:
      - name: make dirhtml
        env:
          SECRET_NAME: ${{ secrets.SECRET_NAME }}
        run: |
          make my_project
```

:::{caution}
Repository secrets are not passed to workflows that are triggered by a pull request from a forked repository.
:::

### Access the secret on Read the Docs

If you deploy documentation using Read the Docs, ensure that the secret is available as an environment variable in the Read the Docs build environment:

1. Navigate to [Read the Docs](https://readthedocs.org) and log into your account.
1. Click on the name of the project you wish to enable the secret for.
1. Click the *{octicon}`gear` Admin* button.
1. Click the *Environment Variables* section in the left sidebar and then click on {guilabel}`Add Environment Variable`.
1. Enter the secret name into the *Name* field and paste in your secret value into the *Value* field.
1. **Important:** leave the box *Expose this environment variable in PR builds?* unchecked to keep your token secret.
1. Confirm by clicking {guilabel}`Save`.

:::{caution}
Custom environment variables not marked as public are not available in pull request builds. See the [readthedocs docs – Environment variables and build process](https://docs.readthedocs.io/en/stable/environment-variables.html).
:::
