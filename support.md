(support:email)=
# Get support

Send all support requests as an email to [**`support@2i2c.org`**](mailto:support@2i2c.org).
This will be routed to the 2i2c support team, and we will get back to you shortly!
When you make a support request, please include as much information as possible in order to provide context needed to resolve your issue!

% hard-coding this because sphinx-design buttons don't work with mailto
<a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-primary reference external" href="mailto:support@2i2c.org"><span>Send a support email</span></a>

## Types of support

For information about the types of support we may offer, and how it relates to our Shared Responsibility Model, see [](shared-responsibility:support).

## Who can ask for support?

A **Community Representative** of a hub should be the one that surfaces support requests to the 2i2c Engineering Team.
Before reaching out to 2i2c for support, this person should work with others in their community to understand the problem and to ensure that it is something that requires intervention from a 2i2c Engineer.

## The support process

When you send us a support email, we'll try and resolve your issue via the following process:

- The email to `support@2i2c.org` will open up a ticket in [the 2i2c FreshDesk account](https://2i2c.freshdesk.com).
  This is a private space where 2i2c engineers can communicate with you and one another around the issue.
- We will investigate to understand what kind of issue is at hand.
  2i2c provides support for major infrastructure problems, outages, or upgrades.
  It doesn't provide support for daily workflow questions like debugging tracebacks in Python libraries.
- If needed, we'll open an issue in [our `infrastructure` repository](https://github.com/2i2c-org/infrastructure) in order to track the steps needed to resolve this issue.
- Throughout this process, we'll communicate with you via the `support@2i2c.org` address. You are also  welcome to follow along and discuss in any issues that we may create if you prefer.
- When the issue is resolved, we'll send you a confirmation via `support@2i2c.org`, and we'll close the support issue.

## Send encrypted content

Sometimes community representatives need to send us *encrypted* information -
usually credentials for cloud access or an authentication system. We use
[age](https://age-encryption.org/) (pronounced *aghe*) to allow such information to
be encrypted and then sent to us in a way that *anyone* on the team can decrypt,
rather than the information be tied to a single engineer. You'll be directed to this
page by 2i2c support if we require something encrypted from you.

This page describes how you can encrypt information and send it to us!

1. [Install age](https://github.com/FiloSottile/age#installation) on your computer.
   On a Mac, if you are using `homebrew`, you can simply `brew install age`. On Linux,
   your package emanager should have `age`, and on Windows you can find binaries to download
   [from the releases page](https://github.com/FiloSottile/age/releases). See
   [all installation options](https://github.com/FiloSottile/age#installation)
2. Run `age -e -r age1mmx8hfzalmn3tmpryrfvcud5vyfakxdfqe683r40qkr6pjd2ag6s72cat5 -a` on
   your terminal, and paste the contents of the message you want to encrypt. Press enter,
   then `Ctrl-D`. Make sure to copy this exactly!
3. `age` will print the encrypted version of your message on your terminal, and it'll look
   something like this:

   ```
   -----BEGIN AGE ENCRYPTED FILE-----
   YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSAzOW1zTEwrM0FOZ2dWQUo0
   bks2WlZ0eU5LclRVNW4wcEZzRngyT0NSUkRjCm5oR0hGbzV0ZXJ4ZE0xQkdqSXFY
   WkoxaWI4VWQvd3pNbnpiR1BjTnNwREkKLS0tIHpLRXorOWlsS2pFWHFiK1JqUW8v
   U1pyYW40QSswcFNRZnBDcDcwN29EeVUKC5temNTLqJPd5oT0kfOOK2UHGgb2IVzK
   zZS5QmYxmbRNa7qRGqbL
   -----END AGE ENCRYPTED FILE-----
   ```

4. Copy the encrypted version of the message and include it in the message to `support@2i2c.org`.
   All 2i2c engineers will be able to decrypt the message!
