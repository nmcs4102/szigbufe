from user import User
import cart_manager
from datetime import datetime

def home_template_user(user):
	return """<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
		<link href="./customer.css" rel="stylesheet">
        <title>SZIG Büfé - Home</title>
		<link rel="shortcut icon" type="image/x-icon" href="https://media.discordapp.net/attachments/916346162171215893/917858667120971828/food.png">
	</head>
	<style>
		#cho1 {{text-align: center}}
		#cart_contents {{margin: auto; padding: 2px width: 650px; border-spacing: 2px;}}
		#cart-item {{height: 60px; padding: 10px; border-spacing: 2px; text-align: center;}}
		#center_this {{text-align: center}}
	</style>
	<body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
		<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
              <div class="navbar-brand">SZIG Büfé</div>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/">Termékek</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/checkout">Kosár</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/myorders">Rendeléseim</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/topup">Feltöltés</a>
                  </li>
                </ul>
					<span class="navbar-text">
						{}Ft | {} <img src="{}" width=50px;height=50px> <a style="text-decoration:none" href="/logout">Kijelentkezés</a>
					</span>
				</div>
			</div>
        </nav>
		<h1 id="cho1">Termékek</h1>
			<hr>
			<table id="cart_contents">
				<tr><td id="cart-item"><img src="https://media.discordapp.net/attachments/916346162171215893/918149590300127273/hot-dog.png?width=150&height=150" width=150px;height=150px></td><td id="cart-item"><h3>Hot Dog</h3>290Ft<br><a class="btn btn-outline-success" href="/atc?id=001" role="button">Kosárba</a></td></tr>
				<tr><td id="cart-item"><img src="https://media.discordapp.net/attachments/916346162171215893/918151054653292574/sandwich.jpg" width=150px;height=150px></td><td id="cart-item"><h3>Szendvics</h3>220Ft<br><a class="btn btn-outline-success" href="/atc?id=002" role="button">Kosárba</a></td></tr>
				<tr><td id="cart-item"><img src="https://media.discordapp.net/attachments/916346162171215893/918150844761915392/csokis-csiga.jpg?width=150&height=150" width=150px;height=150px></td><td id="cart-item"><h3>Csokis Csiga</h3>250Ft<br><a class="btn btn-outline-success" href="/atc?id=003" role="button">Kosárba</a></td></tr>
				<tr><td id="cart-item"><img src="https://media.discordapp.net/attachments/916346162171215893/918151927689277441/chocolate-chips-muffin-isolated-white-background-35031201.jpg" width=150px;height=150px></td><td id="cart-item"><h3>Muffin</h3>350Ft<br><a class="btn btn-outline-success" href="/atc?id=004" role="button">Kosárba</a></td></tr>
				<tr><td id="cart-item"><img src="https://media.discordapp.net/attachments/916346162171215893/918148829302378496/fanta.jpg?width=150&height=150" width=150px;height=150px></td><td id="cart-item"><h3>Fanta</h3>330Ft<br><a class="btn btn-outline-success" href="/atc?id=005" role="button">Kosárba</a></td></tr>
				<tr><td id="cart-item"><img src="https://media.discordapp.net/attachments/916346162171215893/918148483683328000/15374262997377.jpg?width=150&height=150" width=150px;height=150px></td><td id="cart-item"><h3>Mizse 1L</h3>150Ft<br><a class="btn btn-outline-success" href="/atc?id=006" role="button">Kosárba</a></td></tr>
			</table>
			<hr>
	
	</body>
</html>
""".format(user.balance, user.name, user.profile_pic)


