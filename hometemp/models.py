from django.db import models

class Record(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    home_temp = models.DecimalField(max_digits=4, decimal_places=1)
    outside_temp = models.DecimalField(max_digits=4, decimal_places=1)
    target_temp = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return 'In: %s  Out: %s  Target: %s' % (
            self.home_temp,
            self.outside_temp,
            self.target_temp
        )

    def to_gviz_row(self):
        return (
            self.datetime,
            float(self.home_temp),
            float(self.target_temp),
            float(self.outside_temp),
        )
