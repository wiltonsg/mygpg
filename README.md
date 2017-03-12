# mygpg
```
usage: mygpg.py [-h] [-c FILENAME] [-g] [-a ALGO] [-k KEYSIZE] [-u NAME]
                [-m EMAIL] [-C COMMENT] [-e EXPIRY]

optional arguments:
  -h, --help            show this help message and exit
  -c FILENAME, --config FILENAME
                        read config from FILE
  -g, --genkey          generate a new keypair
  -a ALGO, --algo ALGO  use the ALGO key algorithm when generating keys
  -k KEYSIZE, --keysize KEYSIZE
                        use a key size of length KEYSIZE
  -u NAME, --user NAME  set NAME as the name to use for the key's user-id
  -m EMAIL, --email EMAIL
                        set EMAIL as the email to use for the key's user-id
  -C COMMENT, --comment COMMENT
                        set COMMENT as the comment to use for the key's user-
                        id
  -e EXPIRY, --expiry EXPIRY
                        EXPIRY duration until keys expire
```
