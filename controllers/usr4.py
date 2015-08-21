def get_db():
	from gluon.dal import DAL
	return DAL('sqlite://storage.sqlite',auto_import=True)

def index():
	import re
	if request.vars['emailId'] == None:
		return "Error 504"
	else:
		print "inside main body"
		email=request.vars['emailId']
		print "Got vars"
		db=get_db()
		print "Got dB and Vars"
		flag=0
		urs=""
		for row in db().select(db.usrtable.ALL):
			print "inside for"
			if re.match(row.emailid,email,re.IGNORECASE):
				print "Found Match!"
				usr=row.usrname
				flag=1
				break
		if flag==1:
			print flag
			return usr
		else:
			print flag
			return "Error"
