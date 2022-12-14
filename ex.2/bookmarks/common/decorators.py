from django.http import HttpResponseBadRequest


def is_ajax(request):
    pass


def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__ =f.__doc__
    wrap.__name__=f.__name__
    return wrap