from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone

from .models import Question


class QuestionMethodTests(TestCase):
	def test_was_published_recentrly_with_future_question(self):
	'''
	was_published_recentrly() should return flase for question whose pub
	dateis in the future
	'''
	time = timezone.now() + datetime.timedelta(days=30)
	future_question = Question(pub_date=time )
	self.assertEqual(future_question.was_published_recentrly(),False)	