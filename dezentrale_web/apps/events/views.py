from django.http import JsonResponse


def example(request):
    data = [
        {
            'title': 'event1',
            'start': '2010-01-01'
        },
        {
            'title': 'event2',
            'start': '2010-01-05',
            'end': '2010-01-07'
        }
    ]
    return JsonResponse(data, safe=False)
