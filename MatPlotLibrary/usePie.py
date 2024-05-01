import matplotlib.pyplot as window

half = [35, 35, 20, 10]
oppenents = ["Real Madrid", "Bayern Munich", "Paris-Sant-German", "Brossua Dortmond"]
window.title("Champions Legue Winner(Guessing)", loc="left")
poping = [0.03,0.03,0.05,0.1]
window.pie(half, labels = oppenents, startangle=90, explode=poping, shadow=True)
window.legend(title="Teams:", loc="lower left")
window.show()