# Share data files with your users

Sometimes Hub Admins might need to distribute a set of files to all users, rather than each user re-downloading the same dataset. This is particularly useful for educational use cases, where you might be teaching a course that reads a common dataset.

:::{tip}
If you are teaching with large datasets, you might run out of
memory! So consider teaching with just a subset of data before
distributing large datasets to your users.
:::

## The `shared` directory

There are two folders that are used together to allow administrators to
share data files with all users.

`shared`
: All users have a directory called `shared` in their home directory.
  This is a *readonly* directory - users and administrators can not write to it.
  However, anybody can *access* and *read from* the `shared` directory.
  This is how a user accesses a data file distributed by a Hub administrator.

::::{margin} 
:::{image} media/shared-readwrite.png
:::
The `shared-readwrite` folder appears for Hub Admins only.
::::

`shared-readwrite`
: **(administrators only)** Admins also have a directory called `shared-readwrite` in their home directory. This is the *same folder* as the `shared` directory, but writeable!
  Any files admins put here will be immediately visible in all users' `shared` directories.

### Example workflow

To share datasets with users, Hub Admins should place the dataset in the `~/shared-readwrite` directory. If they are distributing notebook / content that *reads* this dataset, it should refer to files in the `~/shared/` that is readable by all Hub Users and *not* `~/shared-readwrite`. This will prevent accidental deletion or overwriting between Hub Admins.

:::{tip}
It is the responsibility of the Hub Admins delete files in the `shared-readwrite` directory when no longer needed to minimize cloud billing costs. Hub Admins are responsible for managing storage costs and files stored in `shared-readwrite`.
:::

## The `allusers` directory - available upon request

Sometimes, Hub Administrators might need to share data files with the users,
and this files must only be visible to the users that they're addressed to.
For example, uploading graded notebook assignments in each user's home directory.

If such a workflow is needed, then an additional `allusers` directory can be enabled for **administrators only**,
where all the Hub users' directories are accessible to read and modify. Please reach out to us if you'd like this
feature enabled.

```{warning}
Please keep in mind that enabling this feature, means that any admin user could access all users' home directories,
and possibly delete them by accident, if not careful.
So, this feature should be used with extra caution!
```
