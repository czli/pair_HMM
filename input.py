#!/usr/bin/python
"""
	The file is used to read the parameters from command line to set the global settings. In the future, we maybe allow using a setting file as an input.
"""
import sys
import os
import re
import settings

def readArgv(argv):

	intArguments = {
		'len': 'LENGTH',
	      'iter' : 'ITERATE',
	      'rep'  : 'REPLICATE'
	}
	floatArguments = {
		'l': 'LAMBDA',
		'e': 'EPSILON',
		'a': 'INDEL',
		'g': 'GAMMA',
		 't' : 'TIME',
	    'step' : 'STEP'
	}
	fileArguments = {
		'in' : 'IN_FILE',
		'out': 'OUT_FILE'
	}
	stringArguments = {
		'tree': 'TREE',
		'id' : 'ID',
		'm' : 'MODEL',
		'itype': 'IN_FORMAT'
	}
	boolArguments = {
		'acheck': 'ACHECK',
		'pcheck': 'PCHECK',
		'tcheck': 'TCHECK',
		'alignment': 'ALIGNMENT',
		'simul': 'SIMUL'}

	for x in range(1, len(argv)):
		key, value = argv[x].split("=",2)
		rValue = None

		if key in intArguments:
			settings.__dict__[intArguments[key]] = int(value)
		elif key in floatArguments:
			settings.__dict__[floatArguments[key]] = float(value)
		elif key in fileArguments:
			if "in" == key:
				if len(re.findall(r'/', value)):
					if not os.path.exists("./data/%s"%(value.split('/')[0])):
						os.system("mkdir ./data/%s"%(value.split('/')[0]))
					if None != settings.ID:
						settings.__dict__[fileArguments[key]] = '%s/data/%s_%s%s'%(settings.ROOT, os.path.splitext(value)[0], settings.ID, os.path.splitext(value)[1])
					else:
						settings.__dict__[fileArguments[key]] = '%s/data/%s'%(settings.ROOT, value)
				else:
					sDir = os.path.splitext(value)[0]
					if not os.path.exists("./data/%s"%(sDir)):
						os.system("mkdir ./data/%s"%(sDir))
					if None != settings.ID:
						settings.__dict__[fileArguments[key]]  = '%s/data/%s/%s_%s%s'%(settings.ROOT, sDir, os.path.splitext(value)[0], settings.ID, os.path.splitext(value)[1])
					else:
						settings.__dict__[fileArguments[key]]  = '%s/data/%s/%s'%(settings.ROOT, sDir, value)
			else:
				if not os.path.exists("./data/%s"%(value)):
					os.system("mkdir ./data/%s"%(value))
				settings.__dict__[fileArguments[key]] = '%s/data/%s/'%(settings.ROOT, value)
		elif key in stringArguments:
			settings.__dict__[stringArguments[key]] = value.strip()
		elif key in boolArguments:
			if 0 == int(value):
				settings.__dict__[boolArguments[key]] = False
			else:
				settings.__dict__[boolArguments[key]] = True

	if "phylip" == settings.IN_FORMAT:
		settings.REAL_TIME = float(re.search('_t(\d+\.?\d+)_', os.path.basename(settings.IN_FILE)).group(1))
				
