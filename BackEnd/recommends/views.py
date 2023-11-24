from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import RecommendSerializer
from .models import Recommend
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
import joblib
import pandas as pd
from rest_framework.response import Response
import pickle


# Create your views here.

# 추천 예금, 적금 상품 저장
@api_view(['POST'])
def save_recommendation(request):   
    age = request.data['age']
    salary = int(request.data['salary'].strip())
    money = int(request.data['money'].strip())
    print(age,salary,money)
    print(type(age))

    # 적금 모델 불러오기
    saving_model = joblib.load('recommends/SavedModels/xgboost_saving_model.pkl')

    # 예금 모델 불러오기
    deposit_model = joblib.load('recommends/SavedModels/xgboost_deposit_model.pkl')

    # 실제 사용 시 새로운 데이터에 대한 예측

    new_data = pd.DataFrame({'age_bin': [age], 'salary_bin': [salary], 'money_bin': [money]})
    saving_product = saving_model.predict(new_data)
    deposit_product = deposit_model.predict(new_data)
    print(saving_product)
    print(deposit_product)
  
    print(int(deposit_product[0]),type(int(deposit_product[0])))
    print(int(saving_product[0]),type(int(saving_product[0])))
    recom = {
        'deposit' : int(deposit_product[0]),
        'saving' : int(saving_product[0])
    }

    return Response(recom)
