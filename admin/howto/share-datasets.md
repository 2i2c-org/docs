# Share large data files with your users

Sometimes you might need to distribute a set of large files to all
your users, so they don't have to re-download it once per person. 
This is particularly useful in educational contexts, where you might
be teaching a course that reads a common dataset.

```{warning}
If you are teaching with large datasets, you might run out of
memory! So consider teaching with just a subset of data before
distributing large datasets to your users.
```

All users have a directory called `shared` in their home directory.
This is meant to be used to distribute datasets and other files that
can be read by all users. This is a *readonly* directory - regular
users can not write to it.

Admin users will also have a directory called `shared-readwrite` in
their home directory. This is the *same* as the `shared` directory,
but writeable! So any files admins put here will be immediately
visible in all users' `shared` directories.

So to share datasets with users, admins should put the dataset in
`~/shared-readwrite`. If they are distributing notebook / content
that *reads* this dataset, it should refer to files in `~/shared/`
rather than in `~/shared-readwrite`. This will prevent accidental
erasures / writes on behalf of admins.

```{warning}
This is an experimental feature, and the names of these directories
and their structure is subject to change.
```
