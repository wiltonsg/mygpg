#!/usr/bin/env python3
from __future__ import absolute_import, print_function, unicode_literals
del absolute_import, print_function, unicode_literals

#import gpg
import sys
#from lxml import etree

# This is the example from the GPGME manual.
def genkey(self, **kwargs):
    """Generate a GPG public and private keypair using the given arguments or config file."""
    for name, value in kwargs.items():
        if name == "config":
            print("Config File: " + value)
        elif name == "algo-main":
            print("Key Algorithm: " + value)
        elif name == "keysize-main":
            print("Key Size (Primary): " + value)
        elif name == "algo-sub":
            print("Subkey Algorithm: " + value)
        elif name == "keysize-sub":
            print("Key Size (Subkey): " + value)
        elif name == "name":
            print("Common Name: " + value)
        elif name == "userid":
            print("User ID: " + value)
        elif name == "comment":
            print("Comment: " + value)
        elif name == "duration":
            print("Key Duration: " + value)
        else:
            print(kwargs.items)
    
    print(self)

if __name__ == "__main__":
    genkey(sys.argv)
    
    #tree = etree.parse(config)
    
    #with gpg.Context() as c:
        #c.set_progress_cb(gpg.callbacks.progress_stdout)
        #c.op_genkey(parms, None, None)
        #print("Generated key with fingerprint {0}.".format(
    #c.op_genkey_result().fpr))