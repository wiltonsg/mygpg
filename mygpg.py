#!/usr/bin/env python3
from __future__ import absolute_import, print_function, unicode_literals
del absolute_import, print_function, unicode_literals

#import gpg
import sys
from optparse import OptionParser
#from lxml import etree

def main():
    parser = OptionParser()
    parser.add_option("-c", "--config", dest="config", help="read config from FILE", metavar="FILE")
    parser.add_option("-a", "--algo", dest="algo", help="Use the key algorithm ALGO when generating", metavar="ALGO")
    (options, args) = parser.parse_args()
    if options.config:
        print(options.config)
    elif options.algo:
        print(options.algo)
        
def genkey(self, **kwargs):
    """Generate a GPG public and private keypair using the given arguments or config file."""
    #with gpg.Context() as c:
        #c.set_progress_cb(gpg.callbacks.progress_stdout)
        #c.op_genkey(parms, None, None)
        #print("Generated key with fingerprint {0}.".format(
    #c.op_genkey_result().fpr))    

if __name__ == "__main__":
    main()
    