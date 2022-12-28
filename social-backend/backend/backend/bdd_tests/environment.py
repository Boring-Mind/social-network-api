import coverage
from rest_framework.test import APIClient

from backend.bdd_tests.bdd_utils import reload_modules


def django_ready(context):
    """Hook that will run on a per-scenario basis.

    If you want to have some fixtures or factories that have to be created
    at the beginning of each scenario, you can put them here.
    """
    context.test.client = APIClient()


def before_all(context):
    cov = coverage.Coverage()
    cov.start()
    context.cov = cov

    reload_modules()


def after_all(context):
    cov = context.cov
    cov.stop()
    cov.save()
    cov.html_report(directory="./cov")
