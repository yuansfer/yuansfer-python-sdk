# -*- coding: utf-8 -*-


from yuansfer.dto.recurring.PayPal_BillingCycle_Amount import PayPal_BillingCycle_Amount


class PayPal_BillingCycle_Frequency:
    def __init__(self, starting_quantity = None, ending_quantity = None, amount: PayPal_BillingCycle_Amount = None) -> None:
        self.amount = amount
        self.starting_quantity = starting_quantity
        self.ending_quantity = ending_quantity