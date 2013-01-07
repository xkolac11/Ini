
import ConfigParser 

class parser:

	config = ConfigParser.ConfigParser()

	def parse(self,file):
		config = self.config.read(file)
		
	def getPropertyValue(self, section, name):
		return self.config.get(section,name)
		
	def getValueAsInt(self, section, name):
		return self.config.getint(section,name)
		
	def getValueAsFloat(self, section, name):
		return self.config.getfloat(section,name)
		
	def getValueAsBoolean(self, section, name):
		return self.config.getboolean(section,name)
		
	def loadConfiguration(self, filepath, requiredconfig):
		config = self.config.read(filepath)
		k = requiredconfig.keys()
		
		for section in k:
			sec_exists = self.config.has_section(section)
			if sec_exists == False:
				raise ConfigParser.NoSectionError
			
			for names in requiredconfig[section]:
				name_exists = self.config.has_option(section,names)
				if name_exists == False:
					raise ConfigParser.NoOptionError(names,section)
		

#end of class parser