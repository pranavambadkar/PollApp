from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def get_default_creator():
	default_user = User.objects.get(username="demotest")
	return default_user.id

class PollModel(models.Model):
	creator = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_creator)
	question = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	op1 = models.CharField(max_length=50)
	op2 = models.CharField(max_length=50)
	op3 = models.CharField(max_length=50)
	op1c = models.IntegerField(default=0)
	op2c = models.IntegerField(default=0)
	op3c = models.IntegerField(default=0)

	def total(self):
		return self.op1c + self.op2c + self.op3c

class DemoModel(models.Model):
	ques = models.TextField()
	option_one = models.CharField(max_length=50)
	option_two = models.CharField(max_length=50)
	option_three = models.CharField(max_length=50)
	option_one_count = models.IntegerField(default=0)
	option_two_count = models.IntegerField(default=0)
	option_three_count = models.IntegerField(default=0)

	def total(self):
		return self.option_one_count + self.option_two_count + self.option_three_count

class SocialMedia(models.Model):
	linkedin_url  = models.URLField()
	github_url  = models.URLField()
	instagram_url  = models.URLField()


