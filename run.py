#!/usr/bin/env python3.6
import getpass
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


def display_sites():
    """
    Function that returns all the saved site credentials
    """
    return Site.display_sites()


def main():
    print("Welcome to Pass Locker")
    print("\n")
    while True:
        print("-"*70)
        short_code = input(
            "Use the following short codes: ca - Create account, lg - login to your account(if you have one), ex - exit Pass Locker \n").lower().strip()
        print("."*75)

        if short_code == "ca":
            print("Create account")
            user_name = input("User Name: ")
            password = input("Password: ")

            save_account(create_acc(user_name, password))  # create account
            print("\n")
            print(f"Congratulations {user_name} you may now log in")
            print("\n")

        elif short_code == "lg":
            print("Log In")
            username = input("User Name: ")
            passwrd = getpass.getpass()
            signin = user_login(username, passwrd)
            if signin == True:
                print(f"Welcome {username}. What would you like to do?")
                while True:
                    print("-"*70)
                    short_code = input(
                        "Use the following short codes: as - add site credentials, dc - delete credentials, da - display all credentials, sc - search credentials, ex - exit Pass Locker \n").lower().strip()
                    print("."*75)
                    if short_code == "as":
                        print("Enter new site credentials")
                        sitename = input("Site name: ")
                        siteuser = input("User name: ")
                        sitepass = input("password: ")
                        save_sitec(create_site(sitename, siteuser, sitepass))
                        print(
                            f"New created account: \n Account:{sitename}\n User Name:{siteuser} \n Password: {sitepass}")

                    elif short_code == "da":
                        if display_sites():
                            for site in display_sites():
                                print(
                                    f"site:{site.name} \n User Name:{site.username} \n Password:{site.pword}\n")
                        else:
                            print("You do not seem to have anything saved yet")

                    elif short_code == "dc":
                        print("Enter the name of the site you want to delete:")
                        delete_name = input("Site name: ")
                        if site_search(delete_name):
                            delete_site = site_search(delete_name)
                            del_site(delete_site)
                        else:
                            print("Enter valid name")

                    elif short_code == "sc":
                        print("Enter the name of the site you want to view:")
                        search_name = input("Site name: ")
                        if site_search(search_name):
                            search_site = site_search(search_name)
                            print(f"Site name....{search_site.name}")
                            print(f"User name....{search_site.username}")
                            print(f"Password....{search_site.pword}")
                        else:
                            print("Enter valid name")

            else:
                print("Details did not match any user...Create account?")

        elif short_code == "ex":
            print("You have successfully exited Pass Locker")
            break


if __name__ == '__main__':

    main()
