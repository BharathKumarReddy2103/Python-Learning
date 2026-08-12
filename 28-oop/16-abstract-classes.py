from abc import ABC, abstractmethod


class PaymentProvider(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class StripePayment(PaymentProvider):

    def process_payment(self, amount):
        print(f"Processing ₹{amount} payment using Stripe")


class RazorpayPayment(PaymentProvider):

    def process_payment(self, amount):
        print(f"Processing ₹{amount} payment using Razorpay")


stripe = StripePayment()
razorpay = RazorpayPayment()

stripe.process_payment(1000)
razorpay.process_payment(2000)