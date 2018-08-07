from django.urls import path
from pastebin.views import PasteCreate, PasteDetail, PasteList, PasteUpdate, PasteDelete

urlpatterns = [
    path('', PasteCreate.as_view(), name='create'),
    path('paste/<int:pk>', PasteDetail.as_view(), name='pastebin_paste_detail'),
    path('pastes/', PasteList.as_view(), name='pastebin_paste_list'),
    path('paste/<int:pk>/edit', PasteUpdate.as_view(), name='pastebin_paste_update'),
    path('paste/<int:pk>/delete', PasteDelete.as_view(), name='pastebin_paste_delete')
]
