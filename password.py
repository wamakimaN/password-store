class Account:
    """
    class that generates new instances of user accounts
    """
    acc_list = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_acc(self):
        Account.acc_list.append(self)
