from operator import index
from django.contrib import admin
from django.urls import path
from faperta.views import faperta, tambah_jurusan, ubah_faperta, hapus_faperta
from feb.views import feb, tambah_jurusan, ubah_feb, hapus_feb
from fh.views import fh, tambah_jurusan, ubah_fh, hapus_fh
from fisip.views import fisip, tambah_jurusan, ubah_fisip, hapus_fisip
from fk.views import fk, tambah_jurusan, ubah_fk, hapus_fk
from fkip.views import fkip, tambah_jurusan, ubah_fkip, hapus_fkip
from ft.views import ft, tambah_jurusan, ubah_ft, hapus_ft
from pascasarjana.views import pascasarjana, tambah_jurusan, ubah_pasca, hapus_pasca
from Profil.views import Profil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fkip/', fkip),
    path('faperta/', faperta),
    path('feb/', feb),
    path('fh/', fh),
    path('fisip/', fisip),
    path('fk/', fk),
    path('ft/', ft),
    path('pascasarjana/', pascasarjana),
    path('profil/', Profil),
    path('tambah-jurusan/', tambah_jurusan),
    path('faperta/ubah/<int:id_faperta>', ubah_faperta, name='ubah_faperta'),
    path('faperta/hapus/<int:id_faperta>', hapus_faperta, name="hapus_faperta"),
    path('feb/ubah/<int:id_feb>', ubah_feb, name='ubah_feb'),
    path('feb/hapus/<int:id_feb>', hapus_feb, name="hapus_feb"),
    path('fh/ubah/<int:id_fh>', ubah_fh, name='ubah_fh'),
    path('fh/hapus/<int:id_fh>', hapus_fh, name="hapus_fh"),
    path('fisip/ubah/<int:id_fisip>', ubah_fisip, name='ubah_fisip'),
    path('fisip/hapus/<int:id_fisip>', hapus_fisip, name="hapus_fisip"),
    path('fk/ubah/<int:id_fk>', ubah_fk, name="ubah_fk"),
    path('fk/hapus/<int:id_fk>', hapus_fk, name="hapus_fk"),
    path('fkip/ubah/<int:id_fkip>', ubah_fkip, name='ubah_fkip'),
    path('fkip/hapus/<int:id_fkip>', hapus_fkip, name="hapus_fkip"),
    path('ft/ubah/<int:id_ft>', ubah_ft, name='ubah_ft'),
    path('ft/hapus/<int:id_ft>', hapus_ft, name="hapus_ft"),
    path('pasca/ubah/<int:id_pasca>', ubah_pasca, name='ubah_pasca'),
    path('pasca/hapus/<int:id_pasca>', hapus_pasca, name="hapus_pasca"),
]
