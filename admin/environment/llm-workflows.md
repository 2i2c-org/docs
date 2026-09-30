# LLM and AI workflows

Some communities want their users to have access to Large Language Models (LLMs) / Generative AI (GenAI) models.
For example, via coding agents in the terminal or [Jupyter AI](https://github.com/jupyterlab/jupyter-ai) in JupyterLab.
This is a new and evolving space, so your best bet is to learn how other communities have set up their hubs and workflows, and look to their configuration for inspiration.

For one approach, check out our blog post: [How we set up an AI-enabled hub for the Responsible GenAI workshop](https://2i2c.org/blog/genai-workshop-hub-setup/).
It covers the configuration used by the [CryoCloud](https://book.cryointhecloud.com/) and [NASA ESDS](https://www.earthdata.nasa.gov/esds) communities for a recent GenAI workshop, including the user image, model access, and what we'd improve next time.

A few things to keep in mind:

- Install AI tools in your [community image](customize.md), like any other package.
- Model providers need an API key. 2i2c can [add a shared key to your hub](#managing-secrets), but every user can read it.
- Reach out to [support](#support) if you'd like to set up something similar.
