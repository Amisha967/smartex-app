# import re

# def parse_sms(text):
#     amount_match = re.search(r'INR|Rs\.?\s?([\d,]+\.\d+)', text)
#     merchant_match = re.search(r'at\s+([A-Za-z0-9\s&]+)', text)
#     transaction_type = "Credit" if "credited" in text.lower() else "Debit"

#     return {
#         "amount": amount_match.group(1) if amount_match else None,
#         "merchant": merchant_match.group(1) if merchant_match else None,
#         "type": transaction_type
#     }
import re

def parse_sms(text):
    if not isinstance(text, str):
        return {"amount": None, "type": None}

    amount_match = re.search(r'(?:INR|Rs\.?)\s?([\d,]+\.\d+)', text)
    txn_type = None
    if "debited" in text.lower():
        txn_type = "debit"
    elif "credited" in text.lower():
        txn_type = "credit"

    return {
        "amount": amount_match.group(1) if amount_match else None,
        "type": txn_type
    }