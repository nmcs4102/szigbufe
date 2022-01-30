from flask import Flask, send_from_directory, redirect, request, url_for, session
from flask.helpers import safe_join
import os
import json
from oauthlib.oauth2 import WebApplicationClient
import requests
from user import User
from sitetemplates import home_template_user, login_template, topup_template_user, checkout_template_user, empty_cart, message_page, order_success, order_status, user_orders_template, client_page
import stripe

#Google Login Setup
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
GOOGLE_CLIENT_ID = "1002301447947-3aj85fv9licjq20l35aphp2ellbvnm0a.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")
app = Flask(__name__)
static = safe_join(os.path.dirname(__file__), 'htmls')
app.app_context().push()
app.secret_key = "8406e61a454e19e05d884f55c881aa033ed4200b269a5ac4f0dd35cda94f0d9a"

#Stripe Checkout Setup
stripe_keys = {
    "secret_key": "sk_test_51K3PCKDqO24KENkJ8X5phY3MJ777AQWqlXTljlE2Dw75U7g3i0fKobAhzwwQSUyjhwu1iKuq1jMCZhoXyHfE7AoV00q1Pbhgmi",
    "publishable_key": "pk_test_51K3PCKDqO24KENkJ8h6WGLmyXCLz9asR75epHMbp46BOV4gGbKlkgJd5odqVHn79UT5289yeGnhKpLmLjcVivf0K002QvZbTYG",
}

stripe.api_key = stripe_keys["secret_key"]

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)
def get_google_provider_cfg():
	return requests.get(GOOGLE_DISCOVERY_URL).json()

@app.route("/")
def index():
	if 'userid' in session:
		user = User.get(session['userid'])
		if user == None:
			session.pop('userid', None)
			return redirect('https://www.szigbufe.shop')
		return home_template_user(user)
	if request.base_url[:11] != "http://www.":
		return redirect('https://www.szigbufe.shop')
	return login_template()
@app.route("/login")
def login():
	google_provider_cfg = get_google_provider_cfg()
	authorization_endpoint = google_provider_cfg["authorization_endpoint"]
	request_uri = client.prepare_request_uri(
		authorization_endpoint,
		redirect_uri=request.base_url + "/callback",
		scope=["openid", "email", "profile"],
	)
	return redirect(request_uri)
@app.route("/login/callback")
def callback():
	code = request.args.get("code")
	google_provider_cfg = get_google_provider_cfg()
	token_endpoint = google_provider_cfg["token_endpoint"]
	token_url, headers, body = client.prepare_token_request(
		token_endpoint,
		authorization_response=request.url,
		redirect_url=request.base_url,
		code=code
	)
	token_response = requests.post(
		token_url,
		headers=headers,
		data=body,
		auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
	)
	client.parse_request_body_response(json.dumps(token_response.json()))
	userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
	uri, headers, body = client.add_token(userinfo_endpoint)
	userinfo_response = requests.get(uri, headers=headers, data=body)
	if userinfo_response.json().get("email_verified"):
		unique_id = userinfo_response.json()["sub"]
		users_email = userinfo_response.json()["email"]
		picture = userinfo_response.json()["picture"]
		users_name = userinfo_response.json()["given_name"]
	else:
		return "User email not available or not verified by Google.", 400
	user = User(
		id_=unique_id, name=users_name, email=users_email, profile_pic=picture, balance=1000, next_order=1
	)
	if not User.get(unique_id):
		User.create(unique_id, users_name, users_email, picture)
	else:
		user = User.get(unique_id)
	session['userid'] = unique_id
	return redirect(url_for("index", _scheme='https', _external=True))
@app.route("/logout")
def logout():
	session.pop('userid', None)
	return redirect(url_for("index", _scheme='https', _external=True))
@app.route("/topup")
def topup():
	if 'userid' in session:
		user = User.get(session['userid'])
		return topup_template_user(user)
	return redirect(url_for("index", _scheme='https', _external=True))
@app.route("/atc")
def add_to_cart():
	if 'userid' in session:
		item = request.args.get("id", default = -1, type = int)
		# add site for invalid item code
		if item != -1:
			if 'cart' in session:
				session['cart'] = "{0},{1}".format(session['cart'], item-1)
			else:
				session['cart'] = str(item-1)
	return redirect(url_for("index", _scheme='https', _external=True))
@app.route("/checkout")
def checkout():
	if 'userid' in session:
		user = User.get(session['userid'])
		if 'cart' in session:
			cart = session['cart'].split(",")
			cart.sort()
			return checkout_template_user(user, cart)
		return empty_cart(user)
	return redirect(url_for("index", _scheme='https', _external=True))
