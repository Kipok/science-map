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
  name = models.CharField(max_length=255)
  short_name = models.CharField(max_length=30)

  def __str__(self):
    return self.short_name


class PaperType(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=3200)

  def __str__(self):
    return self.name


class Paper(models.Model):
  title = models.CharField(max_length=200)
  problem = models.TextField(max_length=500)
  solution = models.TextField(max_length=2000)
  conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
  text_url = models.URLField()
  code_url = models.URLField(blank=True)
  project_url = models.URLField(blank=True)
  date_published = models.DateField(verbose_name="publication date")

  types = models.ManyToManyField(PaperType)
  authors = models.ManyToManyField(Author, through='Authorship')

  def __str__(self):
    return self.title


class Authorship(models.Model):
  paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  order_number = models.IntegerField()


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
  visual_description = models.ImageField(upload_to='uploads', blank=True)

  def __str__(self):
    return self.short_name


class ValueResult(models.Model):
  value = models.FloatField()
  dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
  metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
  method = models.ForeignKey(Method, on_delete=models.CASCADE)
  paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
  # TODO: how to display?
  configuration = models.TextField(max_length=1000, blank=True)
  # TODO: add check that there are no two results for the same method/dataset
  # TODO: think about rewriting it in the actual format:
  #       dataset: list of metrics, list of methods-values

  def __str__(self):
    return "{}/{}/{}/{:.2f}".format(self.dataset.name, self.method.name,
                                    self.metric.name, self.value)


class TextResult(models.Model):
  short_description = models.CharField(max_length=100)
  detailed_description = models.TextField(max_length=3000)
  visual_description = models.ImageField(upload_to='uploads', blank=True)
  paper = models.ForeignKey(Paper, on_delete=models.CASCADE)

  def __str__(self):
    return self.short_description


class LinkType(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=3200)

  def __str__(self):
    return self.name


class Link(models.Model):
  # TODO: add check that can't link to itself
  type = models.ForeignKey(LinkType, on_delete=models.CASCADE)
  src_paper = models.ForeignKey(
    Paper,
    on_delete=models.CASCADE,
    related_name='src_paper'
  )
  dst_paper = models.ForeignKey(
    Paper,
    on_delete=models.CASCADE,
    related_name='dst_paper',
  )

  def __str__(self):
    return "{}--{}--{}".format(
      self.src_paper.title, self.type, self.dst_paper.title,
    )
