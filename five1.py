Data = "Toys are made from different types of plastic and wood"

st_in_upper = (Data.upper())
print(st_in_upper)

st_in_lower = (Data.lower())
print(st_in_lower)

st_in_title = (Data.title())
print(st_in_title)

st_in_capitalize =(Data.capitalize())
print(st_in_capitalize)

split_out = (Data.split())
print(split_out)

split_output = (Data.split("of"))
print(split_output)

join_output = " ".join(Data.split())
print(join_output)

join_out = "-".join(Data.split())
print(join_out)

find_out = (Data.find("wood"))
print(find_out)

statement = "Chocolate come moulds come in various materials come"
outputs = statement.find("come")
print(outputs)
out_find =statement.rfind("come")
print(out_find)
out_finds =statement.rfind("do")
print(out_finds)
out_finds =statement.index("do")
print(out_finds)








