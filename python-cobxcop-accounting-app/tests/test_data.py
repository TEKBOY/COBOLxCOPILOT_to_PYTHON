import unittest
from data_program import DataProgram

class TestDataProgram(unittest.TestCase):
    def setUp(self):
        self.dp = DataProgram()

    def test_initial_balance(self):
        self.assertEqual(self.dp.storage_balance, 1000.00)

    def test_read_operation(self):
        self.assertEqual(self.dp.process_operation('READ'), 1000.00)

    def test_write_operation(self):
        self.dp.process_operation('WRITE', 500.50)
        self.assertEqual(self.dp.storage_balance, 500.50)

    def test_write_and_read(self):
        self.dp.process_operation('WRITE', 123.45)
        self.assertEqual(self.dp.process_operation('READ'), 123.45)

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            self.dp.process_operation('INVALID')

    def test_write_without_balance(self):
        with self.assertRaises(ValueError):
            self.dp.process_operation('WRITE')

    def test_case_insensitive_read(self):
        self.assertEqual(self.dp.process_operation('read'), 1000.00)

    def test_case_insensitive_write(self):
        self.dp.process_operation('write', 888.88)
        self.assertEqual(self.dp.storage_balance, 888.88)

    def test_strip_operation(self):
        self.dp.process_operation('  WRITE  ', 777.77)
        self.assertEqual(self.dp.storage_balance, 777.77)

if __name__ == '__main__':
    unittest.main() 