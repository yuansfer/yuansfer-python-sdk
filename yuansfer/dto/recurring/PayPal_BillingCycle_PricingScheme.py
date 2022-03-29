
from yuansfer.dto.recurring.PayPal_BillingCycle_Amount import PayPal_BillingCycle_Amount
from yuansfer.dto.recurring.PayPal_BillingCycle_Frequency import PayPal_BillingCycle_Frequency


class PayPal_BillingCycle_PricingScheme:
    def __init__(self, version: int = None, fixed_price: PayPal_BillingCycle_Amount = None, pricing_model = None, tiers: PayPal_BillingCycle_Frequency = None, update_time = None, create_time = None) -> None:
        self.version = version
        self.fixed_price = fixed_price
        self.pricing_model = pricing_model
        self.tiers = tiers
        self.update_time = update_time
        self.create_time = create_time