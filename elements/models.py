from django.db import models


class Dataset(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=2000)

  def __str__(self):
    return self.name


class Metric(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=2000)
  # TODO: add automatically checked range?

  def __str__(self):
    return self.name


class Author(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class Conference(models.Model):
  title = models.CharField(max_length=300)
  short_title = models.CharField(max_length=30)

  def __str__(self):
    return self.short_title


class Paper(models.Model):
  title = models.CharField(max_length=200)
  problem = models.TextField(max_length=500)
  solution = models.TextField(max_length=2000)
  conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
  text_url = models.URLField()
  code_url = models.URLField(blank=True)
  project_url = models.URLField(blank=True)
  date_published = models.DateField(verbose_name="publication date")

  DATASET_TYPE = 0
  METHOD_TYPE = 1
  THEORY_TYPE = 2
  TYPE_CHOICES = (
      (DATASET_TYPE, 'Dataset'),
      (METHOD_TYPE, 'Method'),
      (THEORY_TYPE, 'Theory'),
  )

  type = models.IntegerField(choices=TYPE_CHOICES)
  authors = models.ManyToManyField(Author)

  def __str__(self):
    return self.title


class Method(models.Model):
  title = models.CharField(max_length=100)
  short_title = models.CharField(max_length=20)
  description = models.TextField(max_length=3200)
  orig_paper = models.ForeignKey(
      Paper, on_delete=models.CASCADE, verbose_name='Original elements',
  )

  def __str__(self):
    return self.short_title


class Result(models.Model):
  value = models.FloatField()
  dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
  metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
  paper = models.ForeignKey(Paper, on_delete=models.CASCADE)

  def __str__(self):
    return "{}/{}/{:.2f}".format(self.dataset.name, self.metric.name, self.value)
