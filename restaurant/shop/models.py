from django.db import models

class Categorie(models.Model):

    nume = models.CharField(max_length=50)

    def __str__(self):
        return self.nume

# Create your models here.
class Produs(models.Model):

    nume = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    pret = models.IntegerField()
    descriere = models.CharField(max_length=200)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nume} - {self.pret} - {self.descriere}"

class Livrare(models.Model):
    produse = models.ManyToManyField(Produs)
    adresa = models.CharField(max_length=200)
    numar_telefon=models.IntegerField()
    metoda_plata=models.CharField(max_length=20)


    def __str__(self):
        return f"Livrare pentru adresa: {self.adresa}, numar telefon: {self.numar_telefon}, metoda plata: {self.metoda_plata}, status: {self.status}"


