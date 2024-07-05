import json
#1
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
json_data=json.dumps(data)
print(json_data)
#2
talaba_json = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
print(talaba_json["ism"])
print(talaba_json["familiya"])
#3
with open("data.json","w") as file:
  json.dump(data,file)
with open("talaba.json","w") as file:
  json.dump(talaba_json,file)
#4
with open("student.json") as f:
    talaba=json.load(f)
for i in range(3):
    print(f"{talaba['student'][i]['name']} {talaba['student'][i]['lastname']},{talaba['student'][i]['year']}-kurs,{talaba['student'][i]['faculty']}-fakulteti talabasi")