class PayPalTaxes(object):
    def __init__(self, percentage = None, inclusive: bool = None):

        self.percentage = percentage
        self.inclusive = str(inclusive).lower() if inclusive is not None else inclusive