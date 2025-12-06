from typing import Protocol, Literal

# Allowed payment types
PayType = Literal["CASH", "CARD", "PHONE"]

class Payable(Protocol):
    def get_pay_type(self) -> PayType:
        ...

    def set_pay_type(self, payment_method: PayType) -> None:
        ...
