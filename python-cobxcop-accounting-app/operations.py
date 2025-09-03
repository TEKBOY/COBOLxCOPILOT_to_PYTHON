print(">>> operation.py is loaded")  # debug au chargement

from data_program import DataProgram

class Operations:
    def __init__(self):
        self.data_program = DataProgram()

    def process(self, passed_operation):
        operation_type = passed_operation.strip().upper()
        print(f">>> Operations.process called with: {operation_type}")  # debug

        if operation_type == 'TOTAL':
            final_balance = self.data_program.process_operation('READ')
            print(f"Current balance: {final_balance:.2f}")

        elif operation_type == 'CREDIT':
            amount = float(input("Enter credit amount: "))
            final_balance = self.data_program.process_operation('READ')
            final_balance += amount
            self.data_program.process_operation('WRITE', final_balance)
            print(f"Amount credited. New balance: {final_balance:.2f}")

        elif operation_type == 'DEBIT':
            amount = float(input("Enter debit amount: "))
            final_balance = self.data_program.process_operation('READ')
            if final_balance >= amount:
                final_balance -= amount
                self.data_program.process_operation('WRITE', final_balance)
                print(f"Amount debited. New balance: {final_balance:.2f}")
            else:
                print("Insufficient funds for this debit.")
        else:
            print("Unknown operation.")