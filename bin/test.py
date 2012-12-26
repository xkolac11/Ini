import ini_parser

file = "test.ini"
section = "Files"
name = "two"

#testovani
obj = ini_parser.parser()
obj.parse(file)
var = obj.getPropertyValue(section,name)
print var