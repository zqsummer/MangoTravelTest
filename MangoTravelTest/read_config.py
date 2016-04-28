import ConfigParser
import os

abs_path = os.path.split(os.path.realpath(__file__))[0]

class ReadConfig:
    def __init__(self):

        self.cf = ConfigParser.ConfigParser()
        self.cf.read(os.path.join(abs_path, "config.conf"))

    def get(self, d_name, s_name):
        value = self.cf.get(d_name, s_name)
        return value