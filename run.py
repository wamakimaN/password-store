#!/usr/bin/env python3.6
from password import *


def create_acc(user, key):
    """
    function to create a new account
    """
    new_acc = Account(user, key)
    return new_acc


def create_site(sname, suser, skey):
    """
    function to create a new account
    """
    new_site = Site(sname, suser, skey)
    return new_site

def save_account(acc):
    """
    Function to save contact
    """
    acc.save_acc()