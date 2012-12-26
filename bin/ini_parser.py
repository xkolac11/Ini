import ConfigParser #tohle je modul s funkcemi pro praci s ini, cfg, ... soubory

"""
Nevim, jestli je nutne udelat tridu a vsechny
metody do ni dat, nebo proste jenom
metody bez tridy.
"""

class parser:

	config = ConfigParser.RawConfigParser()

	def parse(self,file):
		config = self.config.read(file)
		
	def getPropertyValue(self,section,name):
		var = self.config.get(section,name)
		return var

  
#end of class parser