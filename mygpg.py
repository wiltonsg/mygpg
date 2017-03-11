#!/usr/bin/env python3
from __future__ import absolute_import, print_function, unicode_literals
del absolute_import, print_function, unicode_literals

import gpg
from optparse import OptionParser
from lxml import etree

def main():
    parser = OptionParser()
    parser.add_option("-c", "--config", dest="config", help="read config from FILE", metavar="FILE")
    parser.add_option("-g", "--genkey", dest="genkey", help="generate a new keypair", default=False, action="store_true")
    parser.add_option("-a", "--algo", dest="algo", help="use the ALGO key algorithm when generating keys", metavar="ALGO")
    parser.add_option("-k", "--keysize", dest="keysize", help="use a key size of length KEYSIZE", metavar="KEYSIZE")
    parser.add_option("-u", "--user", dest="name", help="set NAME as the name to use for the key's user-id", metavar="NAME")
    parser.add_option("-m", "--email", dest="email", help="set EMAIL as the email to use for the key's user-id", metavar="EMAIL")
    parser.add_option("-C", "--comment", dest="comment", help="set COMMENT as the comment to use for the key's user-id", metavar="COMMENT")
    parser.add_option("-e", "--expiry", dest="expiry", help="EXPIRY duration until keys expire", metavar="EXPIRY")
    
    (options, args) = parser.parse_args()
    if options.config:
        load_config(options.config)
    elif options.genkey:
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
