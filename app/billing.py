from datetime import date
from typing import List
from app.licenses import BillableLicense


def bill_customer(license: BillableLicense, billing_date: date) -> float:
    if not license.is_active(billing_date):
        return 0.0
    return license.calculate_fee()


def bill_all(licenses: List[BillableLicense], billing_date: date) -> float:
    total = 0.0
    for license in licenses:
        if license.is_active(billing_date):
            total += license.calculate_fee()
    return total