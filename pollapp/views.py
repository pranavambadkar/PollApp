from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import PollModel, DemoModel, SocialMedia
from django.http import HttpResponse


def uhome(request):
	if request.user.is_authenticated:
		return render(request, "uhome.html")
	else:
		return redirect("ulogin")

def ulogin(request):
	if request.user.is_authenticated:
		return redirect("uhome")
	else:
		if request.method == "POST":
			un = request.POST.get("un")
			pw = request.POST.get("pw")
			usr = authenticate(username=un, password=pw)
			if usr is None:
				return render(request, "ulogin.html", {"msg":"Invalid Username or Password."})
			else:
				login(request, usr)
				return redirect("uhome")
		else:
			return render(request, "ulogin.html")

def usignup(request):
	if request.user.is_authenticated:
		return redirect("uhome")
	else:
		if request.method == "POST":
			un = request.POST.get("un")
			email = request.POST.get("email")
			pw1 = request.POST.get("pw1")
			pw2 = request.POST.get("pw2")
			if pw1 == pw2:
				try:
					usr = User.objects.get(username=un)
					return render(request, "usignup.html", {"msg":"User already registered."})
				except User.DoesNotExist:
					usr = User.objects.create_user(username=un, email=email, password=pw1)
					usr.save()
					return redirect("ulogin")
			else:
				return render(request, "usignup.html", {"msg":"Failed, Password did not match."})
		else:
			return render(request, "usignup.html")

def create(request):
	if request.user.is_authenticated and request.method == "POST":
		question = request.POST.get("question")
		op1 = request.POST.get("op1")
		op2 = request.POST.get("op2")
		op3 = request.POST.get("op3")
		data = PollModel(question=question, op1=op1, op2=op2, op3=op3)
		data.creator = request.user
		data.save()
		poll = PollModel.objects.all()
		return render(request, "viewpoll.html", {"poll" : poll})
	elif request.user.is_authenticated:
		return render(request, "create.html")
	else:
		return redirect("uhome")

def demo(request):
	poll = DemoModel.objects.get()
	if request.method == "POST":
		selected_option = request.POST['poll']
		if selected_option == "option1":
			poll.option_one_count += 1
		elif selected_option == "option2":
			poll.option_two_count += 1
		elif selected_option == "option3":
			poll.option_three_count += 1
		else:
			return HttpResponse(400, "Invalid form!")
		poll.save()
		return redirect("demoresult")
	return render(request, "demo.html", {"poll" : poll})

def demoresult(request):
	poll = DemoModel.objects.get()
	return render(request, "demoresult.html", {"poll" : poll})

def about(request):
	social_media = SocialMedia.objects.all()
	return render(request, "about.html", {"social_media": social_media})

def vote(request, poll_id):
	if request.user.is_authenticated:
		poll= PollModel.objects.get(pk=poll_id)
		if request.method == "POST":
			selected_option = request.POST['poll']
			if selected_option == "option1":
				poll.op1c += 1
			elif selected_option == "option2":
				poll.op2c += 1
			elif selected_option == "option3":
				poll.op3c += 1
			else:
				return HttpResponse(400, "Invalid form!")
			poll.save()
			return redirect("results", poll.id)
		return render(request, "vote.html", {"poll" : poll})
	else:
		return redirect("ulogin")

def viewpoll(request):
	if request.user.is_authenticated:
		poll = PollModel.objects.all()
		return render(request, "viewpoll.html", {"poll" : poll})
	else:
		return redirect("ulogin")

def results(request, poll_id):
	if request.user.is_authenticated:
		poll = PollModel.objects.get(pk=poll_id)
		return render(request, "results.html", {"poll" : poll})
	else:
		return redirect("ulogin")

def deletepoll(request, poll_id):
	if request.user.is_authenticated:
		poll = get_object_or_404(PollModel, pk=poll_id)
		if poll.creator != request.user:
			return render(request, "confirm.html")
		poll.delete()
		return redirect("viewpoll")
	else:
		return redirect("ulogin")

def confirm(request, poll_id):
	if request.user.is_authenticated:
		poll = PollModel.objects.get(pk=poll_id)
		return render(request, "confirm.html", {"poll" : poll})
	else:
		return redirect("ulogin")

def ucp(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			password1 = request.POST.get("pw1")
			password2 = request.POST.get("pw2")
			if password1 == password2:
				try:
					usr = User.objects.get(username=request.user.username)
					usr.set_password(password1)
					usr.save()
					return redirect("ulogin")
				except User.DoesNotExist:
					return render(request, "ucp.html", {"msg":"User does not exists."})
			else:
				return render(request, "ucp.html", {"msg":"Failed, Password did not match."})	
		else: 		
			return render(request, "ucp.html")
	else: 
		return redirect("ulogin")

def ulogout(request):
	logout(request)
	return redirect("uhome")