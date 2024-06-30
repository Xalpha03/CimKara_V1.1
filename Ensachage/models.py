from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EnsachageModel(models.Model):
    """Model definition for MODELNAME."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    livraison = models.IntegerField(blank=True, null=True, default=0)
    casse = models.IntegerField(blank=True, null=True, default=0)
    ensache = models.IntegerField(blank=True, null=True)
    tx_casse = models.FloatField(blank=True, null=True)
    vrack = models.FloatField(blank=True, null=True, default=0)
    created = models.DateField(blank=False)   

    # TODO: Define fields here

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Ensachage'
        verbose_name_plural = 'Ensachage'
    
    def make_ensache(self):
        if self.livraison is not None:
            self.ensache = self.livraison * 20
        # return self.ensache
    
    def make_tx_casse(self):
        if self.livraison != 0 and self.casse !=0:
            self.tx_casse = round((self.casse * 100) / (self.ensache + self.casse), 2)
        else:
            self.tx_casse = 0.0
        # return self.tx_casse
    def save(self, *args, **kwargs):
        self.make_ensache()
        self.make_tx_casse()
        super(EnsachageModel, self).save(*args, **kwargs)