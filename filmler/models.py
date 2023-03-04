from django.db import models

# Create your models here.
# Sayfamda filmlerin hangi bilgilerini istiyorsam onun bilgilerini yazıyorum aşağıya:
class Film(models.Model):
    isim = models.CharField(max_length=100)
    resim = models.FileField(upload_to = 'filmler/')

    # Sayfada görüntülemek istediğim bilgi ise filmlerin ismi:
    def __str__(self):
        return self.isim