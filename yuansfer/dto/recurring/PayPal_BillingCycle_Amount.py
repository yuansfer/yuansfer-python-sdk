# -*- coding: utf-8 -*-

class PayPalBillingCycleAmount(object):

    def __init__(self, value: int = None, currency_code = None):
        self.value = value
        self.currency_code = currency_code