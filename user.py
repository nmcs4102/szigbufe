from flask_login import UserMixin


class User(UserMixin):
	def __init__(self, id_, name, email, profile_pic, balance, next_order):
		self.id = id_
		self.name = name
		self.email = email
		self.profile_pic = profile_pic
		self.balance = balance
		self.next_order = next_order

	@staticmethod
	def get(user_id):
		try:
			with open("//var//www//html//FlaskApp//userdata//{}.dat".format(user_id), "r", encoding="utf-8") as f:
				user = f.readline().split(",")
		except:
			return None
		user = User(id_=user[0], name=user[1], email=user[2], profile_pic=user[3], balance=user[4], next_order=user[5])
		return user

	@staticmethod
	def create(id_, name, email, profile_pic):
		with open("//var//www//html//FlaskApp//userdata//{}.dat".format(id_), "w", encoding="utf-8") as f:
			f.write("{0},{1},{2},{3},100000,1".format(id_, name, email, profile_pic))
		with open("//var//www//html//FlaskApp//topupdata//{}.dat".format(email), "w", encoding="utf-8") as f:
				f.write("{}".format(id_))
	@staticmethod
	def update_balance(user, newbal, nnext_order):
		with open("//var//www//html//FlaskApp//userdata//{}.dat".format(user.id), "w", encoding="utf-8") as f:
			f.write("{0},{1},{2},{3},{4},{5}".format(user.id, user.name, user.email, user.profile_pic, newbal, nnext_order))