@app.route("/empty_cart")
def empty():
	if 'userid' in session:
		session.pop('cart', None)
	return redirect(url_for("index", _scheme='https', _external=True))
@app.route("/complete_order")
def order():
	if 'userid' in session:
		user = User.get(session['userid'])
		if 'cart' in session:
			cart = session['cart'].split(",")
			cart.sort()
			# try:
			session.pop('cart', None)
			return order_success(user, cart)
			# except:
			session['cart'] = ",".join(cart)
			return message_page(user, "A rendelésed feldolgozása során hiba történet (nagy eséllyel nincs elég pénz fiókodban)")
		return empty_cart(user)
@app.route("/status")
# takes ?id=X as an argument, doesn't work without
def status():
	if 'userid' in session:
		user = User.get(session['userid'])
		order_id = request.args.get("id", default = -1, type = int)
		if order_id != -1:
			try:
				return(order_status(user, order_id))
			except:
				redirect(url_for("index", _scheme='https', _external=True))
	return redirect(url_for("index", _scheme='https', _external=True))
@app.route("/myorders")
def orders():
	if 'userid' in session:
		user = User.get(session['userid'])
		return user_orders_template(user)
	return redirect(url_for("index", _scheme='https', _external=True))
@app.route('/topup_finalize/<product_id>', methods=['POST'])
def finalize(product_id):
	if 'userid' in session:
		user = User.get(session['userid'])
		amount = int(product_id)*100000
		fee = int(int(product_id)*100000*0.014+9000)
		checkout_session = stripe.checkout.Session.create(
			line_items=[
				{
					'price_data': {
						'product_data': {
                        'name': str(int(product_id)*1000),
						},
					'unit_amount': amount,
                    'currency': 'huf',
					},
					'quantity': 1,
				},
				{
					'price_data': {
						'product_data': {
                        'name': "SZIGBufe Dij",
						},
					'unit_amount': fee,
                    'currency': 'huf',
					},
					'quantity': 1,
				},
			],
			payment_method_types=['card'],
			mode='payment',
			success_url=request.host_url + 'finalize_order/success',
			cancel_url=request.host_url + 'finalize_order/cancel',
		)
		return redirect(checkout_session.url)
	return redirect(url_for("index", _scheme='https', _external=True))
@app.route('/finalize_order/success/')
def success():
	if 'userid' in session:
		user = User.get(session['userid'])
		return message_page(user, "A feltöltés sikeres volt.")
	return redirect(url_for("index", _scheme='https', _external=True))
@app.route('/finalize_order/cancel')
def cancel():
	if 'userid' in session:
		user = User.get(session['userid'])
		return message_page(user, "A feltöltés megszakítódott")
	return redirect(url_for("index", _scheme='https', _external=True))
@app.route('/stripewebhook', methods=['POST'])
def new_event():
	event = None
	payload = request.data
	signature = request.headers['STRIPE_SIGNATURE']
	try:
		event = stripe.Webhook.construct_event(
			payload, signature, "whsec_dkT7umhyXTKcMjtjlLxTTCsqa67gyLX0")
	except Exception as e:
		# the payload could not be verified
		abort(400)
	# Avoid exploits >> check amount, not just email address
	if event['type'] == 'checkout.session.completed':
		session = stripe.checkout.Session.retrieve(
		event['data']['object'].id, expand=['line_items'])
		email = session.customer_details.email
		with open("//var//www//html//FlaskApp//topupdata//{}.dat".format(email), "r", encoding="utf-8") as f:
			uid = f.readline()
		user = User.get(uid)
		amounts = []
		for item in session.line_items.data:
			amounts.append(item.description)
		User.update_balance(user, int(user.balance) + int(amounts[0]), user.next_order)
	return {'success': True}
@app.route('/rendelesek')
def rendelesek():
	if 'userid' in session:
		if session['userid'] == "111327346520201991286":
			return client_page()
	return "False"
@app.route('/order-done')
def clearorder():
	if 'userid' in session:
		order_id = request.args.get("ordernum", default = "", type = str)
		if session['userid'] == "111327346520201991286":
			orderfor = order_id.split("-")
			forderid = "{}-{}".format(orderfor[1], orderfor[2])
			with open("//var//www//html//FlaskApp//orderdata//{}".format(forderid), "r", encoding="utf-8") as f:
				export = f.readline()
			with open("//var//www//html//FlaskApp//orderdata//{}".format(forderid), "w", encoding="utf-8") as f:
				export = f.write("1{}".format(export[1:]))
			os.remove("//var//www//html//FlaskApp//currentorders//{}".format(order_id))
			return redirect("https://www.szigbufe.shop/rendelesek")
	return redirect(url_for("index", _scheme='https', _external=True))
		