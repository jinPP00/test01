with open("sample.txt", mode="r", encoding="utf-8") as s:
  mycontnet = s.read()
print(mycontnet)


with open("./data/sample.txt", mode="r", encoding="utf-8") as s:
  mycontnet = s.read()
print(mycontnet)
