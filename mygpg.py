#!/usr/bin/env python3
from __future__ import absolute_import, print_function, unicode_literals
del absolute_import, print_function, unicode_literals

import gpg
from argparse import ArgumentParser
from lxml import etree

def main():
    parser = ArgumentParser()
    parser.add_argument("-c", "--config", dest="config", help="read config from FILE", metavar="FILE")
    parser.add_argument("-g", "--genkey", dest="genkey", default=False, action="store_true", help="generate a new keypair")
    parser.add_argument("-a", "--algo", dest="algo", help="use the ALGO key algorithm when generating keys", metavar="ALGO")
    parser.add_argument("-k", "--keysize", dest="keysize", help="use a key size of length KEYSIZE", metavar="KEYSIZE")
    parser.add_argument("-u", "--user", dest="name", help="set NAME as the name to use for the key's user-id", metavar="NAME")
    parser.add_argument("-m", "--email", dest="email", help="set EMAIL as the email to use for the key's user-id", metavar="EMAIL")
    parser.add_argument("-C", "--comment", dest="comment", help="set COMMENT as the comment to use for the key's user-id", metavar="COMMENT")
    parser.add_argument("-e", "--expiry", dest="expiry", help="EXPIRY duration until keys expire", metavar="EXPIRY")
    
    args = parser.parse_args()
    if args.config:
        load_config(args.config)
    if args.genkey:
        print("Generating new keypair...")

def load_config(file):
    """Load an XML GPG key parameters file and return its etree object."""
    print("Loaded key params from... " + file)

def genkey(key_parms):
    """Generate a GPG public and private keypair using the given arguments or config file."""
    
    with gpg.Context() as c:
        c.set_progress_cb(gpg.callbacks.progress_stdout)
        c.op_genkey(key_parms, None, None)
        print("Generated key with fingerprint {0}.".format(
            c.op_genkey_result().fpr))

if __name__ == "__main__":
    main()
