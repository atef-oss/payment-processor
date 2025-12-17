from datetime import datetime
from typing import Dict, List

class PaymentProcessor:
    def __init__(self):
        self.paid_transactions = {}
        self.verified_transactions = {}

    def add_payment(self, payer: str, amount: float, payment_method: str):
        transaction_id = str(datetime.now())
        self.paid_transactions[transaction_id] = {
            "payer": payer,
            "amount": amount,
            "payment_method": payment_method,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return transaction_id

    def verify_payment(self, transaction_id: str, signature: str):
        if transaction_id in self.paid_transactions and self.paid_transactions[transaction_id]["signature"] == signature:
            self.verified_transactions[transaction_id] = self.paid_transactions[transaction_id]
            del self.paid_transactions[transaction_id]
            return True
        return False

    def get_verified_payments(self) -> List[Dict]:
        return list(self.verified_transactions.values())

def process_payment(payer: str, amount: float, payment_method: str, signature: str) -> str:
    processor = PaymentProcessor()
    transaction_id = processor.add_payment(payer, amount, payment_method)
    result = processor.verify_payment(transaction_id, signature)
    if result:
        print(f"Payment with ID {transaction_id} has been verified.")
    else:
        print(f"Payment with ID {transaction_id} has been rejected.")

# Example usage
if __name__ == "__main__":
    process_payment("John Doe", 100.0, "Credit Card", "abc123")