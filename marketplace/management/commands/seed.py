from django.core.management.base import BaseCommand
from marketplace.models import User, PhotoCard, Sale
from django.utils import timezone

class Command(BaseCommand):
    help = '예시데이터 추가'

    def handle(self, *args, **kwargs):
        user1 = User.objects.create_user(username='user1', password='password1')
        user2 = User.objects.create_user(username='user2', password='password2')
        user3 = User.objects.create_user(username='user3', password='password3')

        pc1 = PhotoCard.objects.create(name='PhotoCard1')
        pc2 = PhotoCard.objects.create(name='PhotoCard2')

        Sale.objects.create(photo_card=pc1, price=1000, fee=200, state='sale', seller=user2, create_date=timezone.now(), renewal_date=timezone.now())
        Sale.objects.create(photo_card=pc2, price=2000, fee=400, state='sale', seller=user3, create_date=timezone.now(), renewal_date=timezone.now())
        Sale.objects.create(photo_card=pc1, price=3000, fee=600, state='sold', seller=user1, buyer=user2, create_date=timezone.now(), renewal_date=timezone.now(), sold_date=timezone.now())
        Sale.objects.create(photo_card=pc2, price=4000, fee=800, state='sold', seller=user2, buyer=user3, create_date=timezone.now(), renewal_date=timezone.now(), sold_date=timezone.now())
