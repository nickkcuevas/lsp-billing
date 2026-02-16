from datetime import date, timedelta
from app.licenses import MonthlyLicense, AnnualLicense, LifetimeLicense
from app.billing import bill_customer, bill_all


def test_monthly_license_billing():
    today = date.today()
    license = MonthlyLicense(start_date=today, monthly_fee=100.0)
    assert bill_customer(license, today) == 100.0


def test_annual_license_billing():
    today = date.today()
    license = AnnualLicense(start_date=today, annual_fee=1200.0)
    assert bill_customer(license, today) == 100.0  # 1200/12


def test_inactive_license_billing():
    today = date.today()
    future = today + timedelta(days=60)
    license = MonthlyLicense(start_date=today, monthly_fee=100.0)
    assert bill_customer(license, future) == 0.0


def test_bill_all():
    today = date.today()
    monthly = MonthlyLicense(start_date=today, monthly_fee=50.0)
    annual = AnnualLicense(start_date=today, annual_fee=600.0)

    total = bill_all([monthly, annual], today)
    assert total == 100.0  # 50 + 600/12