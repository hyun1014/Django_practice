from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=50)
    vote_cnt = models.IntegerField(verbose_name='vote count', default=0)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    def vote_morethan_10(self):
        if self.vote_cnt>10:
            return True
        else:
            return False

    def __str__(self):
        return self.choice_text