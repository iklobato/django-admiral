from django.db import models

class AllFieldTypes(models.Model):
    # Numeric Fields
    integer_field = models.IntegerField(default=0)
    positive_integer = models.PositiveIntegerField(default=0)
    small_integer = models.SmallIntegerField(default=0)
    big_integer = models.BigIntegerField(default=0)
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2)
    float_field = models.FloatField(default=0.0)


