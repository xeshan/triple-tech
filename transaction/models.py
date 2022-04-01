from django.db import models
import uuid

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_eligible = models.BooleanField(default=False)
    program_name = models.TextField(null=False)
    currency = models.TextField(null=False)
    country_name = models.TextField(null=False)
    bank_name = models.TextField(null=False)

    def __str__(self):
        return f"{self.program_name} {self.currency} {self.country_name} {self.bank_name}"
