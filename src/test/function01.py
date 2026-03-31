# 税込価格を求める関数
rate = 0.1


def tax(total):
    return int(total * rate)


def tax_amount(total):
    return int(total * (1 + rate))


print('税額{}円'.format(tax(100)))
print('税込金額{}円'.format(tax_amount(100)))
