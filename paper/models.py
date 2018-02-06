from django.db import models


class Method(models.Model):
    title = models.CharField(max_length=100)
    short_title = models.CharField(max_length=20)
    description = models.CharField(max_length=3000)
    orig_paper = models.ForeignKey(
        'Paper', on_delete=models.CASCADE, verbose_name='Original paper',
    )

    def __str__(self):
        return self.short_title

# class Result(models.Model):
#     value = models.FloatField()


class Paper(models.Model):
    title = models.CharField(max_length=200)
    problem = models.TextField(max_length=500)
    solution = models.TextField(max_length=2000)

    DATASET_TYPE = 0
    METHOD_TYPE = 1
    THEORY_TYPE = 2
    TYPE_CHOICES = (
        (DATASET_TYPE, 'Dataset'),
        (METHOD_TYPE, 'Method'),
        (THEORY_TYPE, 'Theory'),
    )

    type = models.IntegerField(choices=TYPE_CHOICES)
    methods = models.ManyToManyField(Method, blank=True)

    def __str__(self):
        return self.title
