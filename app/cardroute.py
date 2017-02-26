#-*- coding: UTF-8 -*- 
from flask import Blueprint
from flask import request,jsonify,json
from models import *
import models 
import string
from sqlalchemy import Date, cast
import random
import weme

card_route = Blueprint('card_route', __name__)

#防止数据库为空
"""define checkdbNone"""
def checkdb(dbNone):
	return dbNone if dbNone!=None else ''

#发布美食卡片的路由
@card_route.route("/publishcard",methods=['POST'])
def publishactivity():
	try:
		token = request.json['token']
		title = request.json.get('title','')
		location = request.json.get('location','')
		longitude = request.json.get('longitude','')
		latitude = request.json.get('latitude','')
		price = request.json.get('price','')
		comment = request.json.get('comment','')
		u = getuserinformation(token)
		if u is not None:
			u.weme = u.weme + weme.WEMEpublishFoodcard
			u.addpwd()
			comment = comment.encode('UTF-8')
			tmpfoodcard = foodcard(title = title,location = location,longitude = longitude,latitude = latitude,price = price,comment = comment)
			u.publishfoodcard(tmpfoodcard)
			id = tmpfoodcard.id
			state = 'successful'
			reason = ''
		else:
			id = ''
			state = 'fail'
			reason = 'no user'
	except Exception, e:	
		print e
		id = ''
		state = 'fail'
		reason = 'exception'

	response = jsonify({'state':state,
						'reason':reason,
						'id':id})
	return response

@card_route.route("/getfoodcard",methods=['POST'])
def getfoodcard():
	def isliked(u, foodcardid):
		lc = u.likefoodcards.filter_by(foodcardid = foodcardid).first()
		if lc != None:
			return 1
		else:
			return 0
	try:
		token = request.json['token']
		u = getuserinformation(token)
		if u is not None:
			listfoodcard = foodcard.query.filter_by(passflag='1').all()
			total = len(listfoodcard)
			tmprand = random.sample(listfoodcard,min(10,total))
			result = []
			if len(tmprand)>0:
				for tmpfoodcard in tmprand:
					result += [{"id":tmpfoodcard.id,"title":checkdb(tmpfoodcard.title),"authorid":checkdb(tmpfoodcard.authorid),"author":checkdb(tmpfoodcard.author.name),"imageurl":checkdb(tmpfoodcard.imageurl),'location':checkdb(tmpfoodcard.location),'longitude':checkdb(tmpfoodcard.longitude),'latitude':checkdb(tmpfoodcard.latitude),
								'price':checkdb(tmpfoodcard.price),'comment':checkdb(tmpfoodcard.comment),'likenumber':checkdb(tmpfoodcard.likenumber), 'likeflag':isliked(u, tmpfoodcard.id)}]
				state = 'successful'
				reason = ''
			else:
				result = ''
				state = 'fail'
				reason = 'no card'				
		else:
			result = ''
			state = 'fail'
			reason = 'no user'
	except Exception, e:	
		print e
		result = ''
		state = 'fail'
		reason = 'exception'

	response = jsonify({'state':state,
						'reason':reason,
						'result':result})
	return response

@card_route.route("/likefoodcard",methods=['POST'])
def likefoodcard():
	try:
		token = request.json['token']
		foodcardid = request.json['foodcardid']
		u = getuserinformation(token)
		if u is not None:
			tmpfoodcard = foodcard.query.filter_by(id = foodcardid).first()
			temp = u.likefoodcard(tmpfoodcard)
			if temp == 0:
				state = 'successful'
				reason = ''
				u.weme = u.weme + weme.WEMELIKE
				u.addpwd()
				tmpfoodcard.likenumber = tmpfoodcard.likeusers.count()
				tmpfoodcard.add()
				likenumber = tmpfoodcard.likenumber
			elif temp == 1:
				state = 'fail'
				reason = 'already like'
				likenumber = ''
			else:
				state = 'fail'
				reason = 'exception'
				likenumber = ''
		else:
			state = 'fail'
			reason = 'no user'
			likenumber = ''
	except Exception, e:	
		print e
		likenumber = ''
		state = 'fail'
		reason = 'exception'

	response = jsonify({'state':state,
						'reason':reason,
						'likenumber':likenumber})
	return response 