def login_template():
	return ''' <!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
		<link href="./login.css" rel="stylesheet">
		<title>SZIG Büfé - Login</title>
		<link rel="shortcut icon" type="image/x-icon" href="https://media.discordapp.net/attachments/916346162171215893/917858667120971828/food.png">
	</head>
	<body>
		<section class="login-block">
			<div class="container-fluid">
				<div class="row">
					<div class="col-sm-12">
						<form class="md-float-material form-material" action="#" method="POST">
							<div class="auth-box card">
								<div class="card-block">
									<div class="row">
										<div class="col-md-12">
											<h2 class="text-center heading">SZIG Büfé</h2>
										</div>
									</div>
									<div class="or-container">
										<div class="line-separator"></div>
									</div>
									<div class="row">
										<div class="col-md-12">
											<h4 class="text-center heading">Lépj be a Google fiókoddal!</h4>
										</div>
									</div> <br>
									<div class="row">
										<div class="d-grid gap-2"><a class="btn btn-lg btn-google btn-block btn-outline" href="/login"><img src="https://img.icons8.com/color/16/000000/google-logo.png"> Sign in with Google</a> </div>
									</div> <br>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
		</section>
	</body>
</html>
'''

def topup_template_user(user):
	return """<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
		<link href="./customer.css" rel="stylesheet">
        <title>SZIG Büfé - Feltöltés</title>
		<link rel="shortcut icon" type="image/x-icon" href="https://media.discordapp.net/attachments/916346162171215893/917858667120971828/food.png">
	</head>
	<style>
	#cho1 {{text-align: center}}
	#cart_contents {{margin: auto; padding: 2px width: 650px; border-spacing: 2px;}}
	#cart-item {{height: 60px; padding: 10px; border-spacing: 2px; text-align: center;}}
	#center_this {{text-align: center}}
	</style>
	<body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
		<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
              <div class="navbar-brand">SZIG Büfé</div>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/">Termékek</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/checkout">Kosár</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/myorders">Rendeléseim</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/topup">Feltöltés</a>
                  </li>
                </ul>
                <span class="navbar-text">
					{}Ft | {} <img src="{}" width=50px;height=50px> <a style="text-decoration:none" href="/logout">Kijelentkezés</a>
				</span>
              </div>
            </div>
		</nav>
		<h1 id="cho1">Fetöltés</h1>
		<hr>
		<table id="cart_contents">
			<tr><td id="cart-item"><h3>1000 Ft</h3></td><td id="cart-item"><form method="POST" action="/topup_finalize/1">
				<input type="submit" value="Feltöltés">
			</form></td></tr>
			<tr><td id="cart-item"><h3>3000 Ft</h3></td><td id="cart-item"><form method="POST" action="/topup_finalize/3">
				<input type="submit" value="Feltöltés">
			</form></td></tr>
			<tr><td id="cart-item"><h3>5000 Ft</h3></td><td id="cart-item"><form method="POST" action="/topup_finalize/5">
				<input type="submit" value="Feltöltés">
			</form></td></tr>
			<tr><td id="cart-item"><h3>10000 Ft</h3></td><td id="cart-item"><form method="POST" action="/topup_finalize/10">
				<input type="submit" value="Feltöltés">
			</form></td></tr>
		</table>
		<hr>
		<h2 id="center_this"><a id="back_btn" style="text-decoration:none" href="/">Vissza</a></h2>
	</body>
</html>
""".format(user.balance, user.name, user.profile_pic)
def checkout_template_user(user, cart):
	total = cart_manager.get_total(cart)
	checkout_table_lines = cart_manager.get_item_template(cart)
	return """<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
		<link href="./customer.css" rel="stylesheet">
		<title>SZIG Büfé - Kosár</title>
        <link rel="shortcut icon" type="image/x-icon" href="https://media.discordapp.net/attachments/916346162171215893/917858667120971828/food.png">
	</head>
	<style>
	#cho1 {{text-align: center}}
	#cart_contents {{margin: auto; padding: 2px width: 650px; border-spacing: 2px;}}
	#cart-item {{height: 60px; padding: 10px; border-spacing: 2px; text-align: center;}}
	#center_this {{text-align: center}}
	</style>
	<body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
		<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
              <div class="navbar-brand">SZIG Büfé</div>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/">Termékek</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/checkout">Kosár</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/myorders">Rendeléseim</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/topup">Feltöltés</a>
                  </li>
                </ul>
                <span class="navbar-text">
					{}Ft | {} <img src="{}" width=50px;height=50px> <a style="text-decoration:none" href="/logout">Kijelentkezés</a>
				</span>
              </div>
            </div>
			</nav>
			<h1 id="cho1">Kosár</h1>
			<hr>
			<table id="cart_contents">
				{}
				<tr><td id="cart-item" colspan="2"><h3>Összeg</h3></td><td id="cart-item"><h3>{}Ft</h3></td></tr>
			</table>
			<hr>
			<h2 id="center_this"><a id="checkout_btn" style="text-decoration:none" href="/complete_order">Megrendelem</a></h2>
			<h2 id="center_this"><a id="checkout_btn" style="text-decoration:none" href="/empty_cart">Empty Cart</a></h2>
	</body>
</html>""".format(user.balance, user.name, user.profile_pic, checkout_table_lines, total)

