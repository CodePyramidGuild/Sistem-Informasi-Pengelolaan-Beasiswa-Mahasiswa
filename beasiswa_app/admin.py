from django.contrib import admin
from .models import Beasiswa, Mahasiswa

@admin.register(Beasiswa)
class BeasiswaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'deskripsi', 'tanggal_mulai', 'tanggal_selesai')

@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nim', 'email', 'alamat')
