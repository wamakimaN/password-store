import unittest
from password import Account


class Test_acc(unittest.TestCase):
    """
    Test class that defines test cases for the account class behaviours.
    """

    def setUp(self):
        """
        set up method to run before each test case.
        """
        self.new_acc = Account("wamakima", "qwerty456")

    def test_init(self):
        """
        to test if the object is initialized properly
        """
        self.assertEqual(self.new_acc.user_name, "wamakima")
        self.assertEqual(self.new_acc.password, "qwerty456")

    def tearDown(self):
        """
        Method that cleans up after each case has run.
        """
        Account.acc_list = []

    def test_save_acc(self):
        """
        test_save_acc test case to test if the account object is saved into the account list
        """
        self.new_acc.save_acc()
        self.assertEqual(len(Account.acc_list), 1)

    def test_save_multiple_acc(self):
        """
        test_save_multiple_contact to check if we can save multiple contact
        objects to our acc_list
        """
        self.new_acc.save_acc()
        test_acc = Account("user", "0712345678")  # new account
        test_acc.save_acc()
        self.assertEqual(len(Account.acc_list), 2)


if __name__ == '__main__':
    unittest.main()
