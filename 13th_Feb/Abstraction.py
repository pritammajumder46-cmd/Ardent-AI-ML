# ABSTRACTION : WHERE THE MAIN LOGIC IS HIDDEN IN CODE ONLY NECEESSORY  CODE DETAILS ARE 

# parent class (abstraction)

class Payment:
    def pay(self, amount):
        pass
# Card Payment
class CardPayment(Payment):
    def pay(self,amount):
        self._validate_card()
        self._check_balance(amount)
        self._connect_bank()
        self.deduct_amount(amount)
        self._show_success()
# Hidden from user
    def _validate_card(self):
        print("Validatibg Card....")
    def _check_balance(self,amount):
        print("Checking Card Balance")
    def _connect_bank(self):
        print("Connecting to bank Server")
    def _deduct_amount(self):
        print("RS", amount, "Deducted from card")
    def _show_success(self):
        print("Card Payment Successful")

# UPI PAYMENT
class UPIPayment(Payment):
    def pay(self,amount):
        self._verifify_upi()
        self._check_balance(amount)
        self._sen