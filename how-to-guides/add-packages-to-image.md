# Add packages to a community-maintained upstream image

This instructional guide shows you how to add packages to a community-maintained upstream image. In this example, we add the [Python package `xarray`](https://docs.xarray.dev/en/stable/) to the [`jupyter/scipy-notebook` image](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html) maintained by the [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html) community.

```{contents}
:maxdepth: 2
:local:
```

(add-packages:set-up-github)=
## Set up the GitHub repository and connect it to quay.io

1. Fork {octicon}`repo-forked;1em;sd-text-info` the GitHub repository [example-inherit-from-community-image](https://github.com/yuvipanda/example-inherit-from-community-image) into your GitHub account.

   ```{margin}
   If you do not have a quay.io account, then can register for one at [https://sso.redhat.com](https://sso.redhat.com). Note that if you need to join your organization's account then you should register using an invitation from the organization's admin.
   ```
   
1. We recommend using [quay.io](https://quay.io) to host your custom image. Navigate to [quay.io](https://quay.io) and log into your account.

1. On quay.io, click {octicon}`plus;1em;sd-text-info` *Create a new repository* and name your repository, e.g. `jupyter-scipy-xarray`. Set the repository to *Public* and leave it as an <i class="fa-regular fa-hard-drive sd-text-info"></i> *(Empty repository)*.


### Allow robot access to your quay.io repository

The following summarizes [Section 3.2. Allowing robot access to a user repository](https://access.redhat.com/documentation/en-us/red_hat_quay/3.3/html/use_red_hat_quay/use-quay-manage-repo#allow-robot-access-user-repo) of the quay.io documentation.

1. From quay.io, access your user settings by clicking your username in the top-right corner of the screen and selecting *User settings*.

1. Click the <i class="fa fa-robot sd-text-info"></i> Robot icon from the left column.

1. Click the {octicon}`plus;1em;sd-text-info` *Create Robot Account* button.

   ```{margin}
   You can also edit permissions later by clicking {octicon}`gear;1em;sd-text-info` *Options* next to the Robot Account name and selecting <i class="fa-regular fa-hard-drive sd-text-info"></i> *Set Repository Permissions*.
   ```

1. Name your robot, e.g. `<hub_name>_image_builder` and then check the box next to the repository name that you created in [Set up GitHub repository and connect it to quay.io](#set-up-github-repository-and-connect-it-to-quay-io), e.g. `jupyter-scipy-xarray`. From the dropdown, select the *Write* permission and then confirm by clicking *Add permissions*.
   
1. Click the Robot Account name to view its credentials, e.g.
   - *Username:* \<username\>+_<hub_name>_image_builder
   - *Password:* <64 character authorization token>.
   
   ```{image} media/quay-robot-credentials.png
   :alt: Screenshot showing the username and password credentials of a Robot Account on quay.io.
   ```
   
### Create GitHub secrets

The following summarizes [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) of the GitHub documentation.

1. From the fork of your GitHub repository, click *Settings > Secrets and variables > Actions*

1. Under the section *Repository secrets*, click the *New repository secret* button

1. Create two new repository secrets
   - *Name*: `QUAY_USERNAME` and then paste the Robot account username from above into *Secret*
   - *Name*: `QUAY_PASSWORD` and then paste the Robot account password from above into *Secret*

   ```{image} media/github-secret-username.png
   :alt: Screenshot of adding the QUAY_USERNAME as a GitHub secret.
   ```

   ```{image} media/github-secret-password.png
   :alt: Screenshot of adding the QUAY_PASSWORD as a GitHub secret.
   ```

Once complete, under the section *Repository secrets* you should now see two rows for `QUAY_USERNAME` and `QUAY_PASSWORD`.
   
### Enable GitHub workflows

1. From the fork of your GitHub repository, click {octicon}`play;1em;sd-text-info` *Actions*.

1. Enable GitHub workflows by clicking *I understand my workflows, go ahead and enable them*.
   
## Edit GitHub repository files to customize your image

1. Log into your hub to start a small server with the image you wish to update.

   ```{margin}
    If your image user interface is RStudio, then switch to the JupyterLab interface by altering the URL to the form `https://<hub_name>.2i2c.cloud/user/<username>/lab`.
   ```

1. Click on the ![Git icon](media/git.svg) to open the JupyterLab Git extension.

1. Clone the forked repository from [Set up the GitHub repository and connect it to quay.io](#set-up-the-github-repository-and-connect-it-to-quay-io) into the hub by the clicking *Clone a Repository* button followed by entering the URL of the remote Git repository, e.g. `https://github.com/<username>/example-inherit-from-community-image.git`.

1. Change the working directory by double-clicking *example-inherit-from-community-image* in the file explorer on the left side of the screen.

### Build base image

1. Update the GitHub workflow files with your quay.io repository
   - Open *.github/workflows/build.yaml* and update `IMAGE_NAME` with e.g. `<username>/jupyter-scipy-xarray`
   - Open *.github/workflows/test.yaml* and update `IMAGE_NAME` with e.g. `<username>/jupyter-scipy-xarray`   

   ```{image} media/edit-github-workflow.png
   :alt: Screenshot of updating the IMAGE_NAME in the GitHub workflow test.yaml file.
   ```
   
1. From the ![Git icon](media/git.svg) JupyterLab Git extension, stage your changes to *.github/workflows/build.yaml* and *.github/workflows/test.yaml* by clicking the {octicon}`plus;1em;sd-text-info` plus symbol next to the filenames under the *Changed* section.

1. At the bottom of the panel enter a summary message, e.g. *Update IMAGE_NAME to \<username\>/jupyter-scipy-xarray*, then commit your changes
    
1. Push your changes to the remote repository by clicking the <svg width="16" viewBox="0 0 18 18" xmlns="http://www.w3.org/2000/svg" data-icon="git:push"><path xmlns="http://www.w3.org/2000/svg" class="jp-icon3" d="M14.5125 7.53C14.0025 4.9425 11.73 3 9 3C6.8325 3 4.95 4.23 4.0125 6.03C1.755 6.27 0 8.1825 0 10.5C0 12.9825 2.0175 15 4.5 15H14.25C16.32 15 18 13.32 18 11.25C18 9.27 16.4625 7.665 14.5125 7.53ZM14.25 13.5H4.5C2.8425 13.5 1.5 12.1575 1.5 10.5C1.5 8.9625 2.6475 7.68 4.17 7.5225L4.9725 7.44L5.3475 6.7275C6.06 5.355 7.455 4.5 9 4.5C10.965 4.5 12.66 5.895 13.0425 7.8225L13.2675 8.9475L14.415 9.03C15.585 9.105 16.5 10.0875 16.5 11.25C16.5 12.4875 15.4875 13.5 14.25 13.5ZM6 9.75H7.9125V12H10.0875V9.75H12L9 6.75L6 9.75Z" fill="#4F4F4F"></path></svg> Git push icon at the top of the panel.

   ````{Note}
   If you see the following dialog box,
    
   ```{image} https://github.com/czi-catalystproject/hub-champion-training/blob/main/media/episodes/transfer_data/gh-credentials.png?raw=true
   :alt: Screenshot of Git credentials required dialog.
   :width: 65%
   :align: center
   ```

   then we recommend you press *Cancel* and securely authenicate using `gh-scoped-creds`. See the [2i2c Docs](https://2i2c.org/community-showcase/user/topics/data/git.html) for more information.
   ````

1. This triggers the [repo2docker-action](https://github.com/jupyterhub/repo2docker-action) to build the base image and push this to the quay.io repository. The build process can take a few minutes. You can view the status of the build by visiting the {octicon}`plus;1em;sd-text-info` *Actions* tab at `https://github.com/<username>/example-inherit-from-community-image`.
    
1. When the build has finished, you can check your image hosted on quay.io by navigating to a URL of the form *https://quay.io/repository/\<username\>/\<quay-repo-name\>*, e.g. *https://quay.io/repository/jnywong/jupyter-scipy-xarray*.
    
### Update the base image
    
1. From the ![Git icon](media/git.svg) JupyterLab Git extension, expand the *Current Branch* dropdown and click the *New Branch* button
   - Name your branch, e.g. *add-xarray*
   - Select *main* for the *Create branch based on...* option.

   ```{image} media/git-create-branch.png
   :alt: Screenshot of creating a new branch from the main branch using the Git JupyterLab extension.
   ```
    
1. Edit the *Dockerfile*
   - Update the `FROM` instruction with the base image you require, e.g. `quay.io/jupyter/scipy-notebook:python-3.11`
   - Remove the tests for the sake of simplicity by deleting the `COPY` instruction and deleting the `image-tests` folder in the file explorer.

   ```{image} media/edit-dockerfile.png
   :alt: Screenshot of updating the DockerFile.
   ```

### Add packages to the Conda environment

1. Edit *environment.yml* 
   - Specify the Python version required, e.g. `python=3.11`
   - Add the extra package(s) to install, e.g. `xarray`.

   ```{image} media/edit-environment-yaml.png
   :alt: Screenshot of updating environment.yml.
   ```
    
1. See the [repo2docker](https://repo2docker.readthedocs.io/en/latest/config_files.html#environment-yml-install-a-conda-environment) documentation for more details on how to configure your environment.
    
### Trigger build and check the custom image on Binder
    
1. Stage, commit and push your changes by following the similar steps in Section [Build base image](build-base-image).

1. Visit your GitHub repository at `https://github.com/<username>/example-inherit-from-community-image` and click the *Compare & pull request* button.
    
1. Open a pull request and double-check that the target branch is *\<username\>:main* (this usually defaults to the upstream repo).
    
1. Click *Create pull request* to confirm, which will trigger the [repo2docker-action](https://github.com/jupyterhub/repo2docker-action) to build a preview of your custom image using Binder. 
    
1. When the Binder is ready, a pull request comment from the *github-actions* bot will appear with a link. Click the *launch binder* button. The build process can take a few minutes.

1. Once complete, Binder launches into a preview of your custom container hosted at *mybinder.org*.

   ```{image} media/launch-mybinder.png
   :alt: Screenshot of the Binder launcher.
   ```
    
   Test the preview of your custom environment. You can continue editing the *DockerFile* and *environment.yml*, then push changes to the pull request as required.
    
1. When you are ready to push the repository to quay.io, merge the pull request to *main* on GitHub by clicking *Confirm merge*. The build process can take a few minutes.

   ```{margin}
   The `git-commit-hash` is useful for matching the image to the changes associated with the corresponding commit in your GitHub repository's history.
   ```

1. You can check your image is updated on quay.io by navigating to a URL of the form `https://quay.io/repository/<>username/<repo_name>`, e.g. https://quay.io/repository/jnywong/jupyter-scipy-xarray, and then clicking on the <i class="fa fa-tags sd-text-info"></i> Tags sub-menu to view a list of image versions. The full image tag is of the form

   ```
   <registry>/<username>/<repo_name>:<git-commit-hash>
   ```

e.g. `quay.io/jnywong/jupyter-scipy-xarray:739fec9705b1`, which you need to provide in the Section [Link custom image to your hub](#link-custom-image-to-your-hub).
    
## Link custom image to your hub
    
1. Open a [2i2c support ticket](https://docs.2i2c.org/support/) to request an update to your hub with the new custom image.

```{image} media/open-support-ticket.png
:alt: Screenshot of 2i2c support ticket.
```

1. In the *Topic of Request* option, select the *Image Change Request* option and in the *Description* provide a link to the full image tag.
    
1. Click the *Send button* to confirm the support ticket request.
