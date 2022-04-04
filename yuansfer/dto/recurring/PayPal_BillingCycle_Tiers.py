# -*- coding: utf-8 -*-
from yuansfer.dto.recurring.paypal_billingcycle_amount import PayPalBillingCycleAmount

class PayPalBillingCycleTiers(dict):
    def __init__(self, starting_quantity = None, ending_quantity = None, amount: PayPalBillingCycleAmount = None):
        self.amount = amount
        self.starting_quantity = starting_quantity
        self.ending_quantity = ending_quantity

    def to_dict(self):
        return self.__dict__