# -*- coding: utf-8 -*-

class PayPal_BillingCycle_Frequency:
    def __init__(self, interval_unit = None, interval_count: int = None) -> None:
        self.interval_unit = interval_unit
        self.interval_count = interval_count