(outages)=
# Outages

An outage is a period of time when a hub critical service is unavailable or not functioning as expected and impacting the hub users' activity.
We strive to minimize outages and their impact on users, but they can still happen for various reasons.

This page documents the categories of outages and what the users are experiencing during those outages.
If you or your users are experiencing any of these outages, please [reach out to support](support:email) as soon as possible. It's helpful if you're able to share with us which specific users are experiencing an outage and what they're seeing. 

## 1. Hub URL is unavailable
When accessing the hub URL, users are presented with a “Service Unavailable" error or the domain doesn't resolve.

## 2. Authorized users cannot login
After taking all the steps to login into the hub, the user is presented with an error message or redirected to the login page in a loop, even though they should be able to access the hub, i.e. they have been authorized by an admin user.
These users aren’t able to reach the server spawn page.

## 3. User servers not starting 
After the user has logged in, when they try to start a server, it either just fails super fast or after a long timeout period.

## 4. Home directory for a hub is full and users can not write files
When users try to create new files or save their progress they aren't able to.

## 5. Reduced performance of the system
When such an outage is happening, users are experiencing long server startup times, their kernels dying or RStudio intermittent 500x errors.

## 6. Underlying Infrastructure outages
When the underlying infrastructure (e.g. the cloud provider, quay.io etc) is experiencing an outage users can experience image building not working, hub url not being unavailable, or users servers not starting,
