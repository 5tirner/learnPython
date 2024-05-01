import numpy
import scipy.stats as st
import math
# Standar Deviation Is Value That Describe If Our Data Is Close To Each Other Or Not
# If The Standart Deviation Is In A Low Range Thats Mean Our Data Is Clode To The Average Value
# Else It Mean Not
# To Extract The Standart Deviation We Use std method from numpy
results = [11, 2, 19]
standartDeviationOFResults = numpy.std(results)
print(standartDeviationOFResults, type(standartDeviationOFResults))
# We Can Also Clacul The Standart Deviation From The Variance Value By Get The square Root Of The Variance
# We Can Calculate Variance Using var Methon in numpy
varianceOfResult = numpy.var(results)
print(varianceOfResult, type(varianceOfResult))
print(math.sqrt(varianceOfResult))

#Standard Deviation is often represented by the symbol Sigma: σ
# Variance is often represented by the symbol Sigma Squared: σ2