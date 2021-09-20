# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# This script grabs a matrix of hub service features at this address:
# https://docs.google.com/spreadsheets/d/1SEcL8islOY1aQEMzfa2U1MaPWAmmZLX2AWmRLQWH5PE/edit#gid=1864974850
# It then saves it to a CSV so that we can display it in our documentation.

# %%
# Download feature matrix
from pathlib import Path

import pandas as pd


URL_FEATURE_MATRIX = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5p52Wu166vKpcjTu9jf5J2yNG6c_C2-pHRkNLGQwKN2gJ_1UoGlalaglsgtBfQ7W0-aTP11phpgSA/pub?gid=1864974850&single=true&output=csv"

print("Updating feature table...")
features = pd.read_csv(URL_FEATURE_MATRIX)
subset = features.query("status == 'active'")[
    ["name", "category", "description", "research", "education"]
].replace("x", "✔️")

# %% [markdown]
# Sort so that we have the categories grouped properly

# %%
sort_order = [
    "Authentication 🔍",
    "User Environment ⚒️",
    "Configurable resources 📈",
    "Cloud infrastructure ☁️",
    "Service Level 👷‍♀️",
    "Open Source 💗",
]
subset = subset.set_index("category").loc[sort_order].reset_index()

# %% [markdown]
# Munging into a table with headers for each category

# %%
df = []
for cat, data in subset.groupby("category", sort=False):
    data = data.drop(columns=["category"])
    data = pd.concat(
        [
            pd.DataFrame(
                [[f"<p class='feature-header'>{cat}</p>", "", "", ""]],
                columns=data.columns,
            ),
            data,
        ]
    )
    df.append(data)
df = pd.concat(df)

# %% [markdown]
# Saving for re-use in Sphinx

# %%
df.to_csv("../build_assets/feature-matrix.csv", index=None)
print("Finished updating feature table...")
