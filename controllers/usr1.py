# -*- coding: utf-8 -*-
def get_db():
		from gluon.dal import DAL
		return DAL('sqlite://storage.sqlite',auto_import=True)

def index():
	import re
	if request.vars['key'] != "fjnFF2rfaads32edfa#@":
		return "Error 504"
	else:
		topic=request.vars['topic']
		sub=request.vars['sub']
		descp=request.vars['descp']
		loc=request.vars['loc']
		file_dets=request.vars['uploadfile']
		name=request.vars['name']
		add=request.vars['add']
		phno=request.vars['phno']
		emailidd=request.vars['emailid']
		datentime=request.vars['datentime']
		print "reciever1: got vars"
		db=get_db()
		print "reciever1: got db"
		print "reciever1: inserting vars in table"
		db.FIRapp.insert()
		return "set"
