zakupy = {"mleko": "litry", "woda": "litry", "jablka": "sztuki",
          "cukier": "kilogramy", "gruszki": "sztuki", "cukierki": "sztuki"}

lista = {key: value for key, value in zakupy.items() if value == "sztuki"}
print(lista)
