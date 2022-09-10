# Send `support@2i2c.org` encrypted content

Sometimes community representatives need to send us *encrypted* information -
usually credentials for cloud access or an authentication system. We use
[age](https://age-encryption.org/) (pronounced *aghe*) to allow such information to
be encrypted and then sent to use in a way that *anyone* on the team can decrypt,
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