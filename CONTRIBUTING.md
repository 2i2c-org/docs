# Contributing to this repository

Most of this repository is structured for **Sphinx**, a documentation engine in Python.

## Build the documentation locally

The easiest way to build the documentation in this repository is to use `nox`, a tool for quickly building environments and running commands within them.
This ensures that your environment has all the dependencies needed to build the documentation.

To do so, follow these steps:

1. Install `nox`

   ```
   pip install nox
   ```
2. Build the documentation:

   ```
   nox -s docs_build
   ```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `_build/html`.

To build live documentation that updates when you update local files, run the following command:

```
nox -s docs_live
```

## Pre-populate the FreshDesk Help widget

We use a [FreshDesk Help Widget](https://support.freshdesk.com/support/solutions/articles/239273-set-up-your-help-widget) to let users quickly submit support tickets from our documentation.
This is the little widget in the bottom-right that you can click on.

Configuration for the JavaScript that loads this widget is in our `conf.py` file.
See the `widget_embed_code` section.

### Create a button to make the widget pop up

Trigger the Help widget by calling the `openWidget()` function in JavaScript.
You can attach it to a button by embedding some raw HTML in MyST Markdown like so:

```html
<button onclick="openWidget()">
   Click here to open a support ticket
</button>
```

<button onclick="openWidget()">
   Click here to open a support ticket
</button>

### Pre-fill parts of the support widget

You can configure the button to pre-populate fields for the user so that they can ask make their request more quickly.
To do so, use `key:"value"` pairs in the call to `openWidget()`.

See the `widget_embed_code` section of `conf.py` for the list of possible field names.

The example below populates a few extra fields:

```html
<button onclick="openWidget({name:'Jo the Jovyan', description:'This is a cool feature!', type: 'Feature Request'})">
   Click here to open a support ticket
</button>
````

<button onclick="openWidget({name:'Jo the Jovyan', description:'This is a cool feature!', type: 'Feature Request'})">
   Click here to open a support ticket
</button>

:::{admonition} Things to pay attention to:

- **Note curly brackets!** You need to give the `key:val` pairs inside curly brackets!
- **Type must exactly match a dropdown option**. If you get the case, spacing, etc wrong, then no option will be selected.
:::