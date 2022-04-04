# Yuansfer Python SDK

[Yuansfer API](https://docs.yuansfer.com/)

## Requirements

The SDK supports the following versions of Python:
* Python 3 versions 3.4 and later

## Installation

Install the latest SDK using pip:

```sh
pip install yuansfer==3.0.2.0
```

## Usage

First time with Yuansfer? Here’s how to get started:

1. **Create a Yuansfer Sandbox account.** If you don’t have one already, [sign up for a sandbox account](https://yuansfer.github.io/yuansfer-sandbox-application/?language=english).

Now let’s call your first Yuansfer API. Create a python new file, and copy the following code into that file:

```python
from yuansfer.client import Client

# Create an instance of the API Client
# and initialize it with the sandbox credentials
client = Client(
    environment='sandbox',
    merchantNo='{{REPLACE_MERCHANT_NUMBER}}',
    storeNo='{{REPLACE_STORE_NUMBER}}',
    token='{{REPLACE_TOKEN}}'
)

### 1. Online API

# Get an instance of the Yuansfer Online API you want call
api_online = client.online
# Set request payload
params = {
    'amount':'0.01',
    'currency':'USD',
    'settleCurrency':'USD',
    'vendor':'alipay',
    'terminal':'ONLINE',
    'reference': datetime.now,
    'ipnUrl':"http://zk-tys.yunkeguan.com/ttest/test",
    'callbackUrl':"http://zk-tys.yunkeguan.com/ttest/test",
    'description':'descrip',
    'note':'note'
}
# Make a Yuansfer Secure Pay request
result = api_online.secure_pay(params)
# Call the success method to see if the call succeeded
if result.is_success():
    # Check if the request is successful
    if result.body['ret_code'] == '000100':
        # The body property is the resposne from Yuansfer
        yuansferResponse = result.body['result']
        print(yuansferResponse)
    else:
        print(result.body['ret_msg'])
# Call the error method to see if the call failed
elif result.is_error():
    print('Error calling OnlineApi.SecurePay')
    errors = result.errors
    # An error is returned as a list of errors
    for error in errors:
    	# Each error is represented as a dictionary
        for key, value in error.items():
            print(f"{key} : {value}")
        print("\n")

### 2. Offline API

# Get an instance of the Yuansfer Offline API you want call
api_offline = client.offline
# Set request payload
params = {
    'amount':'0.01',
    'currency':'USD',
    'settleCurrency':'USD',
    'reference': datetime.now
}
# Make a Yuansfer Instore Create Transaction QR Code request
result = offline.instore_create_tran_qrcode(params)
# Call the success method to see if the call succeeded
if result.is_success():
    # Check if the request is successful
    if result.body['ret_code'] == '000100':
        # The body property is the resposne from Yuansfer
        yuansferResponse = result.body['result']
        print(yuansferResponse)
    else:
        print(result.body['ret_msg'])
# Call the error method to see if the call failed
elif result.is_error():
    print('Error calling OfflineApi.InstoreCreateTranQrcode')
    errors = result.errors
    # An error is returned as a list of errors
    for error in errors:
    	# Each error is represented as a dictionary
        for key, value in error.items():
            print(f"{key} : {value}")
        print("\n")

### 3. Mobile API

# Get an instance of the Yuansfer Mobile API you want call
api_mobile = client.mobile
# Set request payload
params = {
    'amount':'0.01',
    'currency':'USD',
    'settleCurrency':'USD',
    'reference': datetime.now,
    'vendor':'alipay',
    'terminal':'APP'
}
# Make a Yuansfer Mobile Prepay request
result = api_mobile.mobile_prepay(params)
# Call the success method to see if the call succeeded
if result.is_success():
    # Check if the request is successful
    if result.body['ret_code'] == '000100':
        # The body property is the resposne from Yuansfer
        yuansferResponse = result.body['result']
        print(yuansferResponse)
    else:
        print(result.body['ret_msg'])
# Call the error method to see if the call failed
elif result.is_error():
    print('Error calling MobileApi.MobilePrepay')
    errors = result.errors
    # An error is returned as a list of errors
    for error in errors:
    	# Each error is represented as a dictionary
        for key, value in error.items():
            print(f"{key} : {value}")
        print("\n")

### 4. Data Search API

# Get an instance of the Yuansfer Data Search API you want call
api_data_search = client.data_search
# Set request payload
params = {
    "transactionNo": "297553638301777927"
}
# Make a Yuansfer Transaction Query request
result = api_data_search.tran_query(params)
# Call the success method to see if the call succeeded
if result.is_success():
    # Check if the request is successful
    if result.body['ret_code'] == '000100':
        # The body property is the resposne from Yuansfer
        yuansferResponse = result.body['result']
        print(yuansferResponse)
    else:
        print(result.body['ret_msg'])
# Call the error method to see if the call failed
elif result.is_error():
    print('Error calling DataSearchApi.TranQuery')
    errors = result.errors
    # An error is returned as a list of errors
    for error in errors:
    	# Each error is represented as a dictionary
        for key, value in error.items():
            print(f"{key} : {value}")
        print("\n")

### 5. PayPal Subscription API

# Get an instance of the Pockyt Data Search API you want call
api_recurring = client.recurring

## Set request payload
# Declare PayPal Billing Cycle Object
params = {
    "clientId": "<PayPalClientID>",
    "secret": "<PayPalSecretID>",
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
                fixed_price= PayPalBillingCycleAmount(value="20", currency_code="USD").to_dict()
            ).to_dict(),
            frequency= PayPalBillingCycleFrequency(interval_count= 1, interval_unit="MONTH").to_dict(),
            tenure_type="REGULAR",
            sequence=1,
            total_cycles=999
        ).to_dict()]
    ),
    "paymentPreferences": json.dumps(
        PayPalPaymentPreferences(
            auto_bill_outstanding=True,
            setup_fee=PayPalPaymentPreferencesSetUpFee(value=20, currency_code="USD").to_dict(),
            setup_fee_failure_action="CONTINUE",
            payment_failure_threshold=3
        ).to_dict()
    ),
    "taxes": json.dumps(
        PayPalTaxes(percentage="10",inclusive=True).to_dict()
    ),
    "productSchema": json.dumps(PayPalProductSchema(type ="SERVICE", category="SOFTWARE").to_dict())
}
# Make a Pockyt PayPal Subscription request
result = api_recurring.paypal_subscription(params)
# Call the success method to see if the call succeeded
if result.is_success():
    # Check if the request is successful
    if result.body['ret_code'] == '000100':
        # The body property is the response from Pockyt
        yuansferResponse = result.body['result']
        print(yuansferResponse)
    else:
        print(result.body['ret_msg'])
# Call the error method to see if the call failed
elif result.is_error():
    print('Error calling RecurringApi.PayPal_Subscription')
    errors = result.errors
    # An error is returned as a list of errors
    for error in errors:
    	# Each error is represented as a dictionary
        for key, value in error.items():
            print(f"{key} : {value}")
        print("\n")
