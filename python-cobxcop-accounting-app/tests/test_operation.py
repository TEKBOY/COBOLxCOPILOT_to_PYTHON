import unittest
from unittest.mock import patch
from operations import Operations

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.ops = Operations()
        self.ops.data_program.reset_balance()

    @patch('builtins.print')
    def test_total_operation(self, mock_print):
        self.ops.process('TOTAL')
        mock_print.assert_called_with('Current balance: 1000.00')

    @patch('builtins.input', return_value='100')
    @patch('builtins.print')
    def test_credit_operation(self, mock_print, mock_input):
        self.ops.process('CREDIT')
        mock_print.assert_called_with('Amount credited. New balance: 1100.00')

    @patch('builtins.input', return_value='200')
    @patch('builtins.print')
    def test_debit_operation(self, mock_print, mock_input):
        self.ops.process('DEBIT')
        mock_print.assert_called_with('Amount debited. New balance: 900.00')

    @patch('builtins.input', return_value='2000')
    @patch('builtins.print')
    def test_debit_insufficient_funds(self, mock_print, mock_input):
        self.ops.process('DEBIT')
        mock_print.assert_called_with('Insufficient funds for this debit.')

    @patch('builtins.print')
    def test_unknown_operation(self, mock_print):
        self.ops.process('UNKNOWN')
        mock_print.assert_called_with('Unknown operation.')

    @patch('builtins.input', return_value='0')
    @patch('builtins.print')
    def test_credit_zero(self, mock_print, mock_input):
        self.ops.process('CREDIT')
        mock_print.assert_called_with('Amount credited. New balance: 1000.00')

    @patch('builtins.input', return_value='0')
    @patch('builtins.print')
    def test_debit_zero(self, mock_print, mock_input):
        self.ops.process('DEBIT')
        mock_print.assert_called_with('Amount debited. New balance: 1000.00')

    @patch('builtins.input', return_value='1000')
    @patch('builtins.print')
    def test_debit_exact_balance(self, mock_print, mock_input):
        self.ops.process('DEBIT')
        mock_print.assert_called_with('Amount debited. New balance: 0.00')

    @patch('builtins.input', return_value='-100')
    @patch('builtins.print')
    def test_credit_negative(self, mock_print, mock_input):
        self.ops.process('CREDIT')
        mock_print.assert_called_with('Amount credited. New balance: 900.00')

    @patch('builtins.input', return_value='-100')
    @patch('builtins.print')
    def test_debit_negative(self, mock_print, mock_input):
        self.ops.process('DEBIT')
        mock_print.assert_called_with('Amount debited. New balance: 1100.00')

if __name__ == '__main__':
    unittest.main()
