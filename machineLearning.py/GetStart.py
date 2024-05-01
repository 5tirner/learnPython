import numpy
import scipy.stats as st
data = [437,4375,435784,436754,45678954,5467854,54678,43657,46357, 435784]
# To Exrtact The Average Value We Use Mean Method From numpy
average = numpy.mean(data)
print(f"The Average Value In Data {type(average)} -> {average}")
# To Exrtact The Median We Use Midian Method From numpy
mid = numpy.median(data)
print(f"The Middle Number In Data {type(mid)} -> {mid}")
# To Extract The Most Common Value We Use mode method From scipy.stats
mc = st.mode(data)
print(f"The Most Common Value In Data {type(mc)} -> {mc}")
print(mc.mode)