def empty_cart(user):
	return """<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
		<link href="./customer.css" rel="stylesheet">
		<title>SZIG Büfé - Kosár</title>
        <link rel="shortcut icon" type="image/x-icon" href="https://media.discordapp.net/attachments/916346162171215893/917858667120971828/food.png">
	</head>
	<style>
	#cho1 {{text-align: center}}
	#cart_contents {{margin: auto; padding: 2px width: 650px; border-spacing: 2px;}}
	#cart-item {{height: 60px; padding: 10px; border-spacing: 2px; text-align: center;}}
	#center_this {{text-align: center}}
	</style>
	<body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
		<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
              <div class="navbar-brand">SZIG Büfé</div>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/">Termékek</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/checkout">Kosár</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/myorders">Rendeléseim</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/topup">Feltöltés</a>
                  </li>
                </ul>
                <span class="navbar-text">
					{}Ft | {} <img src="{}" width=50px;height=50px> <a style="text-decoration:none" href="/logout">Kijelentkezés</a>
				</span>
              </div>
            </div>
			</nav>
			<h1 id="cho1">A kosár üres</h1>
			<hr>
			<h2 id="center_this"><a id="checkout_btn" style="text-decoration:none" href="/">Vissza</a></h2>
	</body>
</html>""".format(user.balance, user.name, user.profile_pic)


