from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name='Category Name')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'
    
class Quiz(models.Model):
    title = models.CharField(max_length=100,verbose_name='Quiz Title')
    category =models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Quizzes'
        


class Update(models.Model):
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Question(Update):
    
    SCALE = (
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced')
    )
    
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    title = models.CharField(max_length=300,verbose_name='question')
    difficulty = models.IntegerField(choices=SCALE)
    date_created = models.DateTimeField(auto_now_add=True)
   
    
    def __str__(self):
        return self.title
    
class Answer(Update):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=250)
    is_right = models.BooleanField(default=False)
   
    
    def __str__(self):
        return self.answer_text
    
    
    