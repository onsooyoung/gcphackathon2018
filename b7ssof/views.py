from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
#from google.cloud import bigquery

def index(request):
    return render(request, 'b7ssof/index.html', {})

@csrf_exempt
def analsys(request):

    param_question = request.POST.get('param_question')

    print("param_question: "+param_question)
    #todo 구문분석후 통계작업...

    return render(request, 'b7ssof/analsys.html', {})


def rank(request):
    return render(request, 'b7ssof/rank.html',{})

"""
def getTagRank():
    bigquery_client = bigquery.Client()
    query = ('SELECT rank, tag, cnt, percentage FROM {}.{} LIMIT 10'
            .format( 'stackoverflow_summary', 'tag_rank'))

    try:
        query_job = bigquery_client.query(query)

    except Exception as e:
        print("Error")
        print(e)

"""