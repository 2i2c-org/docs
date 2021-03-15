# Distribute content with nbgitpuller

You'll often want to distribute *content* (such as notebooks, scripts, sample
data, etc) to your users so they can do exercises, follow along with a lecture,
or use as a starting point for their own work. This content is often constantly
updated as time goes on, and needs to not overwrite your student's work if you
make an adjustment to content that has already been touched by the student.


[nbgitpuller](https://jupyterhub.github.io/nbgitpuller) is the tool
we recommend for this. The workflow goes something like this:

## Put your content in a public GitHub repository

Create a repository on [GitHub](https://github.com) and start putting your
content there. This is the *source* of the content that will be distributed
to your users. You can update it as often as you wish. While instructors will
need to know how github works, *your users will never have to interact with
git directly*.
   
## Generate an nbgitpuller link

Generate an [nbgitpuller link](http://nbgitpuller.link). This generates a
*clickable link* that contains within it the following pieces of information:

1. The URL to your hub. Upon clicking the link, users will be redirected to
   this hub, and content will be pulled into their home directory there.
2. The URL of the git repository where the content lives.
3. The branch in the git repository where the content lives. The default
   specified there is `master`, although newer GitHub repositories use `main`
   as the default. You can find yours on the Github page of your content
   repository
4. The default interface to open when users click this link. The default is
   the classic notebook, but many other apps are available.
5. A file to open when the link is clicked. When left empty, a directory
   listing with the content of the repository will be shown. 
   
```{figure} ../../images/nbgitpuller-ui.png
The [`nbgitpuller.link`](http://nbgitpuller.link) user interface, along with 
some important fields highlighted.
```

```{tip}
Unfortunately, RStudio does not support opening a specific file, and will 
always show the home directory. Users will have to manually navigate to 
the appropriate file.
```

Once you've filled these out, you can copy the link from the textbox above the form.

## Distribute your nbgitpuller link

Distribute the link you have generated to your users. Upon clicking the link,
they will be:

1. Redirected to your hub, and asked to log in if they have not already
2. The first time the link is clicked, your content repository will be pulled
   into their home directory! 
3. If they had already clicked the link before, any new changes in your
   content repository will be pulled in. Any changes the user has made will
   be [automatically
   merged](https://jupyterhub.github.io/nbgitpuller/topic/automatic-merging.html)
   with changes in the content repository, in such a way that the user's
   changes are never overwritten. All merge conflicts will also be
   automatically resolved, so users don't have to interact with git.
4. If you have picked a specific file to be displayed, the user will be
   redirected to that file, open in the application you picked. If not, the
   directory listing of local copy of the content repository will be shown in
   the application you selected.
   
:::{important}

You **do not** have to create a new link each time you update your content
repository! The same link will continue to work, so you can simply ask your
users to click the link again to fetch the latest changes.

However, if you want to create links to individual files that should be
opened at specific points - like one link per class or assignment - you can
regenerate the links with different values for the file to open or interface.
As long as the hub url, content repository url and the branch name are the
same, users will be not be duplicating content.
:::
