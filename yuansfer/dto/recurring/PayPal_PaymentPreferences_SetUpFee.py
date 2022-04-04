# -*- coding: utf-8 -*-
class PayPalPaymentPreferencesSetUpFee(dict):
    def __init__(self, value = None, currency_code = None):
        self.value = value
        self.currency_code = currency_code

    def to_dict(self):
        return self.__dict__