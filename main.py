from datetime import date
from app.licenses import MonthlyLicense, AnnualLicense, LifetimeLicense
from app.billing import bill_customer, bill_all


def main():
    today = date.today()

    monthly = MonthlyLicense(start_date=today, monthly_fee=50.0)
    annual = AnnualLicense(start_date=today, annual_fee=600.0)
    lifetime = LifetimeLicense(start_date=today)

    # ✅ Billable licenses only
    total = bill_all([monthly, annual], today)
    print(f"Total billed today: ${total:.2f}")

    # ❌ This would be incorrect:
    # bill_customer(lifetime, today)
    # because LifetimeLicense is NonBillable and does not implement BillableLicense

    print("Lifetime license is active but not billable.")


if __name__ == "__main__":
    main()
