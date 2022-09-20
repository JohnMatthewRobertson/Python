import unittest

from application import create_application_instance

class TestCase_Create_UserCar_Using_Model(unittest.TestCase):

    def setUp(self):
        self.app = create_application_instance()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_create_user_car(self):
        