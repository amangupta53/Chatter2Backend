def get_db():
		from gluon.dal import DAL
		dbpath = '/home/Downloads/web2py/applications/sserv/databases/'
		return DAL('sqlite://storage.sqlite',auto_import=True)

def index():
		import re
		if request.vars['emailid']==None  :
			return "Errata!"
		else:
			usrr=request.vars['usr']
			idd=request.vars['emailid']
			print "got vars"
			db=get_db()
			flagid=0
			print "got db"
			dbobj = db.usrtable
			usrs = dbobj.usrname
			q = usrs != None
			s = db(q)
			rows = s.select()
			print "selected"
			for row in rows:
				if re.match(row.emailid,idd):
					flagid=1
					print "Email matched"
					index=row.id
			print flagid
			if flagid==1:
				print "inside if 1/3"
				db(db.usrtable._id==index).delete()
				print "inside if 2/3"
				db.usrtable.insert(usrname=usrr,emailid=idd)
				print "inside if 3/3"
				return "set"
			else:
				return "Error"
