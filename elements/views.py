from django.shortcuts import render, get_object_or_404
from .models import Paper, Method, ValueResult, Dataset, \
                    Metric, Link, LinkType, PaperType, TextResult


def paper_view(request, paper_id):
  paper = get_object_or_404(Paper, pk=paper_id)
  # TODO: rewrite as SQL so that it is always fast?
  results = ValueResult.objects.filter(paper_id=paper_id)
  # datasets - dict of metrics, metric - list of method, value
  # TODO: make a unittest to check this functionality
  datasets_results = {}
  for result in results:
    if result.dataset not in datasets_results:
      datasets_results[result.dataset] = {}
    if result.metric not in datasets_results[result.dataset]:
      datasets_results[result.dataset][result.metric] = []
    datasets_results[result.dataset][result.metric].append(
      (result.method, result.value),
    )
  results_for_template = {}
  for dataset, metrics_dict in datasets_results.items():
    results_for_template[dataset] = (sorted(metrics_dict.keys()), [])
    results_lists = []
    for metric in results_for_template[dataset][0]:
      results_lists.append(
        sorted(metrics_dict[metric], key=lambda x: x[0].short_name),
      )
    # TODO: add support for not equal lists
    for result_tuples in zip(*results_lists):
      results_row = [result_tuples[0][0]]
      for result_tuple in result_tuples:
        results_row.append(result_tuple[1])
      results_for_template[dataset][1].append(results_row)

  context = {
    'paper': paper,
    'authors': paper.authors.all().order_by('authorship__order_number'),
    'methods': Method.objects.filter(paper_id=paper_id),
    'value_results': results_for_template,
    'text_results': TextResult.objects.filter(paper_id=paper_id),
    'links_to_current': Link.objects.filter(dst_paper_id=paper_id),
    'links_from_current': Link.objects.filter(src_paper_id=paper_id),
  }
  return render(request, "elements/paper.html", context)


def method_view(request, method_id):
  method = get_object_or_404(Method, pk=method_id)
  context = {'method': method}
  return render(request, "elements/method.html", context)


def text_result_view(request, text_result_id):
  text_result = get_object_or_404(TextResult, pk=text_result_id)
  context = {'result': text_result}
  return render(request, "elements/text_result.html", context)


def dataset_view(request, dataset_id):
  dataset = get_object_or_404(Dataset, pk=dataset_id)
  context = {'dataset': dataset}
  return render(request, "elements/dataset.html", context)


def metric_view(request, metric_id):
  metric = get_object_or_404(Metric, pk=metric_id)
  context = {'metric': metric}
  return render(request, "elements/metric.html", context)


def link_type_view(request, link_type_id):
  link_type = get_object_or_404(LinkType, pk=link_type_id)
  context = {'link_type': link_type}
  return render(request, "elements/link_type.html", context)


def paper_type_view(request, paper_type_id):
  paper_type = get_object_or_404(PaperType, pk=paper_type_id)
  context = {'paper_type': paper_type}
  return render(request, "elements/paper_type.html", context)
