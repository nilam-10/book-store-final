from django.urls import path
from .views import (
    RegisterView, LoginView, LogoutView, BookListView, BookDetailView,
    AddToCartView, CartView, RemoveFromCartView, AdminPanelView,
    AdminBookCreateView, AdminBookEditView, AdminBookDeleteView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('cart/add/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('admin/', AdminPanelView.as_view(), name='admin_panel'),
    path('admin/book/create/', AdminBookCreateView.as_view(), name='admin_book_create'),
    path('admin/book/edit/<int:pk>/', AdminBookEditView.as_view(), name='admin_book_edit'),
    path('admin/book/delete/<int:pk>/', AdminBookDeleteView.as_view(), name='admin_book_delete'),
]