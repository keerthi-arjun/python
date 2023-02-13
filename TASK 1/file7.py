var1 = "a string to camelcase"
var2="a string to uppercase"
var3="camelcase to snakecase"

res=var1[0].lower() + var1.title()[1:].replace("_","")
print(res)
res1=var2.upper()
print(res1)

