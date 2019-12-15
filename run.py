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
    Function to save account
    """
    acc.save_acc()


def save_sitec(site):
    """
    Function to save site credentials
    """
    site.save_site()


def user_login(userName, passWord):
    """
    function that checks whether an account exist and then logs in the user.
    """
    return Account.acc_exist(userName, passWord)

def site_search(name):
    """
    function that returns a site acording to name searched
    """
    return Site.find_by_name(name)

def del_site(site):
    """
    function to delete site instances
    """
    site.delete_site()