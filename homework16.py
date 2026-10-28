class NumberChecker:
    def check(self, number):
        if number > 0:
            return "Positive number"
        else:
            return "negative number"


checker = NumberChecker()

assert checker.check(5) == "Positive number"
assert checker.check(-3) == "negative number"
assert checker.check(-1) == "negative number"