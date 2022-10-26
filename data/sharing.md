# Share data files with your users

Sometimes you might need to distribute a set of files to all
your users, so they don't have to re-download it once per person.
This is particularly useful in educational contexts, where you might
be teaching a course that reads a common dataset.

```{warning}
If you are teaching with large datasets, you might run out of
memory! So consider teaching with just a subset of data before
distributing large datasets to your users.
```

## The `shared` directory

There are two folders that are used together to allow Administrators to
share data files with all users.

`shared`
: All users have a directory called `shared` in their home directory.
  This is a *readonly* directory - users and administrators can not write to it.
  However, anybody can *access* and *read from* the `shared` directory.
  This is how a user accesses a data file distributed by a hub administrator.

`shared-readwrite`
: **(administrators only)** Admin users also have a directory called `shared-readwrite` in their home directory.
  This is the *same folder* as the `shared` directory, but writeable!
  Any files admins put here will be immediately visible in all users' `shared` directories.

## The `allusers` directory - available upon request

Sometimes, hub Administrators might need to share data files with the users,
and this files must only be visible to the users that they're addressed to.
For example, uploading graded notebook assignements in each user's home directory.

If such a workflow is needed, then an additional `allusers` directory can be enabled for **administrators only**,
where all the hub users' directories are accessible to read and modify. Please reach out to us if you'd like this
feature enabled.

```{warning}
Please keep in mind that enabling this feature, means that any admin user could access all users' home directories,
and possibly delete them by accident, if not careful.
So, this feature should be used with extra caution!
```

## A workflow for sharing datasets

To share datasets with users, admins should put the dataset in
`~/shared-readwrite`. If they are distributing notebook / content
that *reads* this dataset, it should refer to files in `~/shared/`
rather than in `~/shared-readwrite`. This will prevent accidental
erasures / writes on behalf of admins.

```{warning}
This is an experimental feature, and the names of these directories
and their structure are subject to change.
```
