from django.db import models


class Metric(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=2000)
  # TODO: add automatically checked range?
  # TODO: add some field for useful link(s). Also might be useful in other places

  def __str__(self):
    return self.name


class Author(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class Conference(models.Model):
  name = models.CharField(max_length=300)
  short_name = models.CharField(max_length=30)

  def __str__(self):
    return self.short_name


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


class Dataset(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=2000)
  paper = models.ForeignKey(Paper, on_delete=models.CASCADE)

  def __str__(self):
    return self.name


class Method(models.Model):
  name = models.CharField(max_length=100)
  short_name = models.CharField(max_length=20)
  description = models.TextField(max_length=3200)
  paper = models.ForeignKey(
      Paper, on_delete=models.CASCADE, verbose_name='Original elements',
  )

  def __str__(self):
    return self.short_name


class Result(models.Model):
  value = models.FloatField()
  dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
  metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
  method = models.ForeignKey(Method, on_delete=models.CASCADE)
  paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
  # TODO: add check that there are no two results for the same method/dataset
  # TODO: think about rewriting it in the actual format:
  #       dataset: list of metrics, list of methods-values

  def __str__(self):
    return "{}/{}/{}/{:.2f}".format(self.dataset.name, self.method.name,
                                    self.metric.name, self.value)
