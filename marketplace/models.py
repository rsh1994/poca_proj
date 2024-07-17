from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone

# 기본 User 테이블
class User(AbstractUser):
    # 유저는 기본 10,000원을 제공하는 것으로 합니다
    cash = models.DecimalField(max_digits=10, decimal_places=2, default=10000.00)
    
    groups = models.ManyToManyField(
        Group,
        related_name='marketplace_Users',
        blank=True,
        help_text='유저의 그룹관리',
        related_query_name='User'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='marketplace_Users',
        blank=True,
        help_text='유저 권한관리',
        related_query_name='User'
    )

class PhotoCard(models.Model):
    name = models.CharField(max_length=255)

class Sale(models.Model):
    STATE_CHOICES = [
        ('sale', '판매중'),
        ('sold', '판매완료'),
    ]

    photo_card = models.ForeignKey(PhotoCard, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='sale')
    buyer = models.ForeignKey(User, related_name='purchases', null=True, blank=True, on_delete=models.SET_NULL)
    seller = models.ForeignKey(User, related_name='sales', on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)
    renewal_date = models.DateTimeField(auto_now=True)
    sold_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # 가격의 20%를 수수료로 계산합니다.
        self.fee = self.price * 0.2
        super().save(*args, **kwargs)
