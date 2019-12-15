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
