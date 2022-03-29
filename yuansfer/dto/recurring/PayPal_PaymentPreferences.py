from yuansfer.dto.recurring.PayPal_PaymentPreferences_SetUpFee import PayPal_PaymentPreferences_SetUpFee

class PayPal_PaymentPreferences:
    def __init__(self, auto_bill_outstanding: bool = None, setup_fee: PayPal_PaymentPreferences_SetUpFee = None,
    setup_fee_failure_action = None, Payment_failure_threshold: int = None) -> None:
        self.auto_bill_outstanding = str(auto_bill_outstanding).lower() if auto_bill_outstanding is not None else auto_bill_outstanding
        self.setup_fee = setup_fee
        self.setup_fee_failure_action = setup_fee_failure_action
        self.Payment_failure_threshold = Payment_failure_threshold