print(">>> data_program.py is loaded")  # debug au chargement

class DataProgram:
    def __init__(self):
        self.storage_balance = 1000.00
        print(f">>> Initial balance set to {self.storage_balance}")  # debug

    def reset_balance(self):
        self.storage_balance = 1000.00

    def process_operation(self, passed_operation, balance=None):
        operation_type = passed_operation.strip().upper()
        print(f">>> Processing operation: {operation_type}")  # debug

        if operation_type == 'READ':
            return self.storage_balance
        elif operation_type == 'WRITE' and balance is not None:
            self.storage_balance = balance
            print(f">>> Balance updated to {self.storage_balance}")  # debug
            return self.storage_balance
        else:
            raise ValueError("Invalid operation or missing balance for WRITE.")