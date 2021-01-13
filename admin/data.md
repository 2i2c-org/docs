# Data access and sharing

## Share data and files across users

Hubs have a folder called `shared` that is meant for distributing files, data, etc that **all users have access to**. This can be useful for utilizing a shared resource on the hub so that all students don't have to download it themselves (for example, a dataset that is commonly-used in course material).

The `shared` folder is **read-only**, and accessible by *all* users. There is also a `shared-readwrite` folder that has **write and read** privileges, and **only accessible by hub administrators**. All files placed in `shared-readwrite` will show up in `shared` for users.

To share files across users, follow these steps:

- **Hub Aministrators** put files in `shared-readwrite`.

  e.g. on an admin account, put a CSV file in a location like:

  ```
  ~/shared-readwrite/myshareddata.csv
  ```
- **Users access those files** in their code. E.g., run code like:

  ```python
  import pandas as pd
  pd.read_csv("~/shared/myshareddata.csv")
  ```

```{seealso}
To share *content* that is stored in a public repository, see [](include-content).
```

## User storage

Each user gets their own storage that persists across user sessions.
These files are only accessible to the user and to hub administrators.
However, see the other sections on this page for ways to share content and data between users.
