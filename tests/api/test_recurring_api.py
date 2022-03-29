# -*- coding: utf-8 -*-



import json

from tests.api.test_api_base import ApiTestBase
from yuansfer.dto.recurring.PayPal_BillingCycle import PayPal_BillingCycle
from yuansfer.dto.recurring.PayPal_BillingCycle_Amount import PayPal_BillingCycle_Amount
from yuansfer.dto.recurring.PayPal_BillingCycle_Frequency import PayPal_BillingCycle_Frequency
from yuansfer.dto.recurring.PayPal_BillingCycle_PricingScheme import PayPal_BillingCycle_PricingScheme
from yuansfer.dto.recurring.PayPal_PaymentPreferences import PayPal_PaymentPreferences
from yuansfer.dto.recurring.PayPal_PaymentPreferences_SetUpFee import PayPal_PaymentPreferences_SetUpFee
from yuansfer.dto.recurring.PayPal_ProductSchema import PayPal_ProductSchema
from yuansfer.dto.recurring.PayPal_Taxes import PayPal_Taxes

class RecurringApiTests(ApiTestBase):
    # Class to initialize Yuansfer configuration
    @classmethod
    def setUpClass(cls):
        super(RecurringApiTests, cls).setUpClass()

    # Make Recurring Payment request.
    def test_paypal_subscription(self):
        # Parameters for the API call
        params = {
            "clientId": "AXV4uwyZ5WY9zpYs7zaLrnPcHX4s9AA0VdxEX2mo23UTqmVl_aH7V_p0Nguv5sdIB2u3osE40hqIbE7U",
            "secret": "EEYTIteecQSLblfkiZ6uGFe__Zmoy86uLo4T6Y9fst5m834kY09P3Lhsy4qGRccdLgQXI9AHqudMIoWl",
            'amount': "100",
            "productName": "descriptive name for product test",
            "planName": "descriptive name for plan test",
            "planDescription": "detailed description for plan",
            "requestIdProduct": "unique Id for create product request",
            "requestIdPlan": "unique Id for create plan request",
            "frequency": "MONTH",
            "billingCycles": json.dumps([
                PayPal_BillingCycle(
                    pricing_scheme=PayPal_BillingCycle_PricingScheme(
                        fixed_price= PayPal_BillingCycle_Amount(value="20", currency_code="USD").__dict__
                    ).__dict__,
                    frequency= PayPal_BillingCycle_Frequency(interval_count= 1, interval_unit="MONTH").__dict__,
                    tenure_type="REGULAR",
                    sequence=1,
                    total_cycles=999
                ).__dict__]
            ),
            "paymentPreferences": json.dumps(
                PayPal_PaymentPreferences(
                    auto_bill_outstanding=True,
                    setup_fee=PayPal_PaymentPreferences_SetUpFee(value=20, currency_code="USD").__dict__,
                    setup_fee_failure_action="CONTINUE",
                    Payment_failure_threshold=3
                ).__dict__
            ),
            "taxes": json.dumps(
                PayPal_Taxes(percentage="10",inclusive=True).__dict__
            ),
            "productSchema": json.dumps(PayPal_ProductSchema(type ="SERVICE", category="SOFTWARE").__dict__)
        }

        # Perfo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    rm the API call through the SDK function
        response = self.client.recurring.paypal_subscription(params)
        data = response.body
        # Test response code
        self.assertEqual(data['ret_code'], '000100')

unittest = RecurringApiTests()
unittest.setUpClass()
unittest.test_paypal_subscription()
# unittest.test_pay()
# unittest.test_inquiry()