(hub-user-image-template-guide/how-to)=
# Create a custom user image for your hub (advanced)

This advanced guide describes how you can create a custom user image for your community's hub. We recommend [updating a community-maintained upstream image](./update-community-image.md) in the first instance, since this reduces the overall maintenance burden over time. This guide is for advanced users who want complete control over a hub's user image from scratch. It uses [this `hub-user-image-template` repository](https://github.com/2i2c-org/hub-user-image-template) to help you get started.

## 1. Use the template repository

Create a new repository for your user image from the [`hub-user-image-template`](https://github.com/2i2c-org/hub-user-image-template) repository.

1. Go to the [`hub-user-image-template`](https://github.com/2i2c-org/hub-user-image-template) repository.
2. Click the {guilabel}`Use this template` button located at the top of this repository's GitHub page.

   ```{figure} ../../../images/use-template.png
   :alt: Use this template
   ```
3. This will generate a **copy** of the repository that you can modify as you wish.

## 2. Connect the new repository to [quay.io](https://quay.io/)

The image repository is bundled with a GitHub Action that will build a Docker Image from the configuration you've defined in the repository.
To use this image, you'll need to connect the repository to an **Image Registry** where we will push images.
We'll use the [repo2docker-action docs](https://github.com/jupyterhub/repo2docker-action) to guide us.

1. Go to the [repo2docker-action guide's section on pushing to `quay.io`](https://github.com/jupyterhub/repo2docker-action#push-repo2docker-image-to-quayio).
2. Follow all the instructions (except the last step).

When you have completed these steps, you should have:

- A quay.io repository of the form `quay.io/<quay-username>/<repository-name>`
- You should have two secrets set on your newly-created GitHub repository:
  - **`QUAY_USERNAME`**: the user name of the `quay.io` robot account
  - **`QUAY_PASSWORD`**: the password of the `quay.io` robot account

  ```{figure} ../../../images/secrets.png
  :alt: Secrets
  ```

## 3. Enable image pushes to quay.io

Step 2 should have provided the appropriate credentials to push the image to quay.io via GitHub Actions.
This template repository provides a GitHub Actions workflow that is configured to use these credentials to build and push the image to quay.io, but it needs additional configuration. 
Below are the steps to configure each option.

### Enable quay.io image push for [build.yaml](https://github.com/2i2c-org/hub-user-image-template/blob/main/.github/workflows/build.yaml)

The [build.yaml](https://github.com/2i2c-org/hub-user-image-template/blob/main/.github/workflows/build.yaml) workflow builds the container image and pushes it to quay.io **if** credentials and image name are properly set.
This happens on every pushed commit on the main branch of the repo (including when a PR is merged).
The image is also built for every commit pushed to a Pull Request, but **is not pushed to quay.io by default**.

To enable pushing to the appropriate quay.io repository, edit line 47 of [build.yaml](https://github.com/2i2c-org/hub-user-image-template/blob/main/.github/workflows/build.yaml#L46-L47) and:

1. Uncomment the `IMAGE_NAME` option
2. Replace `<quay-username>/<repository-name>` with the info of the `quay.io` repository created at step 2
3. Commit the changes you've made to `build.yaml`

```{figure} ../../../images/image-name-in-build-workflow.png
:alt: IMAGE_NAME
```

You can checkout the logs of this GitHub Workflow via the Github Actions tab on your image repository.

```{figure} ../../../images/build-workflow.png
:alt: Build workflow
```

If you are triggering this action by merging a PR or directly pushing to the main branch, you should look at the Github Actions tab and this will show a `pushing quay.io/...` message, followed by the image name and tag like in the image below.

```{figure} ../../../images/pushing-to-registry-job-step.png
:alt: Build logs
```

### Enable quay.io image **push** during Pull Requests

The [build.yaml](https://github.com/2i2c-org/hub-user-image-template/blob/main/.github/workflows/build.yaml) workflow builds the container image on pull requests.
It can also push it to quay.io **if** the [`NO_PUSH`](https://github.com/jupyterhub/repo2docker-action#optional-inputs) input is removed.

To enable pushing to the appropriate quay.io repository, edit line 33 of [build.yaml](https://github.com/2i2c-org/hub-user-image-template/blob/main/.github/workflows/build.yaml#L32-L33) and comment out or remove the `NO_PUSH` input.

:::{tip}
The [Optional Inputs](https://github.com/jupyterhub/repo2docker-action#optional-inputs) section in the [jupyterhub/repo2docker-action](https://github.com/jupyterhub/repo2docker-action) docs provides more details about the `NO_PUSH` option, alongside additional inputs that can also be passed to the repo2docker-action.
:::

If configured correctly, you will see a `pushing quay.io/...` message in the GitHub Actions logs when you have committed directly to main/merged a PR **and** pushed a commit to a PR.

## 4. Customize the image

Modify [the environment.yml](https://github.com/2i2c-org/hub-user-image-template/blob/main/environment.yml) file and add all the packages you want installed in the conda environment.
Note that repo2docker already installs [this list](https://github.com/jupyterhub/repo2docker/blob/HEAD/repo2docker/buildpacks/conda/environment.yml) of packages.
More about what you can do with `environment.yml`, can be found in the [repo2docker docs](https://repo2docker.readthedocs.io/en/latest/configuration/research/).

1. Commit the changes made to `environment.yml`.
2. Create a Pull Request with this commit, or push it directly to the `main` branch.
3. If you merge the PR above or directly push the commit to the `main` branch, the GitHub Action will automatically build and push the container image. Wait for this action to finish.

## 5. Build and push the image

Images generated by this action are automatically tagged with both `latest` and `<SHA>` corresponding to the relevant commit SHA on GitHub.
Both tags are pushed to the image registry specified by the user.
If an existing image with the *latest* tag already exists in your registry, this Action attempts to pull that image as a cache to reduce unnecessary build steps.

Checkout an example of a [quay.io respository](https://quay.io/repository/2i2c/coessing-image?tab=tags) that hosts the user environment image of a 2i2c hub.

## 6. Connect the hub with this user image

In order to be able to pull the image you need to make sure that your repository is public on your registry. For `quay.io` you can set this under `'Repository Settings'>'Repository Visibility'`

1. Go to the list of image tags on `quay.io`, and find the tag of the last push.
   This is usually **under the latest tag**.
   Use this to construct your image name - `quay.io/<quay-username>/<repository-name>:<tag>`.

   ```{figure} ../../../images/coessing-image-quay.png
   :alt: Tags list example
   ```
2. Open the [Configurator](https://pilot.2i2c.org/en/latest/admin/howto/configurator.html) for the hub (you need to be logged in as an admin).
   You can access it from the hub control panel, under Services in the top bar or by going to `https://<hub-address>/services/configurator/`
 
   ```{figure} ../../../images/configurator.png
   :alt: Configurator
   ```
3. Make a note of the current image name there.
4. Put the image tag you constructed in a previous step into the User docker image text box. Note quay web urls look like `quay.io/repository/2i2c/coessing-image`, but the docker image name in configurator **should not** include the repository part of the URL e.g. `quay.io/2i2c/coessing-image:55adca9b2caa`.
5. Click Submit! *this is alpha level software, so there is no 'has it saved' indicator yet :)*

See [the Configurator docs](https://pilot.2i2c.org/en/latest/admin/howto/configurator.html) for more information.

## 7. Test the new image

Test the new image by starting a new user server!
If you already had one running, you need to stop and start it again to test.
If you find new issues, you can revert back to the previous image by entering the old image name in the JupyterHub Configurator.

*This will be streamlined in the future.*

## Appendix: Push the image to a registry other than Quay.io :cloud:

The [jupyterhub/repo2docker-action](https://github.com/jupyterhub/repo2docker-action) can build and push the image to registries other than [Quay.io](https://quay.io/).
Checkout the [action docs](https://github.com/jupyterhub/repo2docker-action/blob/master/README.md) for the instructions on how to setup your workflow to push to: [AWS Elastic Container Registry](https://github.com/jupyterhub/repo2docker-action#push-repo2docker-image-to-amazon-ecr), [Google Container Registry](https://github.com/jupyterhub/repo2docker-action#push-repo2docker-image-to-google-container-registry) (deprecated but popular), [Google Artifact Registry](https://github.com/jupyterhub/repo2docker-action#push-repo2docker-image-to-google-artifact-registry) (preferred), [Azure Container Registry](https://github.com/jupyterhub/repo2docker-action#push-repo2docker-image-to-azure-container-registry).

:::{note}
For cloud provider-specific registries, if we are running the cluster on our projects, please contact the 2i2c team to give you credentials for it.
:::
