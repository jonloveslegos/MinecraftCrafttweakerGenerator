import sys
import os
import imp
generator = imp.load_source('module.name', os.getcwd()+"/generator/generator.py")