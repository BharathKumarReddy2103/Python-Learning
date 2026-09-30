from numeric_utils import is_prime, sum_of_multiples_of_3_or_5


def check_prime():
    print(is_prime(7) == True)  # Expected output: True
    print(is_prime(70) == False)  # Expected output: False
    print(is_prime(1) == False)  # Expected output: False

def check_sum_of_multiples():
    print(f"Sum of multiples of 3 or 5(1, 1000): {sum_of_multiples_of_3_or_5(1, 1000)}")  # Expected output: 233168


if __name__ == "__main__":
    #check_prime()
    # check_sum_of_multiples()
    # calling args by name
    # sum_of_multiples_of_3_or_5(start=1, end=1000)
    # sum_of_multiples_of_3_or_5(end=1000)
    # sum_of_multiples_of_3_or_5(1000)