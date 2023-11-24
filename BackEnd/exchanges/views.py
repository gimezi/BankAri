from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Exchange
from .serializers import ExchangeSerializer
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated
import pandas as pd
import requests
from django.http import Http404
from django.conf import settings

# Create your views here.

#  https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=AUTHKEY1234567890&searchdate=20180102&data=AP01

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def exchange(request):
    if request.method == 'GET':

        authkey = settings.API_KEY2
        searchdate = '20231101'
        data = 'AP01'
        url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={authkey}&searchdate={searchdate}&data={data}'
        response = requests.get(url)
        r_data = response.json()
        exchanage_rate_summary = pd.DataFrame(r_data)
        
        for i in range(23):
            exchange = exchanage_rate_summary['bkpr'][i]
            exchange = int(exchange.replace(",",""))
            tmp = {
                "nation" :  exchanage_rate_summary['cur_unit'][i],
                "unit" : exchanage_rate_summary["cur_nm"][i],
                "price" : exchange
            }
            serializer = ExchangeSerializer(data=tmp)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

        return JsonResponse({'message':'okay'})


@api_view(['GET'])
def store(request):
    if request.method == 'GET':
        exchanges = get_list_or_404(Exchange)
        serializer = ExchangeSerializer(exchanges,many=True)
        # if serializer.is_valid(raise_exception=True):
        #         serializer.save()
        return Response(serializer.data) 
    
# 환율 데이터 찾기
@api_view(['GET'])
def search(request, nation):
    if request.method == 'GET':
        try:
            exchange = Exchange.objects.get(nation=nation)
        except Exchange.DoesNotExist:
            raise Http404("Exchange 객체를 찾을 수 없습니다.")

        except Exchange.MultipleObjectsReturned:
            # 여러 객체가 반환된 경우 처리. 예를 들어 첫 번째 객체를 사용할 수 있습니다.
            exchange = Exchange.objects.filter(nation=nation).first()

        serializer = ExchangeSerializer(exchange)
        return Response(serializer.data)