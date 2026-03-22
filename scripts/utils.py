import logging
from typing import Dict, List

class Utils:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def validate_payment_method(self, method: str) -> bool:
        """
        Validate the payment method by checking if it's in the list of supported methods.
        """
        supported_methods = ['credit_card', 'paypal', 'bank_transfer']
        return method in supported_methods

    def calculate_taxes(self, amount: float, tax_rate: float) -> float:
        """
        Calculate the taxes for a given amount and tax rate.
        """
        return amount * tax_rate / 100

    def get_payment_success_response(self, payment_id: str) -> Dict:
        """
        Generate a payment success response.
        """
        return {'status': 'success', 'payment_id': payment_id}

    def get_payment_failure_response(self, error_message: str) -> Dict:
        """
        Generate a payment failure response.
        """
        return {'status': 'failure', 'error_message': error_message}

    def is_valid_credit_card_number(self, credit_card_number: str) -> bool:
        """
        Validate a credit card number using the Luhn algorithm.
        """
        digits = [int(d) for d in credit_card_number]
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        for d in even_digits:
            checksum += sum(int(d) for d in str(2 * d))
        for d in odd_digits:
            checksum += d
        return checksum % 10 == 0

def get_unique_ids(ids: List[str]) -> List[str]:
    """
    Remove duplicates from a list of IDs and return the unique IDs.
    """
    return list(set(ids))

def get_average_value(numbers: List[float]) -> float:
    """
    Calculate the average value of a list of numbers.
    """
    return sum(numbers) / len(numbers)