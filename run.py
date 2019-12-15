#!/usr/bin/env python3.6
from password import *

def create_acc(user, key):
    """
    function to create a new account
    """
    new_acc = Account(user,key)
    return new_acc