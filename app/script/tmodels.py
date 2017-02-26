# -*- coding: utf-8 -*-
from flask import Flask
from datetime import *
import random
from sqlalchemy import or_
from sqlalchemy import and_
from sqlalchemy import text
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:SEUqianshou2015@218.244.147.240:3306/flasktestdb?charset=utf8"
#app.config['SQLALCHEMY_DATABASE_URI']="mysql://liewli:liewli@localhost:3306/weme?charset=utf8"
#app.config['SQLALCHEMY_DATABASE_URI']="mysql://ZRR:zrr520@223.3.56.153:3306/flasktestdb?charset=utf8"
#app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:root@localhost:3306/flasktestdb?charset=utf8"
#app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:0596@223.3.36.246:3306/flasktestdb?charset=utf8"
db = SQLAlchemy(app)



class Follow(db.Model):
	__tablename__='follows'
	follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
	followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
	timestamp = db.Column(db.DateTime, default = datetime.now)

#文章点赞关系表
class likepost(db.Model):
	__tablename__ = 'likeposts'
	id = db.Column(db.Integer, primary_key = True)
	userid = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key = True)
	postid = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key = True)
	timestamp = db.Column(db.DateTime,default = datetime.now)
	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2
#评论点赞关系表
class likecomment(db.Model):
	__tablename__ = 'likecomments'
	id = db.Column(db.Integer, primary_key = True)
	userid = db.Column(db.Integer, db.ForeignKey('users.id'),primary_key = True)
	commentid = db.Column(db.Integer,db.ForeignKey('comments.id'),primary_key = True)
	timestamp = db.Column(db.DateTime,default = datetime.now)
	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2
#活动的评论点赞关系表
class likecommentact(db.Model):
	__tablename__ = 'likecommentacts'
	id = db.Column(db.Integer, primary_key = True)
	userid = db.Column(db.Integer, db.ForeignKey('users.id'),primary_key = True)
	commentid = db.Column(db.Integer,db.ForeignKey('commentacts.id'),primary_key = True)
	timestamp = db.Column(db.DateTime,default = datetime.now)
	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2
#喜欢的活动
class likeactivity(db.Model):
	__tablename__ = 'likeactivitys'
	id = db.Column(db.Integer,primary_key = True)
	userid = db.Column(db.Integer,db.ForeignKey('users.id'),primary_key = True)
	activityid = db.Column(db.Integer,db.ForeignKey('activitys.id'),primary_key = True)
	timestamp = db.Column(db.DateTime,default = datetime.now)

#参加活动表
class attentactivity(db.Model):
	__tablename__ = 'attentactivitys'
	id = db.Column(db.Integer,primary_key = True)
	userid = db.Column(db.Integer,db.ForeignKey('users.id'),primary_key = True)
	activityid = db.Column(db.Integer,db.ForeignKey('activitys.id'),primary_key = True)
	state = db.Column(db.Boolean,default =False)
	timestamp = db.Column(db.DateTime,default = datetime.now)
	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2


class Visit(db.Model):
	__tablename__ = 'visit'
	id = db.Column(db.Integer, primary_key = True)
	guestid = db.Column(db.Integer, db.ForeignKey('users.id'))
	hostid = db.Column(db.Integer, db.ForeignKey('users.id'))
	timestamp = db.Column(db.DateTime, default = datetime.now)

#上传活动的生活照
class activitylifeimage(db.Model):
	__tablename__ = 'activitylifeimages'
	id = db.Column(db.Integer,primary_key = True)
	activityid = db.Column(db.Integer,db.ForeignKey('activitys.id'),primary_key = True)
	userid = db.Column(db.Integer,db.ForeignKey('users.id'),primary_key = True)
	imageid = db.Column(db.Integer,db.ForeignKey("imageurls.id"),primary_key = True)
	timestamp = db.Column(db.DateTime,default = datetime.now)
	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2

#点赞的食物卡片
class likefoodcard(db.Model):
	__tablename__ = 'likefoodcards'
	id = db.Column(db.Integer, primary_key = True)
	userid = db.Column(db.Integer, db.ForeignKey('users.id'),primary_key = True)
	foodcardid = db.Column(db.Integer,db.ForeignKey('foodcards.id'),primary_key = True)
	timestamp = db.Column(db.DateTime,default = datetime.now)
	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2


