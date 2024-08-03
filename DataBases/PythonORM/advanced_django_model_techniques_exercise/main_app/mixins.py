from django.db import models


class RechargeEnergyMixin(models.Model):
    def recharge_energy(self, amount: int):
        # print(self.energy, amount)
        self.energy += amount

    class Meta:
        abstract = True