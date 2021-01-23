from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('Flooring & Staircase','Flooring & Staircase'),
    ('Carving', 'Carving'),
    ('Home & Garden Decor','Home & Garden Decor'),
    ('Inlay', 'Inlay'),
    ('Home Mandir','Home Mandir'),
    ('Wall Cladding','Wall Cladding'),
    ('Qibla & Mimbar', 'Qibla & Mimbar'),
    ('Jali', 'Jali'),
    ('Katera & Kabr', 'Katera & Kabr'),
    ('Railing', 'Railing'),
    ('Name Plate', 'Name Plate'),
)

class Project(models.Model):
    tag = models.FloatField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='images/project', null=False, blank=False)

    def __str__(self):
        return f'{self.tag}: ({self.category})'

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)