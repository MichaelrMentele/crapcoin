import hashlib


class Transaction:
    """ This represents a payment from one address to another.

    In order to be a valid payment the following conditions must be true:
    1. output == input coinage
    2. hash of transaction data is signed by sender
    3. sender.balance >= 0
    """
    def __init__(self, payer, payee, input_amount, output_amount):
        self.payer = payer
        self.payee = payee
        self.input = input_amount
        self.output = output_amount
        self.data_hash = hashlib.sha256('f{self.payer}||{self.payee}||{self.input}||{self.output}')
        self.validate()
        self.signature = None

    def sign(self, private_key):
        self.signature = hashlib.sha256('f{self.data_hash}||{private_key}')

    def verify(self, public_key):
        """ Validates that the transaction was signed by the sender """
        pass
