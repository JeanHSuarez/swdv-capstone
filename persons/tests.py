from django.test import TestCase
from persons.models import Person
from persons.models import Employee

class PersonTestCase(TestCase):
	def setUp(self):
		Employee.objects.create(ssn="123456789", firstName="Jude")

	def test_persons(self):
		jude =  Animal.objects.get(firstName="Jude")
		self.assertEqual(jude.ssn(), "123456789")


# Create your tests here. 
