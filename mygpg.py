#!/usr/bin/env python3
import gpg
from argparse import ArgumentParser
# from lxml import etree


def main():
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', dest='config', metavar='FILENAME', help='read config from FILE')
    parser.add_argument('-g', '--genkey', dest='genkey', default=False, action='store_true',
                        help='generate a new keypair')
    parser.add_argument('-a', '--algo', dest='algo', metavar='ALGO',
                        help='use the ALGO key algorithm when generating keys')
    parser.add_argument('-k', '--keysize', dest='keysize', metavar='KEYSIZE', help='use a key size of length KEYSIZE')
    parser.add_argument('-u', '--user', dest='name', metavar='NAME',
                        help='set NAME as the name to use for the key\'s user-id')
    parser.add_argument('-m', '--email', dest='email', metavar='EMAIL',
                        help='set EMAIL as the email to use for the key\'s user-id')
    parser.add_argument('-C', '--comment', dest='comment', metavar='COMMENT',
                        help='set COMMENT as the comment to use for the key\'s user-id')
    parser.add_argument('-e', '--expiry', dest='expiry', help='EXPIRY duration until keys expire', metavar='EXPIRY')
    
    args = parser.parse_args()
    assert isinstance(args.config, object)
    if args.config:
        load_config(args.config)
    if args.genkey:
        print('Generating new keypair...')


def load_config(filename):
    """Load an XML GPG key parameters file and return its etree object."""
    print('Loaded key params from... ' + filename)


def genkey(key_params):
    """Generate a GPG public and private keypair using the given arguments or config file."""
    
    with gpg.Context() as c:
        c.set_progress_cb(gpg.callbacks.progress_stdout)
        c.op_genkey(key_params, None, None)
        print('Generated key with fingerprint {0}.'.format(
            c.op_genkey_result().fpr))

if __name__ == '__main__':
    main()
