import inspect
import importlib


def reload_modules():
    """Reload Django application modules.

    The time before_all() is executed seems to be later than the time
    when Django loads the modules set in each app. So sometimes it is necessary
    to reload django app’s modules for accurate test coverage measurement.

    More on that here: https://behave-django.readthedocs.io/en/latest/testcoverage.html#warning-for-behave-django
    """
    import api

    for app in [api]:
        members = inspect.getmembers(app)
        modules = map(
            lambda keyval: keyval[1],
            filter(lambda keyval: inspect.ismodule(keyval[1]), members),
        )
        for module in modules:
            try:
                importlib.reload(module)
            except:
                continue
