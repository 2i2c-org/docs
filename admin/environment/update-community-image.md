# Re-use and modify a community-maintained image for your hub (recommended)

This instructional guide shows you how to add packages to a community-maintained upstream image. In this example, we add the [Python package `xarray`](https://docs.xarray.dev/en/stable/) to the [`jupyter/scipy-notebook` image](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html) maintained by the [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html) community.

(customize-image:set-up-github)=
## Set up the GitHub repository and connect it to quay.io

1. Fork {icon}`octicon:repo-forked` the GitHub repository [example-inherit-from-community-image](https://github.com/2i2c-org/example-inherit-from-community-image) into your GitHub account.

   ```{note}
   If you do not have a quay.io account, then you can register for one at [https://sso.redhat.com](https://sso.redhat.com). Note that if you need to join your organization's account then you should register using an invitation from the organization's admin.
   ```
   
1. We recommend using [quay.io](https://quay.io) to host your custom image. Navigate to [quay.io](https://quay.io) and log into your account.

1. On quay.io, click {icon}`octicon:plus` {gui}`Create a new repository` and name your repository, e.g. `jupyter-scipy-xarray`. Set the repository to {gui}`Public` and leave it as an {icon}`fa6-regular:hard-drive` {gui}`(Empty repository)`.

### Allow robot access to your quay.io repository

The following summarizes [Section 3.2. Allowing robot access to a user repository](https://access.redhat.com/documentation/en-us/red_hat_quay/3.3/html/use_red_hat_quay/use-quay-manage-repo#allow-robot-access-user-repo) of the quay.io documentation.

1. From quay.io, access your user settings by clicking your username in the top-right corner of the screen and selecting {gui}`User settings`.

1. Click the {icon}`fa6-solid:robot` Robot icon from the left column.

1. Click the {icon}`octicon:plus` {gui}`Create Robot Account` button.

   ```{note}
   You can also edit permissions later by clicking {icon}`octicon:gear` {gui}`Options` next to the Robot Account name and selecting {icon}`fa6-regular:hard-drive` {gui}`Set Repository Permissions`.
   ```

1. Name your robot, e.g. `<hub_name>_image_builder` and then check the box next to the repository name that you created in [Set up GitHub repository and connect it to quay.io](#customize-image:set-up-github), e.g. `jupyter-scipy-xarray`. From the dropdown, select the {gui}`Write` permission and then confirm by clicking {gui}`Add permissions`.
   
1. Click the Robot Account name to view its credentials, e.g.
   - *Username:* \<username\>+_<hub_name>_image_builder
   - *Password:* <64 character authorization token>.
   
   ```{image} images/quay-robot-credentials.png
   :alt: Screenshot showing the username and password credentials of a Robot Account on quay.io.
   ```
   
### Create GitHub secrets

The following summarizes [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) of the GitHub documentation.

1. From the fork of your GitHub repository, click {gui}`Settings > Secrets and variables > Actions`

1. Under the section {gui}`Repository secrets`, click the {gui}`New repository secret` button

1. Create two new repository secrets
   - {gui}`Name`: `QUAY_USERNAME` and then paste the Robot account username from above into {gui}`Secret`
   - {gui}`Name`: `QUAY_PASSWORD` and then paste the Robot account password from above into {gui}`Secret`

   ```{image} images/github-secret-username.png
   :alt: Screenshot of adding the QUAY_USERNAME as a GitHub secret.
   ```

   ```{image} images/github-secret-password.png
   :alt: Screenshot of adding the QUAY_PASSWORD as a GitHub secret.
   ```

Once complete, under the section {gui}`Repository secrets` you should now see two rows for `QUAY_USERNAME` and `QUAY_PASSWORD`.
   
### Enable GitHub workflows

1. From the fork of your GitHub repository, click {icon}`octicon:play` {gui}`Actions`.

1. Enable GitHub workflows by clicking {gui}`I understand my workflows, go ahead and enable them`.
   
## Edit GitHub repository files to customize your image

1. Log into your hub to start a small server with the image you wish to update.

   ```{note}
    If your image user interface is RStudio, then you can switch to the JupyterLab interface by altering the URL to the form `https://<hub_name>.2i2c.cloud/user/<username>/lab`.
   ```

1. Click the ![Git icon](images/git.svg) Git icon in the left sidebar to open the JupyterLab Git extension.

1. Clone the forked repository from [Set up the GitHub repository and connect it to quay.io](#customize-image:set-up-github) into the hub by clicking the {gui}`Clone a Repository` button followed by entering the URL of the remote Git repository, e.g. `https://github.com/<username>/example-inherit-from-community-image.git`.

1. Change the working directory by double-clicking *example-inherit-from-community-image* in the file explorer on the left side of the screen.

(customize-image:build-base-image)=
### Build base image

1. Update the GitHub workflow files with your quay.io repository
   - Open *.github/workflows/build.yaml* and update `IMAGE_NAME` with `<username>/jupyter-scipy-xarray`
   - Open *.github/workflows/test.yaml* and update `IMAGE_NAME` with `<username>/jupyter-scipy-xarray`   

   ```{image} images/edit-github-workflow.png
   :alt: Screenshot of updating the IMAGE_NAME in the GitHub workflow test.yaml file.
   ```
   
1. From the ![Git icon](images/git.svg) JupyterLab Git extension, stage your changes to *.github/workflows/build.yaml* and *.github/workflows/test.yaml* by clicking the {icon}`octicon:plus` plus symbol next to the filenames under the {gui}`Changed` section.

1. At the bottom of the panel enter a summary message, e.g. *Update IMAGE_NAME to \<username\>/jupyter-scipy-xarray*, then commit your changes
    
1. Push your changes to the remote repository by clicking the {icon}`octicon:cloud-upload` Git push icon at the top of the panel.

   ````{dropdown} Move code in and out of the hub with GitHub
   
   If you see the following dialog box,
    
   ```{image} https://github.com/czi-catalystproject/hub-champion-training/blob/main/media/episodes/transfer_data/gh-credentials.png?raw=true
   :alt: Screenshot of Git credentials required dialog.
   :width: 65%
   :align: center
   ```

   then we recommend you press {gui}`Cancel` and securely authenticate using `gh-scoped-creds`. See the [2i2c Docs – Move code in and out of the hub with GitHub](../../user/data/git.md) for more information.
   ````

1. This triggers the [repo2docker-action](https://github.com/jupyterhub/repo2docker-action) to build the base image and push this to the quay.io repository. The build process can take a few minutes. You can view the status of the build by visiting the {icon}`octicon:play` {gui}`Actions` tab at `https://github.com/<username>/example-inherit-from-community-image`.
    
1. When the build has finished, you can check your image hosted on quay.io by navigating to a URL of the form `https://quay.io/repository/<username>/<quay-repo-name>`, e.g. *https://quay.io/repository/jnywong/jupyter-scipy-xarray*.
    
### Update the base image
    
1. From the ![Git icon](images/git.svg) JupyterLab Git extension, expand the {gui}`Current Branch` dropdown and click the {gui}`New Branch` button
   - Name your branch, e.g. *add-xarray*
   - Select *main* for the {gui}`Create branch based on...` option.

   ```{image} images/git-create-branch.png
   :alt: Screenshot of creating a new branch from the main branch using the Git JupyterLab extension.
   ```
    
1. Edit the *Dockerfile*
   - Update the `FROM` instruction with the base image you require, e.g. `quay.io/jupyter/scipy-notebook:python-3.11`
   - For now, remove the tests by deleting the `COPY` instruction and deleting the `image-tests` folder in the file explorer.

   ```{image} images/edit-dockerfile.png
   :alt: Screenshot of updating the Dockerfile.
   ```

### Add packages to the Conda environment

1. Edit *environment.yml* 
   - Specify the Python version required, e.g. `python=3.11`
   - Add the extra package(s) to install, e.g. `xarray`.

   ```{image} images/edit-environment-yaml.png
   :alt: Screenshot of updating environment.yml.
   ```
    
1. See the [repo2docker](https://repo2docker.readthedocs.io/en/latest/config_files.html#environment-yml-install-a-conda-environment) documentation for more details on how to configure your environment.
    
### Trigger build and test the custom image
    
1. Stage, commit and push your changes by following the similar steps in Section [Build base image](#customize-image:build-base-image).

1. Visit your GitHub repository at `https://github.com/<username>/example-inherit-from-community-image` and click the {gui}`Compare & pull request` button.
    
1. Open a pull request and double-check that the target branch is *\<username\>:main* (this usually defaults to the upstream repo).

   ```{image} images/check-target-branch.png
   :alt: Screenshot of the target branch option when opening a GitHub pull request.
   ```
    
1. Click {gui}`Create pull request` to confirm, which triggers the [repo2docker-action](https://github.com/jupyterhub/repo2docker-action) to build and push your image to the quay.io registry.

1. When the GitHub actions have completed, it is important to test your image is working as expected by following either [Test the custom image with a 2i2c hub](#customize-image:test-hub) or [Test the custom image with Binder](#customize-image:test-binder).

(customize-image:test-hub)=
#### Test the custom image with a 2i2c hub

1. When the GitHub actions have completed, you can check your image is updated on quay.io by navigating to a URL of the form `https://quay.io/repository/<username>/<quay-repo-name>`, e.g. https://quay.io/repository/jnywong/jupyter-scipy-xarray, and then clicking on the {icon}`fa6-solid:tags` {gui}`Tags` sub-menu to view a list of image versions. The full image tag is of the form

   ```
   <registry>/<username>/<repo_name>:<git-commit-hash>
   ```

   e.g. `quay.io/jnywong/jupyter-scipy-xarray:739fec9705b1`, which you need to provide in the [](#environment:bring-your-own-image).

1. Navigate to your 2i2c hub and paste the image tag into the {gui}`Image > Custom Image > Other...` field (see [](#environment:bring-your-own-image)).

1. Click {gui}`Start` to launch the server and test your custom environment. You can continue editing the *Dockerfile* and *environment.yml*, then push changes to the pull request as required. 

(customize-image:test-binder)=
#### Test the custom image with Binder
    
1. When the GitHub actions have completed, a pull request comment from the *github-actions* bot will appear with a link. Click the {gui}`launch binder` button. The build process can take a few minutes.

1. Once complete, Binder launches into a preview of your custom container hosted at *mybinder.org*.

   ```{image} images/launch-mybinder.png
   :alt: Screenshot of the Binder launcher.
   ```
    
   Test the preview of your custom environment. You can continue editing the *Dockerfile* and *environment.yml*, then push changes to the pull request as required.

## Publish your new image

1. When you are ready to push the repository to quay.io, merge the pull request to *main* on GitHub by clicking {gui}`Confirm merge`. The build process can take a few minutes.

   ```{note}
   The `git-commit-hash` is useful for matching the image to the changes associated with the corresponding commit in your GitHub repository's history.
   ```

1. You can check your image is updated on quay.io by navigating to a URL of the form `https://quay.io/repository/<username>/<quay-repo-name>`, e.g. https://quay.io/repository/jnywong/jupyter-scipy-xarray, and then clicking on the {icon}`fa6-solid:tags` {gui}`Tags` sub-menu to view a list of image versions. The full image tag is of the form

   ```
   <registry>/<username>/<repo_name>:<git-commit-hash>
   ```

   e.g. `quay.io/jnywong/jupyter-scipy-xarray:739fec9705b1`.

## Link custom image to your hub

Now that your image is published, follow these instructions: [](./customize.md#customize-image:link-custom-image).
