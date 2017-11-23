from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect , HttpResponse
from django.template import RequestContext
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Ad,Tag,Region

def home(request):
	template = loader.get_template('myapp/home.html')
	ads = Ad.objects.all()
	context = {
	'ads' : ads,
	}
	return HttpResponse(template.render(context,request))

def ad(request,ad_id):
	try:
		template = loader.get_template('myapp/products.html')
		ads = Ad.objects.get(id = ad_id)
		context = {
		'details':ads
		}
		return HttpResponse(template.render(context,request))
	except Ad.DoesNotExist as s:
		return HttpResponse("Ad doesn't Exists")
@login_required
def ad_add(request):
	if request.method == 'POST':
		try:
			a = Tag.objects.get(id = request.POST['tag'])
			b = Region.objects.get(code = request.POST['region'])
			c = request.POST['desc']
			Ad.objects.create(a_tag = a,a_region = b, a_desc = c )
			template = loader.get_template('myapp/add.html')
			tags = Tag.objects.all()
			reg = Region.objects.all()
			context = {
			'tags ':tags,
			'reg ': reg,

			}
			return HttpResponseRedirect('/add/')
		except Exception as e:
			return HttpResponse("Error while adding an Ad please contact the Admin ")

	else:
		template= loader.get_template('myapp/add.html')
		tags = Tag.objects.all()
		reg = Region.objects.all()
		context = {
		'tags' :tags,
		'reg' :reg,

		}
		return HttpResponse(template.render(context,request))

def uLogin(request):
	if request.method =='POST':
		username = request.POST['uName']
		password = request.POST['uPass']
		user = authenticate(username = username,password = password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('Invalid username or password')

	else:

			template = loader.get_template('myapp/login.html')
			return HttpResponse(template.render(RequestContext(request)))

def uLogout(request):
	logout(request)
	return HttpResponseRedirect('/')