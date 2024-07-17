from django.urls import path
from .views import SaleListView, SaleDetailView, SaleCreateView, PurchaseView

urlpatterns = [
    path('sales/', SaleListView.as_view(), name='sale-list'), # 판매 목록 테이블 List 조회
    path('sales/<int:photo_card_id>/', SaleDetailView.as_view(), name='sale-detail'), # 판매 목록 테이블 Detail 조회
    path('sales/create/', SaleCreateView.as_view(), name='sale-create'), # 판매 등록
    path('sales/purchase/<int:sale_id>/', PurchaseView.as_view(), name='sale-purchase'), # 포토카드 구매
]