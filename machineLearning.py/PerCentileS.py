import numpy
import scipy.stats as st
import math

# Percenties Used in Statistic To describe A Value That Represent The pErcentage Of Part From Statistic
# We Can Extract The Percentiles Using percentile method from numpy

price = [34,24,23,756,36,248,3246,24,63,46,346,234,13,434,523,54245,57]
percnt0 = numpy.percentile(price, 0)
percnt1 = numpy.percentile(price, 10)
percnt2 = numpy.percentile(price, 20)
percnt3 = numpy.percentile(price, 30)
percnt4 = numpy.percentile(price, 40)
percnt5 = numpy.percentile(price, 50)
percnt6 = numpy.percentile(price, 60)
percnt7 = numpy.percentile(price, 70)
percnt8 = numpy.percentile(price, 80)
percnt9 = numpy.percentile(price, 90)
percnt10 = numpy.percentile(price, 100)
print("0% Of Price Is Less Or Equal To", percnt0)
print("10% Of Price Is Less Or Equal To", percnt1)
print("20% Of Price Is Less Or Equal To", percnt2)
print("30% Of Price Is Less Or Equal To", percnt3)
print("40% Of Price Is Less Or Equal To", percnt4)
print("50% Of Price Is Less Or Equal To", percnt5)
print("60% Of Price Is Less Or Equal To", percnt6)
print("70% Of Price Is Less Or Equal To", percnt7)
print("80% Of Price Is Less Or Equal To", percnt8)
print("90% Of Price Is Less Or Equal To", percnt9)
print("100% Of Price Is Less Or Equal To", percnt10)