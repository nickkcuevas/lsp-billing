from abc import ABC, abstractmethod
from datetime import date, timedelta


# ============================================
# Contracts
# ============================================

class BillableLicense(ABC):
    @abstractmethod
    def calculate_fee(self) -> float:
        pass

    @abstractmethod
    def is_active(self, on_date: date) -> bool:
        pass


class NonBillableLicense(ABC):
    @abstractmethod
    def is_active(self, on_date: date) -> bool:
        pass


# ============================================
# Implementations
# ============================================

class MonthlyLicense(BillableLicense):
    def __init__(self, start_date: date, monthly_fee: float):
        self.start_date = start_date
        self.monthly_fee = monthly_fee

    def calculate_fee(self) -> float:
        return self.monthly_fee

    def is_active(self, on_date: date) -> bool:
        return self.start_date <= on_date < (self.start_date + timedelta(days=30))


class AnnualLicense(BillableLicense):
    def __init__(self, start_date: date, annual_fee: float):
        self.start_date = start_date
        self.annual_fee = annual_fee

    def calculate_fee(self) -> float:
        # Annual fee, billed monthly equivalent for demo
        return self.annual_fee / 12.0

    def is_active(self, on_date: date) -> bool:
        return self.start_date <= on_date < (self.start_date + timedelta(days=365))


class LifetimeLicense(NonBillableLicense):
    def __init__(self, start_date: date):
        self.start_date = start_date

    def is_active(self, on_date: date) -> bool:
        return on_date >= self.start_date