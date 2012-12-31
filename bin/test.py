import ini_parser

file = "test.ini"
section = "Files"
name = "two"

required = {'Files':['one', 'two']}

#testovani
obj = ini_parser.parser()
obj.parse(file)
var = obj.getValueAsFloat(section,name)
print var

obj.loadConfiguration(file,required)
