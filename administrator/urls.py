from django.urls import path
from .views import administrator_view, view_user, tx_user, edit_user, update_tx_status, update_stock

urlpatterns = [
    path('',administrator_view, name="administrator_view"),
    path('view_user/<id>', view_user, name="view_user"),
    path('tx_user/<tx_num>', tx_user, name="tx_user"),
    path('edit_user/<id>', edit_user, name="edit_user"),
    path('update_tx_status/<id>/<tx_num>', update_tx_status, name="update_tx_status"),
    path('update_stock', update_stock, name="update_stock")
]