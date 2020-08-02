from django.test import TestCase
from persons.models import Person
from persons.models import Member

class PersonTestCase(TestCase):
	def setUp(self):
		Member.objects.create(ssn="123456789", firstName="Jude")

	def test_persons(self):
		jude =  Member.objects.get(firstName="Jude")
		self.assertEqual(jude.firstName, "Jude")
		self.assertEqual(jude.ssn, "123456789")


# Create your tests here. 
