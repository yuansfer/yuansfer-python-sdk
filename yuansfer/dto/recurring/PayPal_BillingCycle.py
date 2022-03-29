# -*- coding: utf-8 -*-

from yuansfer.dto.recurring.PayPal_BillingCycle_Frequency import PayPal_BillingCycle_Frequency
from yuansfer.dto.recurring.PayPal_BillingCycle_PricingScheme import PayPal_BillingCycle_PricingScheme


class PayPal_BillingCycle:
    def __init__(self, pricing_scheme: PayPal_BillingCycle_PricingScheme = None, frequency: PayPal_BillingCycle_Frequency = None,
    tenure_type = None, sequence: int = None, total_cycles: int = None) -> None:
        self.pricing_scheme = pricing_scheme
        self.frequency = frequency
        self.tenure_type = tenure_type
        self.sequence = sequence
        self.total_cycles = total_cycles