from django.test import TestCase
from .models import Choice

# Create your tests here.
class ChoiceTest(TestCase):
    #testchoice = Choice.objects.get(choice_text='Les paul')
    def testingchoice(self):
        testchoice = Choice(choice_text='sibal', vote_cnt=20)
        self.assertIs(testchoice.vote_morethan_10(), True)

    