def message_page(user, message):
	return """<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
		<link href="./customer.css" rel="stylesheet">
		<title>SZIG Büfé - Error</title>
        <link rel="shortcut icon" type="image/x-icon" href="https://media.discordapp.net/attachments/916346162171215893/917858667120971828/food.png">
	</head>
	<style>
	#cho1 {{text-align: center}}
	#cart_contents {{margin: auto; padding: 2px width: 650px; border-spacing: 2px;}}
	#cart-item {{height: 60px; padding: 10px; border-spacing: 2px; text-align: center;}}
	#center_this {{text-align: center}}
	</style>
	<body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
		<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
              <div class="navbar-brand">SZIG Büfé</div>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/">Termékek</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/checkout">Kosár</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/myorders">Rendeléseim</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/topup">Feltöltés</a>
                  </li>
                </ul>
                <span class="navbar-text">
					{}Ft | {} <img src="{}" width=50px;height=50px> <a style="text-decoration:none" href="/logout">Kijelentkezés</a>
				</span>
              </div>
            </div>
			</nav>
			<h1 id="cho1">{}</h1>
			<hr>
			<h2 id="center_this"><a id="checkout_btn" style="text-decoration:none" href="/">Vissza</a></h2>
	</body>
</html>""".format(user.balance, user.name, user.profile_pic, message)
def order_success(user, cart):
	cart_sorted = list(map(int, cart[:10]))
	total = cart_manager.get_total(cart)
	checkout_table_lines = cart_manager.get_item_template(cart)
	if int(user.balance) < total:
		return order_error(user)
	cart_sorted = ",".join(cart[:10])
	export = "0;{};{};{}\n".format(cart_sorted, user.id, total)
	ct = datetime.now()
	timenow = "{}{}{}".format(ct.hour, ct.minute, ct.second)
	with open("//var//www//html//FlaskApp//orderdata//{}-{}.dat".format(user.id, user.next_order), "w", encoding="utf-8") as f:
		f.write(export)
	# Add date to front of order in order to prioritize older orders
	export = "0;{};{}-{};{}\n".format(cart_sorted, user.id, user.next_order, total)
	with open("//var//www//html//FlaskApp//currentorders//{}-{}-{}.dat".format(timenow, user.id, user.next_order), "w", encoding="utf-8") as f:
		f.writelines(export)
	User.update_balance(user, int(user.balance)-total, int(user.next_order)+1)
	user = User.get(user.id)
	return """<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
		<link href="./customer.css" rel="stylesheet">
        <title>SZIG Büfé - Siker</title>
		<link rel="shortcut icon" type="image/x-icon" href="https://media.discordapp.net/attachments/916346162171215893/917858667120971828/food.png">
	</head>
	<style>
	#cho1 {{text-align: center}}
	#cart_contents {{margin: auto; padding: 2px width: 650px; border-spacing: 2px;}}
	#cart-item {{height: 60px; padding: 10px; border-spacing: 2px; text-align: center;}}
	#center_this {{text-align: center}}
	#shorterver {{width: 50%;margin-left: auto;margin-right: auto;}}
	</style>
	<body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
		<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
              <div class="navbar-brand">SZIG Büfé</div>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/">Termékek</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/checkout">Kosár</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/myorders">Rendeléseim</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/topup">Feltöltés</a>
                  </li>
                </ul>
                <span class="navbar-text">
					{}Ft | {} <img src="{}" width=50px;height=50px> <a style="text-decoration:none" href="/logout">Kijelentkezés</a>
				</span>
              </div>
            </div>
			</nav>
			<h1 id="cho1">Rendelés #{}-{} sikeresen elküldve</h1>
			<hr>
			<table id="cart_contents">
				{}
				<tr><td colspan="3"><hr id="shorterver"></td></tr>
				<tr><td id="cart-item" colspan="2"><h3>Összeg</h3></td><td id="cart-item"><h3>{}Ft</h3></td></tr>
			</table>
			<hr>
			<h2 id="center_this"><a id="status_btn" style="text-decoration:none" href="/status?id={}">Rendelés állapota</a></h2>
	</body>
</html>""".format(user.balance, user.name, user.profile_pic, user.id[-3:], int(user.next_order)-1, checkout_table_lines, total, int(user.next_order)-1)

def order_status(user, order_id):
	with open("//var//www//html//FlaskApp//orderdata//{}-{}.dat".format(user.id, order_id), "r", encoding="utf-8") as f:
		order_data = f.readline().split(";")
	cart_sorted = order_data[1].split(",")
	total = cart_manager.get_total(cart_sorted)
	checkout_table_lines = cart_manager.get_item_template(cart_sorted)
	status = cart_manager.get_status_message(order_data[0])
	return """<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
		<link href="./customer.css" rel="stylesheet">
        <title>SZIG Büfé - Status</title>
		<link rel="shortcut icon" type="image/x-icon" href="https://media.discordapp.net/attachments/916346162171215893/917858667120971828/food.png">
	</head>
	<style>
	#cho1 {{text-align: center}}
	#cart_contents {{margin: auto; padding: 2px width: 650px; border-spacing: 2px;}}
	#cart-item {{height: 60px; padding: 10px; border-spacing: 2px; text-align: center;}}
	#center_this {{text-align: center}}
	#shorterver {{width: 50%;margin-left: auto;margin-right: auto;}}
	</style>
	<body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
		<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
              <div class="navbar-brand">SZIG Büfé</div>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/">Termékek</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/checkout">Kosár</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/myorders">Rendeléseim</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/topup">Feltöltés</a>
                  </li>
                </ul>
                <span class="navbar-text">
					{}Ft | {} <img src="{}" width=50px;height=50px> <a style="text-decoration:none" href="/logout">Kijelentkezés</a>
				</span>
              </div>
            </div>
			</nav>
			<h1 id="cho1">Rendelés #{}-{}</h1>
			<hr>
			<table id="cart_contents">
				{}
				<tr><td colspan="3"><hr id="shorterver"></td></tr>
				<tr><td id="cart-item" colspan="2"><h3>Összeg</h3></td><td id="cart-item"><h3>{}Ft</h3></td></tr>
			</table>
			<hr>
			<h2 id="center_this">{}</h2>
			<h2 id="center_this"><a id="status_btn" style="text-decoration:none" href="/myorders">Vissza</a></h2>
	</body>
</html>""".format(user.balance, user.name, user.profile_pic, user.id[-3:], order_id, checkout_table_lines, total, status, int(user.next_order)-1)

