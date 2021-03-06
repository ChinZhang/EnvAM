# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Infotable(models.Model):
    year = models.IntegerField(blank=True, null=True)
    country_name = models.CharField(max_length=45, blank=True, null=True)
    country_code = models.CharField(max_length=45, blank=True, null=True)
    c02pc = models.FloatField(db_column='C02PC', blank=True, null=True)  # Field name made lowercase.
    c02t = models.FloatField(db_column='C02T', blank=True, null=True)  # Field name made lowercase.
    ghgt = models.FloatField(db_column='GHGT', blank=True, null=True)  # Field name made lowercase.
    tpap = models.FloatField(db_column='TPAP', blank=True, null=True)  # Field name made lowercase.
    atep = models.FloatField(db_column='ATEP', blank=True, null=True)  # Field name made lowercase.
    eupc = models.FloatField(db_column='EUPC', blank=True, null=True)  # Field name made lowercase.
    gdppue = models.FloatField(db_column='GDPPUE', blank=True, null=True)  # Field name made lowercase.
    nrpgdp = models.FloatField(db_column='NRPGDP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'infotable'
