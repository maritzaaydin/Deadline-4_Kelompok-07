from django.urls import path
from . import views

urlpatterns = [
    path('penyewa',views.penyewa,name='penyewa'),
    path('createdatapenyewa',views.createdatapenyewa,name='createdatapenyewa'),
    path('updatepenyewa/<str:id>', views.updatepenyewa,name='updatepenyewa'),
    path('karyawan',views.karyawan,name='karyawan'),
    path('createdatakaryawan',views.createdatakaryawan,name='createdatakaryawan'),
    path('updatekaryawan/<str:id>', views.updatekaryawan,name='updatekaryawan'),
    path('jenismobil',views.jenismobil,name='jenismobil'),
    path('createdatajenismobil',views.createdatajenismobil,name='createdatajenismobil'),
    path('updatejenismobil/<str:id>', views.updatejenismobil,name='updatejenismobil'),
    path('mobil',views.mobil,name='mobil'),
    path('createdatamobil',views.createdatamobil,name='createdatamobil'),
    path('updatemobil/<str:id>', views.updatemobil,name='updatemobil'),
    path('penyewaan',views.penyewaan,name='penyewa'),
    path('createdatapenyewaan',views.createdatapenyewaan,name='createdatapenyewaan'),
    path('updatepenyewaan/<str:id>', views.updatepenyewaan,name='updatepenyewaan'),
]