def user_orders_template(user):
	last_order_lines = cart_manager.last_orders(user)
	return """<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
		<link href="./customer.css" rel="stylesheet">
        <title>SZIG Büfé - Rendelés History</title>
		<link rel="shortcut icon" type="image/x-icon" href="https://media.discordapp.net/attachments/916346162171215893/917858667120971828/food.png">
	</head>
	<style>
	#cho1 {{text-align: center}}
	#cart_contents {{margin: auto; padding: 2px width: 650px; border-spacing: 2px;}}
	#cart-item {{height: 60px; padding: 10px; border-spacing: 2px; text-align: center;}}
	#center_this {{text-align: center}}
	</style>
	<body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
		<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
              <div class="navbar-brand">SZIG Büfé</div>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/">Termékek</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/checkout">Kosár</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/myorders">Rendeléseim</a>
                  </li>
				  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/topup">Feltöltés</a>
                  </li>
                </ul>
                <span class="navbar-text">
					{}Ft | {} <img src="{}" width=50px;height=50px> <a style="text-decoration:none" href="/logout">Kijelentkezés</a>
				</span>
              </div>
            </div>
			</nav>
			<h1 id="cho1">Utolsó 10 rendelés</h1>
			<hr>
			<table id="cart_contents">
				{}
			</table>
			<hr>
			<h2 id="center_this"><a id="status_btn" style="text-decoration:none" href="/">Vissza</a></h2>
	</body>
</html>""".format(user.balance, user.name, user.profile_pic, last_order_lines)
def client_page():
	cur_orders = cart_manager.get_active_orders()
	refresher = ""
	if cur_orders == """<td id="cart-item" colspan="3">Nincsenek aktív rendelések, az oldal 15 másodperc múlva frissül</td>""":
		refresher = """<meta http-equiv="refresh" content="15">"""
	return """<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
		<link href="./customer.css" rel="stylesheet">
        <title>SZIG Büfé - Home</title>
		<link rel="shortcut icon" type="image/x-icon" href="https://media.discordapp.net/attachments/916346162171215893/917858667120971828/food.png">
		{}
	</head>
	<style>
		#cho1 {{text-align: center}}
		#cart_contents {{margin: auto; padding: 10px width: 1000px; border-spacing: 10px;}}
		#cart-item {{height: 60px; padding: 10px; border-spacing: 5px; text-align: center;}}
		#center_this {{text-align: center}}
	</style>
	<body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
		<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
              <div class="navbar-brand">SZIG Büfé - Aktív</div>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/rendelesek">Frissítés</a>
                  </li>
                </ul>
					<span class="navbar-text">
						Rendelések Oldal
					</span>
				</div>
			</div>
        </nav>
		<h1 id="cho1">Aktiv rendelesek</h1>
			<hr>
			<table id="cart_contents">
				<tr><td id="cart-item"><h3>Rendeles</h3><td id="cart-item"><h3>Termekek</h3></td><td id="cart-item"><h3>Statusz</h3></td></tr>
				{}
			</table>
			<hr>
	</body>
</html>""".format(refresher, cur_orders)