from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
#from google.cloud import bigquery
import re

def index(request):
    return render(request, 'b7ssof/index.html', {})

@csrf_exempt
def analsys(request):

    param_question = request.POST.get('param_question')

    print("param_question: "+param_question)
    #todo 구문분석후 통계작업...
    #accepted_answers_title_summary 이게 타이틀을 쪼개서 리턴하는 sql 입니다.
    #딱요기까지가 빅쿼리가 가능하고 위미없는 단어 제외하고 하는건 뒷단에서 해야될거 같아요
    #젠체 데이터셋중에서 질문자가 채택한 답변만을 모은거에요

    words = param_question.split(" ")

    replacestr = ','.join("'{0}'".format(x) for x in words)

    #replacestr = re.sub(r'\s', r',', param_question)

    print(replacestr)

    for word in words:
        print(word)


    return render(request, 'b7ssof/analsys.html', {})


def rank(request):
    # https://datastudio.google.com/open/13tM_ZV-pkFeCuv9SvvL-fT-lNMzi5c7g
    # https://datastudio.google.com/open/1bzBULr6TDCtjRCeBcDF4vctHehapbrNo
    # https://datastudio.google.com/open/1NGM28cSXqDPxTfvv9MkJ_-zD7ziAAAdb
    # https://datastudio.google.com/open/1wBqUOuiG9dkHzv0oPLQdZnZiZKNbBDax
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