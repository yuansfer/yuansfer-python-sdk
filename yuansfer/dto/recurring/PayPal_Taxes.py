class PayPal_Taxes:
    def __init__(self, percentage = None, inclusive: bool = None) -> None:

        self.percentage = percentage
        self.inclusive = str(inclusive).lower() if inclusive is not None else inclusive