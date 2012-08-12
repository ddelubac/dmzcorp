from django.shortcuts import render_to_response

def home(request):
	return render_to_response("public/home.html", {"welcome_msg": "DMZCorp Starts Small"})

def people(request):
	return render_to_response("public/people.html", {})

def products(request):
	return render_to_response("public/products.html", {})

def lcd_box(request):
	return render_to_response("public/lcd-box.html", {})
