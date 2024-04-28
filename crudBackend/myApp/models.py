from django.db import models
import uuid
# Create your models here.

class baseClass(models.Model):
    uid=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True


class Clients(baseClass):
    g=[ ('m',"Male"), ('f',"Female")]
    full_name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    roll_no=models.CharField(max_length=15, default="noRollNo")
    address=models.TextField()
    gender=models.CharField(choices=g, max_length=2, default="m")
    phone=models.IntegerField()
    mail=models.EmailField(max_length=100, default="no@mail.com")

    def __str__(self) -> str:
        return self.full_name