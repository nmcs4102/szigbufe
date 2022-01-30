from itemdata import item_list
import os

def get_item_template(cart):
	# [:10] prevents too many items from being processed (could slow the server with 1000 items otherwise)
	cart_sorted = list(map(int, cart[:10]))
	checkout_table_lines = ""
	keys = []
	items = {}
	for i in range(len(cart_sorted)):
		ck =cart_sorted[i]
		if ck in items:
			items[ck] += 1
		else:
			keys.append(ck)
			items[ck] = 1
	for i in range(len(keys)):
		cif = item_list[keys[i]+1]
		checkout_table_lines = "{0} {1}".format(checkout_table_lines, """<tr><td id="cart-item"><h3>{0}</h3></td><td id="cart-item"><img src="{1}" width=75px;height=75px></td><td id="cart-item"><h3>{2}x{3}Ft</h3></td></tr>""".format(cif[0], cif[2], items[keys[i]], cif[1]))
	return checkout_table_lines

def get_total(cart):
	cart_sorted = list(map(int, cart[:10]))
	total = 0
	for i in range(len(cart_sorted)):
		total += item_list[cart_sorted[i]+1][1]
	return total


def get_status_message(num):
	if int(num) == 0:
		return "Még nincs kész"
	else:
		return "Elkészült"


def last_orders(user):
	ordernum = int(user.next_order) - 1
	last_order_lines = ""
	for i in range(ordernum, ordernum-10, -1):
		try:
			with open("//var//www//html//FlaskApp//orderdata//{}-{}.dat".format(user.id, i), "r", encoding="utf-8") as f:
				cord = f.readline().split(";")
				last_order_lines = "{0} {1}".format(last_order_lines, """<tr><td id="cart-item"><h3>Rendelés {0}-{1}</h3></td><td id="cart-item">Státusz: {2}</td><td id="cart-item"><h3>Összeg: {3}Ft</h3></td><td><a href="/status?id={4}">Részletek</a></td></tr>""".format(user.id[-3:], i, get_status_message(cord[0]), cord[-1], i))
		except:
			pass
	return last_order_lines


def get_active_orders():
	#Order File Names  <<< This code is probably broken
	ofns = os.listdir("//var//www//html//FlaskApp//currentorders//")
	if not ofns:
		return """<td id="cart-item" colspan="3">Nincsenek aktív rendelések, az oldal 15 másodperc múlva frissül</td>"""
	orders = []
	for i in range(len(ofns)):
		with open("//var//www//html//FlaskApp//currentorders//{}".format(ofns[i]), "r", encoding="utf-8") as f:
			cord = f.readline().split(";")
		citems = cord[1].split(",")
		items = {}
		keys = []
		for f in range(len(citems)):
			ck = int(citems[f])
			if ck in items:
				items[ck] += 1
			else:
				keys.append(ck)
				items[ck] = 1
		itemamount = []
		for f in range(len(keys)):
			itemamount.append("{} x{}".format(item_list[keys[f]+1][0], items[keys[f]]))
		fitems = "<br>".join(itemamount)
		# fix this shit somehow
		cord2 = cord[2].split("-")
		ordernum = cord2[1]
		orderuser = cord2[0][-3:]
		orders.append("""<tr><td id="cart-item"><h3>#{}-{}</h3></td><td id="cart-item">{}</td><td id="cart-item"><a class="btn btn-outline-success" href="/order-done?ordernum={}" role="button">Kesz</a></td></tr>""".format(orderuser, ordernum, fitems, ofns[i]))
	return " ".join(orders)