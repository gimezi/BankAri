from django.db import models
# from django.conf import settings

class Exchange(models.Model):
    # 국가 코드
    nation = models.CharField(max_length=100)
    # 국가당 화폐 단위
    unit = models.TextField(max_length=100)
    # 1원당 금액
    price = models.TextField()