import unittest
from app.models import Writter
from app import db

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_writter=Writter(password="dynamo")

    #test if the password attribute sets the password to the password_hash attribute
    def test_password_set(self):
        self.assertTrue(self.new_writter.password_hash is not None)

    # test if password given is verified with existing password
    def test_password_verified(self):
        self.assertTrue(self.new_writter.verify_password('dynamo'))

    #test the AttributeError is password s being accessed
    def test_attribute_error(self):
        with self.assertRaises(AttributeError):
            self.new_writter.password