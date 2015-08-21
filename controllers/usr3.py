# -*- coding: utf-8 -*-
def get_db():
		from gluon.dal import DAL
		return DAL('sqlite://storage.sqlite',auto_import=True)

def index():
	import re
	if request.vars['key'] != "fjnFF2rfaads32edfa#@":
		return "Error 504"
	else:
		usrr=request.vars['usr']
		emailid=request.vars['emailid']
		db=get_db()
		print "usr3: got vars and dB"
		rec=db.urstable(db.usrtable.emailid==emailid).select().update_record(usr=usrr)
		print "usr3: updating...1/1"
		print "usr3: update complete"
		return "set"
