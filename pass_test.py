import unittest
from password import *

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
        test_save_multiple_acc to check if we can save multiple account
        objects to our acc_list
        """
        self.new_acc.save_acc()
        test_acc = Account("user", "0712345678")  # new account
        test_acc.save_acc()
        self.assertEqual(len(Account.acc_list), 2)

    def test_acc_exists(self):
        """
        test to check if we can return a Boolean  if we cannot find the account.
        """
        self.new_acc.save_acc()
        test_acc= Account("moses","1234")
        test_acc.save_acc()

        acc_exists = Account.acc_exist("moses","1234")

        self.assertTrue(acc_exists)

class Test_site(unittest.TestCase):
    """
    Test class that defines test cases for the site class behaviours.
    """
    def setUp(self):
        """
        set up method to run before each test case.
        """
        self.new_site = Site("twitter","ngugi","asdf")        
    def test_init(self):
        """
        to test if the object is initialized properly
        """
        self.assertEqual(self.new_site.name,"twitter")
        self.assertEqual(self.new_site.username, "ngugi")
        self.assertEqual(self.new_site.pword, "asdf")
    
    def tearDown(self):
        """
        Method that cleans up after each case has run.
        """
        Site.site_list = []

if __name__ == '__main__':
    unittest.main()