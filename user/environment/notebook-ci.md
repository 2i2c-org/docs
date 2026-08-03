(user:notebook-ci)=
# Run notebooks and Jupyter Books as part of your repository's CI/CD on Binder

If you publish notebooks (e.g. in a MyST or Jupyter Book site) and want CI to confirm they still execute correctly over time, [BinderBot](https://2i2c.org/binderbot) is a GitHub Action and CLI that runs them on mybinder.org instead of the CI runner.

:::{admonition} Example use by communities
:class: seealso
Project Pythia's [`cookbook-actions` workflow](https://github.com/ProjectPythia/cookbook-actions/blob/8ec8389666adab5d244a23e1b046bfb7b9bf3804/.github/workflows/build-book.yaml#L158-L163) uses BinderBot to execute their MyST cookbooks on Binder as part of CI.
:::

If you'd like help setting this up, [open a support request](../../support.md).
