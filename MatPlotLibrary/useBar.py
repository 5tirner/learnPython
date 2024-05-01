import matplotlib.pyplot as graph

graph.title("Top Greatest Five Films All Time", loc="left")
graph.xlabel("Film Name")
graph.ylabel("Rate")
x = ["The\nShawshank\nRedemption", "The Godfather", "The Dark\nKnight", " The\nGodfather Part2", "12 Angry\nMen"]
y = [10, 9.7, 9.4, 9.1, 8.98]
graph.bar(x, y, color='k', width=0.3)
graph.show()