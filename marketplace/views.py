from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PhotoCard, Sale, User
from .serializers import PhotoCardSerializer, SaleListSerializer, SaleDetailSerializer, UserSerializer
from django.utils import timezone
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class SaleListView(generics.ListAPIView):
    queryset = Sale.objects.filter(state='sale')
    serializer_class = SaleListSerializer

    @swagger_auto_schema(operation_description="판매중인 포토카드의 리스트를 조회합니다. 중복된 포토카드가 있을 시 가격, 갱신일자 오름차순으로 정렬하여 첫번째 항목을 표출합니다.")
    def get_queryset(self):
        """
        판매중인 포토카드의 리스트를 조회합니다.
        중복된 포토카드가 있을 시 가격, 갱신일자 오름차순으로 정렬하여 첫번째 항목을 표출합니다."
        """
        qs = super().get_queryset()
        unique_photo_cards = qs.values('photo_card_id').distinct()
        result = []
        for photo_card in unique_photo_cards:
            min_price_sale = qs.filter(photo_card_id=photo_card['photo_card_id']).order_by('price', 'renewal_date').first()
            if min_price_sale:
                result.append(min_price_sale)
        return result

class SaleDetailView(generics.RetrieveAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleDetailSerializer
    lookup_field = 'photo_card_id'

    @swagger_auto_schema(operation_description="특정 포토카드의 판매 상세 정보를 조회합니다. 최근 5개의 판매 이력을 함께 제공합니다.")
    def retrieve(self, request, *args, **kwargs):
        """
        특정 포토카드의 판매 상세 정보를 조회합니다.
        최근 5개의 판매 이력을 함께 제공합니다.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        sales_history = Sale.objects.filter(photo_card_id=instance.photo_card_id).order_by('-sold_date')[:5]
        history_serializer = SaleDetailSerializer(sales_history, many=True)
        data = serializer.data
        data['history'] = history_serializer.data
        return Response(data)

class SaleCreateView(generics.CreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleDetailSerializer

    @swagger_auto_schema(operation_description="새로운 포토카드 판매를 등록합니다.")
    def perform_create(self, serializer):
        """
        새로운 포토카드 판매를 등록합니다.
        """
        seller = self.request.user
        photo_card_id = self.request.data.get('photo_card_id')
        price = self.request.data.get('price')
        photo_card = PhotoCard.objects.get(id=photo_card_id)
        serializer.save(seller=seller, photo_card=photo_card, price=price)

class PurchaseView(APIView):

    @swagger_auto_schema(
        operation_description="포토카드를 구매합니다.",
        responses={
            status.HTTP_200_OK: openapi.Response('구매 성공'),
            status.HTTP_400_BAD_REQUEST: openapi.Response('잔액 부족'),
            status.HTTP_404_NOT_FOUND: openapi.Response('상품을 찾을 수 없습니다')
        }
    )
    def post(self, request, sale_id):
        """
        포토카드를 구매합니다.
        """
        try:
            sale = Sale.objects.get(id=sale_id, state='sale')
            buyer = request.user
            if buyer.cash >= sale.price + sale.fee:
                buyer.cash -= sale.price + sale.fee
                sale.buyer = buyer
                sale.state = 'sold'
                sale.sold_date = timezone.now()
                sale.save()
                buyer.save()
                return Response({'status': '구매 성공'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': '잔액 부족'}, status=status.HTTP_400_BAD_REQUEST)
        except Sale.DoesNotExist:
            return Response({'status': '상품을 찾을 수 없습니다'}, status=status.HTTP_404_NOT_FOUND)
