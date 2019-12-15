import unittest
from password import Account


class Test_acc(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours.
    """

    def setUp(self):
        """
        set up method to run beforemeach test case.
        """
        self.new_acc = Account("wamakima", "qwerty456")

    def test_init(self):
        """
        to test if the object is initialized properly
        """
        self.assertEqual(self.new_acc.user_name, "wamakima")
        self.assertEqual(self.new_acc.password, "qwerty456")


if __name__ == '__main__':
    unittest.main()