class User(db.Model):
	__tablename__='users'
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(32),unique = True)
	password = db.Column(db.String(32))
	token = db.Column(db.String(32))
	school = db.Column(db.String(32))
	degree = db.Column(db.String(32))
	department = db.Column(db.String(32))
	enrollment = db.Column(db.String(32))
	name = db.Column(db.String(32))
	gender = db.Column(db.String(32))
	phone = db.Column(db.String(32))
	birthday = db.Column(db.String(32))
	wechat = db.Column(db.String(32))
	qq = db.Column(db.String(32))
	hometown = db.Column(db.String(32))
	hobby = db.Column(db.String(128))
	preference = db.Column(db.String(128))
	qianshoudongda = db.Column(db.String(32))
	#autumn1=db.Column(db.String(32))
	#autumn2=db.Column(db.String(32))
	#autumn3=db.Column(db.String(32))
	#yaoda = db.Column(db.String(32))
	lookcount = db.Column(db.Integer,default = 0)
	cardflag = db.Column(db.Boolean,default =False)
	weme = db.Column(db.Integer,default = 100)
	certification = db.Column(db.Boolean,default =False)
	timestamp = db.Column(db.DateTime,default = datetime.now)
	#relation
	#all users followed by this
	followeds = db.relationship('Follow', foreign_keys = [Follow.follower_id], backref = db.backref('follower', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#all users that follow this
	followers = db.relationship('Follow', foreign_keys = [Follow.followed_id], backref = db.backref('followed', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')

	visitors = db.relationship('Visit', foreign_keys = [Visit.hostid], backref = db.backref('host', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#all users that follow this
	visiteds = db.relationship('Visit', foreign_keys = [Visit.guestid], backref = db.backref('guest', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')

	#校园认证
	certifications = db.relationship('schoolcertification',backref = 'author', lazy = 'dynamic')
	#用户的头像和声音名片
	avatarvoices = db.relationship('avatarvoice',backref = 'author', lazy = 'dynamic')
	#该用户举报的东西
	reports = db.relationship('report',backref = 'author', lazy = 'dynamic')
	#该用户发表的帖子
	posts = db.relationship('post',backref = 'author', lazy = 'dynamic')
	#该用户的评论
	comments = db.relationship('comment', backref = 'author',lazy = 'dynamic')
	#该用户评论活动的评论
	commentacts = db.relationship('commentact', backref = 'author',lazy = 'dynamic')
	#likeposts的外键，该用户喜欢了哪些帖子
	likeposts = db.relationship('likepost', foreign_keys = [likepost.userid], backref = db.backref('likeuser', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#likecomments的外键。该用户喜欢了哪些评论
	likecomments =  db.relationship('likecomment', foreign_keys = [likecomment.userid], backref = db.backref('likeuser', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#likecommentacts的外键。该用户喜欢了哪些活动评论
	likecommentacts =  db.relationship('likecommentact', foreign_keys = [likecommentact.userid], backref = db.backref('likeuser', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#参加的活动activity
	activitys = db.relationship('attentactivity', foreign_keys = [attentactivity.userid], backref = db.backref('attentuser', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#发起的活动
	publishactivitys = db.relationship('Activity',backref = 'author', lazy = 'dynamic')       
	#喜欢的活动
	likeactivitys = db.relationship('likeactivity', foreign_keys = [likeactivity.userid], backref = db.backref('likeuser', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#参加活动的生活照
	lifeimages = db.relationship('activitylifeimage', foreign_keys = [activitylifeimage.userid], backref = db.backref('users', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#发起的美食卡片
	publishfoodcards = db.relationship('foodcard',backref = 'author', lazy = 'dynamic')   	
	#点赞的美食卡片
	likefoodcards =  db.relationship('likefoodcard', foreign_keys = [likefoodcard.userid], backref = db.backref('likeuser', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#
	def add(self):
		try:
			tempuser = User.query.filter_by(username=self.username).first()
			if tempuser is None:
				db.session.add(self)
				db.session.commit()
				return 0
			else:
				return 1
		except Exception, e:
			print e
			db.session.rollback()
			return 2
	def addpwd(self):
		try:
			db.session.add(self)
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2			
		
	def isExisted(self):
		tempuser = User.query.filter_by(username=self.username,password=self.password).first()
		if tempuser is None:
			return 0
		else:
			return 1
	def isExistedusername(self):
		tempuser = User.query.filter_by(username = self.username).first()
		if tempuser is None:
			return 0
		else:
			return 1
	def attent(self,activity):
		try:
			flag = self.activitys.filter_by(activityid = activity.id).first()
			if flag is None:
				f = attentactivity(attentuser = self,attentwhatactivity = activity)
				db.session.add(f)
				db.session.commit()
				return 0
			else:
				return 1
		except Exception, e:
			db.session.rollback()
			return 2	
	def unattent(self,activity):
		try:
			lp = self.activitys.filter_by(activityid = activity.id).first()
			if lp != None:
				db.session.delete(lp)
				db.session.commit()
				return 0
			else:
				return 1
		except Exception, e:
			db.session.rollback()
			return 2
	def isattent(self,activityid):
		try:
			# f = self.activitys.all()
			# L = [x.activityid for x in f]
			# flag = activityid in L
			flag = self.activitys.filter_by(activityid = activityid).first()
			if flag != None:
				return 1
			else:
				return 0
		except Exception, e:
			return 2
			

	def is_following(self, user):
		u=self.followeds.filter_by(followed_id=user.id).first()
		return  u is not None

	def is_followed_by(self, user):
		return self.followers.filter_by(follower_id=user.id).first() is not None

	def follow(self, user):
		try:
			if not self.is_following(user):
				f = Follow(follower=self, followed=user)
				db.session.add(f)
				db.session.commit()
				return 0
			else:
				return 1	
		except Exception, e:
			db.session.rollback()
			return 2
	def unfollow(self, user):
		try:
			f = self.followeds.filter_by(followed_id=user.id).first()
			if f:
				db.session.delete(f)
				db.session.commit()
				return 0
			else:
				return 1
		except Exception, e:
			db.session.rollback()
			return 2
	def likeactivity(self,activity):
		try:
			lp = self.likeactivitys.filter_by(activityid = activity.id).first()
			if lp is None:
				lp = likeactivity(likeuser = self, likewhatactivity = activity)
				db.session.add(lp)
				db.session.commit()
				return 0
			else:
				return 1
		except Exception, e:
			print e
			db.session.rollback()
			return 2
	def unlikeactivity(self,activity):
		try:
			lp = self.likeactivitys.filter_by(activityid = activity.id).first()
			if lp != None:
				db.session.delete(lp)
				db.session.commit()
				return 0
			else:
				return 1
		except Exception, e:
			print e
			db.session.rollback()
			return 2		
		
	def visit(self, user):
		try:
			v = Visit(guest = self, host = user)
			db.session.add(v)
			db.session.commit()
			return 0
		except Exception, e:
			db.session.rollback()
			return 2
	def likepost(self,post):
		try:
			lp = self.likeposts.filter_by(postid = post.id).first()
			if lp is None:
				lp = likepost(likeuser = self, likewhatpost = post)
				db.session.add(lp)
				db.session.commit()
				return 0
			else:
				return 1
		except Exception, e:
			print e
			db.session.rollback()
			return 2
	def likecomment(self,comment):
		try:
			lc = self.likecomments.filter_by(commentid = comment.id).first()
			if lc is None:
				lc = likecomment(likeuser = self, likewhatcomment = comment)
				db.session.add(lc)
				db.session.commit()
				return 0
			else:
				return 1
		except Exception, e:
			print e
			db.session.rollback()
			return 2		
	def likecommentact(self,comment):
		try:
			lc = self.likecommentacts.filter_by(commentid = comment.id).first()
			if lc is None:
				lc = likecommentact(likeuser = self, likewhatcomment = comment)
				db.session.add(lc)
				db.session.commit()
				return 0
			else:
				return 1
		except Exception, e:
			print e
			db.session.rollback()
			return 2		
	def likefoodcard(self,foodcard):
		try:
			lc = self.likefoodcards.filter_by(foodcardid = foodcard.id).first()
			if lc is None:
				lc = likefoodcard(likeuser = self, likewhatfoodcard = foodcard)
				db.session.add(lc)
				db.session.commit()
				return 0
			else:
				return 1
		except Exception, e:
			print e
			db.session.rollback()
			return 2		

	def publishpost(self,post):
		try:
			post.author = self
			db.session.add(post)
			db.session.execute('set names utf8mb4')
			db.session.commit()
			return 0
		except Exception, e:
			print e
			db.session.rollback()
			return 2	
	def publishactivity(self,activity):
		try:
			activity.author = self
			db.session.add(activity)
			db.session.execute('set names utf8mb4')
			db.session.commit()
			return 0
		except Exception, e:
			print e
			db.session.rollback()
			return 2	
	def publishfoodcard(self,foodcard):
		try:
			foodcard.author = self
			db.session.add(foodcard)
			db.session.execute('set names utf8mb4')
			db.session.commit()
			return 0
		except Exception, e:
			print e
			db.session.rollback()
			return 2	
	def publishreport(self,report):
		try:
			report.author = self
			db.session.add(report)
			db.session.execute('set names utf8mb4')
			db.session.commit()
			return 0
		except Exception, e:
			print e
			db.session.rollback()
			return 2	
	def commenttopost(self,comment,post):
		try:
			comment.post = post
			comment.author = self
			comment.commentid = -1
			db.session.add(comment)
			db.session.execute('set names utf8mb4')
			db.session.commit()
			return 0
		except Exception, e:
			print e
			db.session.rollback()
			return 2		
	def commenttoactivity(self,commentact,activity):
		try:
			commentact.activity = activity
			commentact.author = self
			commentact.commentid = -1
			db.session.add(commentact)
			db.session.execute('set names utf8mb4')
			db.session.commit()
			return 0
		except Exception, e:
			print e
			db.session.rollback()
			return 2	
	def commenttocomment(self,comment,destcomment):
		try:
			comment.post = destcomment.post
			comment.author = self
			comment.commentid = destcomment.id
			db.session.add(comment)
			db.session.execute('set names utf8mb4')
			db.session.commit()
			return 0
		except Exception, e:
			print e
			db.session.rollback()
			return 2	
	def commenttocommentact(self,commentact,destcomment):
		try:
			commentact.activity = destcomment.activity
			commentact.author = self
			commentact.commentid = destcomment.id
			db.session.add(commentact)
			db.session.execute('set names utf8mb4')
			db.session.commit()
			return 0
		except Exception, e:
			print e
			db.session.rollback()
			return 2				
							

class MessageAndimage(db.Model):
	__tablename__ = 'messageandimages'
	message_id = db.Column(db.Integer,db.ForeignKey('messages.id'),primary_key = True)
	image_id = db.Column(db.Integer,db.ForeignKey('imageurls.id'),primary_key = True)

class Message(db.Model):
	__tablename__ = "messages"
	id = db.Column(db.Integer,primary_key = True)
	SendId = db.Column(db.String(32))
	RecId = db.Column(db.String(32))
	imagedb = db.relationship('MessageAndimage', foreign_keys = [MessageAndimage.message_id],backref = db.backref('content1',lazy = 'joined'),lazy = 'dynamic',cascade = 'all,delete-orphan')
	text = db.Column(db.String(256))
	state = db.Column(db.String(32),default = '1')
	sendtime = db.Column(db.DateTime, default = datetime.now)

	def add(self):
		try:
			db.session.add(self)
			db.session.execute('set names utf8mb4')
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2
	def addimage(self,image):
		try:
			f = MessageAndimage(content1=self, content2=image)
			db.session.add(f)
			db.session.commit()
			return 0	
		except Exception, e:
			print e
			db.session.rollback()
			return 2

class commentactimageAttach(db.Model):
	__tablename__ = "commentactimageattachs"
	id = db.Column(db.Integer,primary_key = True)
	commentid = db.Column(db.Integer,db.ForeignKey('commentacts.id'),primary_key = True)
	imageid = db.Column(db.Integer,db.ForeignKey('imageurls.id'),primary_key = True)
	timestamp = db.Column(db.DateTime,default = datetime.now)

class commentimageAttach(db.Model):
	__tablename__ = "commentimageattachs"
	id = db.Column(db.Integer,primary_key = True)
	commentid = db.Column(db.Integer,db.ForeignKey('comments.id'),primary_key = True)
	imageid = db.Column(db.Integer,db.ForeignKey('imageurls.id'),primary_key = True)
	timestamp = db.Column(db.DateTime,default = datetime.now)

class postimageAttach(db.Model):
	__tablename__ = "postimageattachs"
	id = db.Column(db.Integer,primary_key = True)
	postid = db.Column(db.Integer,db.ForeignKey("posts.id"),primary_key = True)
	imageid = db.Column(db.Integer,db.ForeignKey("imageurls.id"),primary_key = True)
	timestamp = db.Column(db.DateTime,default = datetime.now)

class activityimageAttach(db.Model):
	__tablename__ = "activityimageattachs"
	id = db.Column(db.Integer,primary_key = True)
	activityid = db.Column(db.Integer,db.ForeignKey("activitys.id"),primary_key = True)
	imageid = db.Column(db.Integer,db.ForeignKey("imageurls.id"),primary_key = True)
	timestamp = db.Column(db.DateTime,default = datetime.now)

class imageURL(db.Model):
	__tablename__ = "imageurls"
	id = db.Column(db.Integer, primary_key = True)
	number = db.Column(db.String(32),primary_key = True)
	#私信的图片附件
	messagedb = db.relationship('MessageAndimage', foreign_keys = [MessageAndimage.image_id],backref = db.backref('content2',lazy = 'joined'),lazy = 'dynamic',cascade = 'all,delete-orphan')
	#帖子的图片附件
	posts = db.relationship('postimageAttach', foreign_keys = [postimageAttach.imageid],backref = db.backref('images',lazy = 'joined'),lazy = 'dynamic',cascade = 'all,delete-orphan')
	#评论的图片附件
	comments = db.relationship('commentimageAttach', foreign_keys = [commentimageAttach.imageid],backref = db.backref('images',lazy = 'joined'),lazy = 'dynamic',cascade = 'all,delete-orphan')
	#活动的图片附件
	activitys = db.relationship('activityimageAttach', foreign_keys = [activityimageAttach.imageid],backref = db.backref('images',lazy = 'joined'),lazy = 'dynamic',cascade = 'all,delete-orphan')
	#活动的生活照
	lifeimages = db.relationship('activitylifeimage', foreign_keys = [activitylifeimage.imageid],backref = db.backref('images',lazy = 'joined'),lazy = 'dynamic',cascade = 'all,delete-orphan')

	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2		

class Activity(db.Model):
	__tablename__="activitys"
	id = db.Column(db.Integer,primary_key=True)
	top = db.Column(db.String(32),default = '0')
	title=db.Column(db.String(32),primary_key=True)
	time=db.Column(db.String(32))
	location=db.Column(db.String(32))
	number=db.Column(db.String(32))
	signnumber = db.Column(db.Integer)
	state = db.Column(db.String(32))
	disable = db.Column(db.Boolean,default =False)
	remark = db.Column(db.String(32))
	authorid = db.Column(db.Integer,db.ForeignKey('users.id'))
	whetherimage = db.Column(db.Boolean,default =False)
	advertise = db.Column(db.String(32))
	detail = db.Column(db.Text)
	label = db.Column(db.String(32))
	passflag = db.Column(db.String(8),default = '0')
	likenumber = db.Column(db.Integer,default = 0)
	timestamp = db.Column(db.DateTime,default = datetime.now)
	#参加活动的人
	users = db.relationship('attentactivity', foreign_keys = [attentactivity.activityid], backref = db.backref('attentwhatactivity', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#活动的图片附件
	images = db.relationship('activityimageAttach', foreign_keys = [activityimageAttach.activityid], backref = db.backref('activitys', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#报名活动用户的生活照
	lifeimages = db.relationship('activitylifeimage', foreign_keys = [activitylifeimage.activityid], backref = db.backref('activitys', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#喜欢该活动的人
	likeusers = db.relationship('likeactivity', foreign_keys = [likeactivity.activityid], backref = db.backref('likewhatactivity', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#活动的评论
	comments = db.relationship('commentact',backref = 'activity',lazy = 'dynamic')
	def add(self):
		try:
			db.session.add(self)
			db.session.execute('set names utf8mb4')
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2	
	def addimage(self,image):
		try:
			f = activityimageAttach(activitys=self, images=image)
			db.session.add(f)
			db.session.commit()
			return 0	
		except Exception, e:
			print e
			db.session.rollback()
			return 2		
	def addlifeimage(self,user,image):
		try:
			f = activitylifeimage(activitys=self, users = user,images=image)
			db.session.add(f)
			db.session.commit()
			return 0	
		except Exception, e:
			print e
			db.session.rollback()
			return 2		



class topic(db.Model):
	__tablename__ = "topics"
	id = db.Column(db.Integer,primary_key=True)
	theme = db.Column(db.String(32))
	imageurl = db.Column(db.String(256))
	note = db.Column(db.String(128))
	number = db.Column(db.Integer)
	slogan = db.Column(db.String(128))
	postnumber = db.Column(db.Integer)
	rank = db.Column(db.Integer)
	posts = db.relationship('post',backref = 'topic',lazy = 'dynamic')
	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2	

class post(db.Model):
	__tablename__ = "posts"
	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(128))
	body = db.Column(db.Text)
	timestamp = db.Column(db.DateTime,index = True, default = datetime.now)
	authorid = db.Column(db.Integer,db.ForeignKey('users.id'))
	topicid = db.Column(db.Integer,db.ForeignKey('topics.id'))
	likenumber = db.Column(db.Integer,default = 0)
	commentnumber = db.Column(db.Integer,default = 0)
	top = db.Column(db.Integer, default = 0)
	disable = db.Column(db.Boolean,default =False)

	#用户评论comment的外键postid，这篇文章的所有评论
	comments = db.relationship('comment',backref = 'post',lazy = 'dynamic')
	#赞了什么文章,喜欢这个文章的所有用户
	likeusers = db.relationship('likepost', foreign_keys = [likepost.postid], backref = db.backref('likewhatpost', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#帖子的图片，以附件的形式上传
	images = db.relationship('postimageAttach', foreign_keys = [postimageAttach.postid], backref = db.backref('posts', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	def add(self):
		try:
			db.session.add(self)
			db.session.execute('set names utf8mb4');
			db.session.commit()
			return 0
		except Exception, e:
			print e
			db.session.rollback()
			return 2
	def addimage(self,image):
		try:
			f = postimageAttach(posts=self, images=image)
			db.session.add(f)
			db.session.commit()
			return 0	
		except Exception, e:
			print e
			db.session.rollback()
			return 2		

class comment(db.Model):
	__tablename__ = 'comments'
	id = db.Column(db.Integer,primary_key = True)
	body = db.Column(db.Text)
	timestamp = db.Column(db.DateTime,index = True, default = datetime.now)
	authorid = db.Column(db.Integer,db.ForeignKey('users.id'))
	postid = db.Column(db.Integer,db.ForeignKey('posts.id'))
	commentid = db.Column(db.Integer,default = -1)
	likenumber = db.Column(db.Integer,default = 0)
	commentnumber = db.Column(db.Integer,default = 0)
	disable = db.Column(db.Boolean,default = False)
	likeusers = db.relationship('likecomment', foreign_keys = [likecomment.commentid], backref = db.backref('likewhatcomment', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#评论的图片，以附件的形式上传
	images = db.relationship('commentimageAttach', foreign_keys = [commentimageAttach.commentid], backref = db.backref('comments', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	def add(self):
		try:
			db.session.add(self)
			db.session.execute('set names utf8mb4')
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2
	def addimage(self,image):
		try:
			f = commentimageAttach(comments=self, images=image)
			db.session.add(f)
			db.session.commit()
			return 0	
		except Exception, e:
			print e
			db.session.rollback()
			return 2	

class commentact(db.Model):
	__tablename__ = 'commentacts'
	id = db.Column(db.Integer,primary_key = True)
	body = db.Column(db.Text)
	timestamp = db.Column(db.DateTime,index = True, default = datetime.now)
	authorid = db.Column(db.Integer,db.ForeignKey('users.id'))
	activityid = db.Column(db.Integer,db.ForeignKey('activitys.id'))
	commentid = db.Column(db.Integer,default = -1)
	likenumber = db.Column(db.Integer,default = 0)
	commentnumber = db.Column(db.Integer,default = 0)
	disable = db.Column(db.Boolean,default = False)
	likeusers = db.relationship('likecommentact', foreign_keys = [likecommentact.commentid], backref = db.backref('likewhatcomment', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	#评论的图片，以附件的形式上传
	images = db.relationship('commentactimageAttach', foreign_keys = [commentactimageAttach.commentid], backref = db.backref('comments', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	def add(self):
		try:
			db.session.add(self)
			db.session.execute('set names utf8mb4')
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2
	def addimage(self,image):
		try:
			f = commentactimageAttach(comments=self, images=image)
			db.session.add(f)
			db.session.commit()
			return 0	
		except Exception, e:
			print e
			db.session.rollback()
			return 2	

class topofficial(db.Model):
	__tablename__ = 'topofficials'
	id = db.Column(db.Integer,primary_key=True)
	imageurl = db.Column(db.String(256))
	postid = db.Column(db.Integer)
	posttitle = db.Column(db.String(128))
	rank = db.Column(db.Integer,default = 0)
	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
			return 0
		except Exception, e:
			print e
			db.session.rollback()
			return 2

class activitytopofficial(db.Model):
	__tablename__ = 'activitytopofficials'
	id = db.Column(db.Integer,primary_key=True)
	imageurl = db.Column(db.String(256))
	activityid = db.Column(db.Integer)
	activitytitle = db.Column(db.String(128))
	rank = db.Column(db.Integer,default = 0)
	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
			return 0
		except Exception, e:
			print e
			db.session.rollback()
			return 2

class foodcard(db.Model):
	__tablename__ = 'foodcards'
	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(128))
	authorid = db.Column(db.Integer,db.ForeignKey('users.id'))
	imageurl = db.Column(db.String(256))
	location = db.Column(db.String(32))
	longitude = db.Column(db.String(32))
	latitude = db.Column(db.String(32))
	price = db.Column(db.String(32))
	comment = db.Column(db.String(512))
	passflag = db.Column(db.String(8),default = '0')
	disable = db.Column(db.Boolean,default = False)
	timestamp = db.Column(db.DateTime,index = True, default = datetime.now)
	likenumber = db.Column(db.Integer,default = 0)
	likeusers = db.relationship('likefoodcard', foreign_keys = [likefoodcard.foodcardid], backref = db.backref('likewhatfoodcard', lazy='joined'), lazy='dynamic', cascade = 'all, delete-orphan')
	def add(self):
		try:
			db.session.add(self)
			db.session.execute('set names utf8mb4')
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2
class report(db.Model):
	__tablename__ = 'reports'
	id = db.Column(db.Integer,primary_key = True)
	authorid = db.Column(db.Integer,db.ForeignKey('users.id'))
	body = db.Column(db.Text)
	type = db.Column(db.String(32))
	typeid = db.Column(db.Integer)
	timestamp = db.Column(db.DateTime,default = datetime.now)
	def add(self):
		try:
			db.session.add(self)
			db.session.execute('set names utf8mb4')
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2

class avatarvoice(db.Model):
	__tablename__ = 'avatarvoices'
	id = db.Column(db.Integer,primary_key = True)
	userid = db.Column(db.Integer,db.ForeignKey('users.id'))
	name = db.Column(db.String(32))
	gender = db.Column(db.String(32))
	avatar_number = db.Column(db.Integer,default = 0)
	avatarurl = db.Column(db.String(256))
	voice_number = db.Column(db.Integer,default = 0)
	voiceurl = db.Column(db.String(256))
	cardflag = db.Column(db.Boolean,default =False)
	disable = db.Column(db.Boolean,default = False)
	def add(self):
		try:
			db.session.add(self)
			db.session.execute('set names utf8mb4')
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2

class schoolcertification(db.Model):
	__tablename__ = 'schoolcertifications'
	id = db.Column(db.Integer,primary_key = True)
	userid = db.Column(db.Integer,db.ForeignKey('users.id'))
	name = db.Column(db.String(32))
	gender = db.Column(db.String(32))
	school = db.Column(db.String(32))
	studentID = db.Column(db.String(64))
	pictureurl = db.Column(db.String(256))
	location = db.Column(db.String(64))
	timestamp = db.Column(db.DateTime,default = datetime.now)
	checkflag = db.Column(db.Boolean,default = False)
	checktime = db.Column(db.DateTime)
	checkresult = db.Column(db.Boolean,default = False)
	def add(self):
		try:
			db.session.add(self)
			db.session.execute('set names utf8mb4')
			db.session.commit()
		except Exception, e:
			print e
			db.session.rollback()
			return 2

def editschooldb(token,school,degree,department,enrollment):
	u=User.query.filter_by(token=token).first()
	if u!=None:
		u.school = school
		u.degree = degree
		u.department = department
		u.enrollment = enrollment
		try:
			db.session.add(u)
			db.session.commit()
			return 0
		except Exception, e:
			db.session.rollback()
			return 1   
	else:
		return 2 

def editpersonaldb(token,name,gender,birthday,phone,wechat,qq,hometown):
	u=User.query.filter_by(token=token).first()
	if u!=None:
		u.name = name
		u.gender = gender
		u.birthday = birthday
		u.phone = phone
		u.wechat = wechat
		u.qq = qq 
		u.hometown = hometown
		try:
			db.session.add(u)
			db.session.commit()
			return 0
		except Exception, e:
			db.session.rollback()
			return 1
	else:
		return 2 

def editpreferdb(token,hobby,preference):
	u=User.query.filter_by(token=token).first()
	if u!=None:
		u.hobby = hobby
		u.preference = preference
		try:
			db.session.add(u)
			db.session.commit()
			return 0
		except Exception, e:
			db.session.rollback()
			return 1   
	else:
		return 2 



def editDBcolumn(token,modifycol,valuecol):
	u=User.query.filter_by(token=token).first()
	#if modifycol=='password':
	#return valuecol
	if u!=None:
		if modifycol=='password':
			u.password = valuecol
		if modifycol=='school':
			u.school = valuecol
		if modifycol=='degree':
			u.degree = valuecol
		if modifycol=='department':
			u.department = valuecol
		if modifycol=='enrollment':
			u.enrollment = valuecol
		if modifycol=='name':
			u.name = valuecol
		if modifycol=='gender':
			u.gender = valuecol
		if modifycol=='birthday':
			u.birthday = valuecol	
		if modifycol=='hobby':
			u.hobby = valuecol
		if modifycol=='preference':
			u.preference = valuecol
		if modifycol=='qianshoudongda':
			u.qianshoudongda = valuecol
		if modifycol=='autumn1':
			u.autumn1=valuecol
		if modifycol=='autumn2':
			u.autumn2=valuecol
		if modifycol=='autumn3':
			u.autumn3=valuecol
		if modifycol=='phone':
			u.phone=valuecol
		if modifycol == 'yaoda':
			u.yaoda = valuecol
			
	else:#
		return 1 

	try:
		db.session.add(u)
		db.session.commit()
		return 0
	except Exception, e:
		db.session.rollback()
		return 1   
	

def getuserinformation(token):
	u=User.query.filter_by(token=token).first()
	return u 

def getTokeninformation(username):
	u=User.query.filter_by(username=username).first()
	return u 

def getuserbyid(id):
	u=User.query.filter_by(id=id).first()
	return u 

def getuserbyname(name):
	tname = '%'+name+'%'
	ulist=User.query.filter(User.name.like(tname))
	return ulist 			

	
def getActivityInformation(id):
	a = Activity.query.filter_by(id = id).first()
	return a 
def getactivityall():
	a = Activity.query.filter_by(disable = False).order_by(Activity.rank).all()
	return a

def getranduser(token):
	u = getuserinformation(token)
	gender = u.gender

	if gender == u'男':
		udif = User.query.filter(and_(User.gender==u"女", User.id > 2)).all()
	else:
		udif = User.query.filter(and_(User.gender==u"男", User.id > 2)).all()

	L1 = [x.id for x in udif]
	f2 = u.followeds.all()
	L2 = [y.followed_id for y in f2]
	L2.append(1)
	L = list(set(L1).difference(set(L2)))
	if len(L)>9:	
		return random.sample(L,10)
	elif len(L)==0:
		return []
	else:
		return L
def getrandcard(u):
	gender = u.gender
	if gender == u'女':
		udif = avatarvoice.query.filter(and_(avatarvoice.gender==u"男", avatarvoice.cardflag != 1)).all()
	else:
		udif = avatarvoice.query.filter(and_(avatarvoice.gender==u"女", avatarvoice.cardflag != 1)).all()
	L1 = [x.userid for x in udif]
	f2 = u.followeds.all()
	L2 = [y.followed_id for y in f2]
	L2.append(1)
	L = list(set(L1).difference(set(L2)))
	if len(L)>9:	
		return random.sample(L,10)
	elif len(L)==0:
		return []
	else:
		return L

def getMessagebyid(id):
	a = Message.query.filter_by(id = id).first()
	return a 

def getMessageList(RecId):
	a = Message.query.filter_by(RecId = RecId).all()
	return a

def getMessageListByID(Id):
	a = Message.query.filter(or_(Message.RecId == Id, Message.SendId == Id)).all()
	return a

def getMessageTwoid(SendId, RecId):
	a = Message.query.filter_by(SendId = SendId, RecId = RecId).all()
	return a

#
def getMessageTwoidPage(SendId, RecId, page):
	m = Message.query.filter(or_(and_(Message.SendId == SendId, Message.RecId == RecId), and_(Message.SendId == RecId, Message.RecId == SendId))).order_by(Message.sendtime.desc()).paginate(page, per_page=5, error_out=False)
	return m

def getImageURLbyid(id):
	a = imageURL.query.filter_by(id = id).first()
	return a 
def gettopicbyid(id):
	a = topic.query.filter_by(id = id).first()
	return a
def getpostbyid(id):
	db.session.execute('set names utf8mb4');
	a = post.query.filter_by(id = id).first()
	return a
def getcommentbyid(id):
	db.session.execute('set names utf8mb4');
	a = comment.query.filter_by(id = id).first()	
	return a
def gettopofficial():
	a = topofficial.query.order_by(topofficial.rank).all()
	return a
def getactivitytopofficial():
	a = activitytopofficial.query.order_by(activitytopofficial.rank).all()
	return a
def gettopiclistdb():
	a = topic.query.order_by(topic.rank).all()
	return a
def getpostlistbypage(page,topicid):
	db.session.execute('set names utf8mb4')
	a = post.query.filter_by(topicid = topicid).order_by(post.top.desc()).order_by(post.timestamp.desc()).paginate(page, per_page=5, error_out=False)
	return a
def getpostcommentbypage(page,postid):
	db.session.execute('set names utf8mb4')
	a = comment.query.filter(and_(comment.postid == postid,comment.commentid == -1)).order_by(comment.timestamp.desc()).paginate(page, per_page=8, error_out=False)
	return a

def getpostcommentactbylimit(endid,activityid):
	db.session.execute('set names utf8mb4')
	a = commentact.query.filter(and_(commentact.activityid == activityid,commentact.commentid == -1)).order_by(commentact.timestamp.desc()).filter(text("id<:value")).params(value=endid).limit(8)
	return a

def getcommenttocommentbyid(destcommentid):
	db.session.execute('set names utf8mb4')
	a= comment.query.filter(comment.commentid.in_(destcommentid)).order_by(comment.timestamp.desc()).all()
	return a
def gettopofficialbyid(id):
	a = topofficial.query.filter_by(id = id).first()
	return a 

def getactivitytopofficialbyid(id):
	a = activitytopofficial.query.filter_by(id = id).first()
	return a 
def getactivitybyid(id):
	a = Activity.query.filter_by(id = id).first()
	return a
def getavatarvoicebyuserid(userid):
	a = avatarvoice.query.filter_by(userid = userid).first()
	return a


if __name__ == '__main__':
	manager.run()





