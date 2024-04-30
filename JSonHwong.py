import json

# Json Is A Syntax For Storing And Exchanging Data
# Also Json Is A Txt Written With Js Object Notation

# JSON
x = '{"Name": "user1","Username": "allah","Abilities": "ALL","Status": "CEO","Clothes": "Sirvite Alegator Kalso Dyal Lahdid"}'

# Parse Json-> x
save = json.loads(x)
print(save)
# Json To String
castSave = str(save)
save1 = json.dumps(save)
print(save1)
print(castSave)

Indent = json.dumps(save, indent=10)
print(Indent)

Sort = json.dumps(save, indent=10, sort_keys=True)
print(Sort)