#merubah tipe data integer ke tipe data lain
print("=====DATA INTEGER=====")
data_integer = 10
print( "data = ", data_integer, ", type = ", type(data_integer))
print("")

data_string = str(data_integer)
print( "data = ", data_string, ", type = ", type(data_string))
data_float = float(data_integer)
print( "data = ", data_float, ", type = ", type(data_float))
data_boolean = bool(data_integer)
print( "data = ", data_boolean, ", type = ", type(data_boolean))

print("")
print("")
print("=====DATA FLOAT=====")
data_float = 10.5
print( "data = ", data_float, ", type = ", type(data_float))
print("")

data_string = str(data_float)
print( "data = ", data_string, ", type = ", type(data_string))
data_integer = float(data_float)
print( "data = ", data_integer, ", type = ", type(data_integer))
data_boolean = bool(data_float)
print( "data = ", data_boolean, ", type = ", type(data_boolean))
