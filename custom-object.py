amount=100.0
taxPercent=7.5
tipPercent=20.0
class Purchase(object):
    def _init_(person, amount):
        amount=self_amount
    def calculateTax(amount, taxPercent):
        return amount * taxPercent/100.0
    def calculateTip(amount, tipPercent):
        return amount * tipPercent/100.0
    def calculateTotal(amount, taxPercent, tipPercent):
        return amount * (1+ taxPercent/100.0 + tipPercent/100.0)
tax=Purchase.calculateTax(100.0, 7.5)
tip=Purchase.calculateTip(100.0, 20.0)
total=Purchase.calculateTotal(100.0, 7.5, 20.0)
print('Tax', tax)
print('Tip', tip)
print('Total', total)
