# -*- coding: utf-8 -*-
class PayPalBillingCycleAmount(dict):

    def __init__(self, value: int = None, currency_code = None):
        self.value = value
        self.currency_code = currency_code

    def to_dict(self):
        return self.__dict__