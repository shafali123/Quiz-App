from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default = uuid.uuid4 , editable=False)
    created_at = models.DateField(auto_now_Add=True)
    updated_at = models.DateField(auto_now= True)

    class Meta:
        abstract = True

class Category(BaseModel):
    
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return super().category_name
    


class QuesModel(BaseModel):
    category = models.ForeignKey(Category ,related_name= 'category', on_delete = models.CASCADE)



    question = models.CharField(max_length=200,null=True)
    marks = models.IntegerField(default =5)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)


    def __str__(self):
        return self.question


class Answer(BaseModel):
    question = models.ForeignKey(QuesModel,related_name='question_answer', on_delete = models.CASCADE)
    answer = models.CharField(max_length = 100)
    is_corect = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

    