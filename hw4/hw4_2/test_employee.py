import unittest
from unittest.mock import patch
from employee import Employee


class MockTestTrue:
    ok = True
    text = 'response.ok = True'
    status_code = 200
    elapsed = 100

    def __init__(self, *args, **kwargs):
        pass


class MockTestFalse:
    ok = False
    text = 'response.ok = False'
    status_code = 400
    elapsed = 100

    def __init__(self, *args, **kwargs):
        pass


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Robert', 'Johns', 53221)

    def test_email(self):
        self.assertEqual(self.employee.email.lower(), 'robert.johns@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee.fullname.lower(), 'robert johns')

    def test_apply_raise(self):
        self.employee.apply_raise()
        self.assertEqual(self.employee.pay, 55882)
        self.assertEqual(self.employee.pay, 55882.0)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mocker):
        mocker.side_effect = MockTestTrue
        self.assertEqual(self.employee.monthly_schedule('April'), 'response.ok = True')

        mocker.side_effect = MockTestFalse
        self.assertEqual(self.employee.monthly_schedule('February'), 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
