# -*- coding: utf-8 -*-



import json
from msilib.schema import Billboard

from tests.api.test_api_base import ApiTestBase
from yuansfer.dto.recurring.paypal_billingcycle import PayPalBillingCycle
from yuansfer.dto.recurring.paypal_billingcycle_amount import PayPalBillingCycleAmount
from yuansfer.dto.recurring.paypal_billingcycle_frequency import PayPalBillingCycleFrequency
from yuansfer.dto.recurring.paypal_billingcycle_pricingscheme import PayPalBillingCyclePricingScheme
from yuansfer.dto.recurring.paypal_paymentpreferences import PayPalPaymentPreferences
from yuansfer.dto.recurring.paypal_paymentpreferences_setupfee import PayPalPaymentPreferencesSetUpFee
from yuansfer.dto.recurring.paypal_productschema import PayPalProductSchema
from yuansfer.dto.recurring.paypal_taxes import PayPalTaxes

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
                PayPalBillingCycle(
                    pricing_scheme=PayPalBillingCyclePricingScheme(
                        fixed_price= PayPalBillingCycleAmount(value="20", currency_code="USD").__dict__
                    ).__dict__,
                    frequency= PayPalBillingCycleFrequency(interval_count= 1, interval_unit="MONTH").__dict__,
                    tenure_type="REGULAR",
                    sequence=1,
                    total_cycles=999
                ).__dict__]
            ),
            "paymentPreferences": json.dumps(
                PayPalPaymentPreferences(
                    auto_bill_outstanding=True,
                    setup_fee=PayPalPaymentPreferencesSetUpFee(value=20, currency_code="USD").__dict__,
                    setup_fee_failure_action="CONTINUE",
                    Payment_failure_threshold=3
                ).__dict__
            ),
            "taxes": json.dumps(
                PayPalTaxes(percentage="10",inclusive=True).__dict__
            ),
            "productSchema": json.dumps(PayPalProductSchema(type ="SERVICE", category="SOFTWARE").__dict__)
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