from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
#additional attributes to include
	website = models.URLField(blank=True)
	picture= models.ImageField(upload_to='profile_images',blank=True)
	def __unicode__(self):
		return self.user.username

	
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
		return self.question_text
	
class Choice(models.Model):
	
	question = models.ForeignKey(Question , on_delete = models.CASCADE)
	choise_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0 )
	def __unicode__(self):
		return self.choise_text