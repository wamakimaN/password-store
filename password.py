import random
import string

class Account:
    """
    class that generates new instances of user accounts
    """
    acc_list = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_acc(self):
        """
        save_acc method saves account objects into acc_list
        """
        Account.acc_list.append(self)

    @classmethod
    def acc_exist(cls, user_name, password):
        for acc in cls.acc_list:
            if acc.user_name == user_name and acc.password == password:
                return True
        return False


class Site:
    """
    class that generates new instances of account credentials
    """
    site_list = []

    def __init__(self, name, username, pword):
        self.name = name
        self.username = username
        self.pword = pword

    def save_site(self):
        """
        save_site method saves account objects into site_list
        """
        Site.site_list.append(self)

    def delete_site(self):
        """
        delete_site method deletes a saved site credentials from the site_list
        """
        Site.site_list.remove(self)

    @classmethod
    def find_by_name(cls, name):
        """
        Method that takes in a name and returns a contact that matches that name.
        """
        for site in cls.site_list:
            if site.name == name:
                return site

    @classmethod
    def display_sites(cls):
        """
        method that returns the site credentials list
        """
        return cls.site_list
    def generate_password():
        char = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        gen_pass = "".join(random.choice(char) for _ in range(8))

        return gen_pass

    
