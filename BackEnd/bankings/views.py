from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from .serializers import DepositSerializer, SavingSerializer, RentalLoanOptionSerializer, RentalLoanSerializer, CombinationSerializer
from django.http import JsonResponse    # json 형태로 반환해줌
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Deposit,Saving,RentalLoan,RentalLoanOption
from rest_framework import status



# 예금 리스트 DB에 저장
@api_view(['GET'])
def save_depositlist(request):
    api_key =  settings.API_KEY1 # api 키를 가져옴
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json() # api 데이터를 response에 저장

    # 상품 리스트가 담긴 baseList를 for문으로 조회하면서 데이터를 저장
    for li in response["result"].get("baseList"):
        save_data = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'bank_name' : li.get('kor_co_nm'),
            'deposit_name' : li.get('fin_prdt_nm'),
            'join_way' : li.get('join_way'),
            'join_member' : li.get('join_member'),  
            'option6' : '-',
            'option12' : '-',
            'option24' : '-',
            'option36' : '-',
            'maxoption6' : '-',
            'maxoption12' : '-',
            'maxoption24' : '-',
            'maxoption36' : '-',
        }
        for option in response["result"].get("optionList"):
            if option['fin_prdt_cd'] == save_data['fin_prdt_cd']:
                if option['save_trm'] == '6':
                    save_data['option6'] = option['intr_rate']
                    save_data['maxoption6'] = option['intr_rate2']
                if option['save_trm'] == '12':
                    save_data['option12'] = option['intr_rate'] 
                    save_data['maxoption12'] = option['intr_rate2']
                if option['save_trm'] == '24':
                    save_data['option24'] = option['intr_rate'] 
                    save_data['maxoption24'] = option['intr_rate2']
                if option['save_trm'] == '36':
                    save_data['option36'] = option['intr_rate'] 
                    save_data['maxoption36'] = option['intr_rate2']
        # 묶어줘서 유효하면 저장
        serializer = DepositSerializer(data=save_data)
        if serializer.is_valid():
            serializer.save()
    
    return JsonResponse({'message': 'okay'})



# 적금 리스트 DB에 저장
@api_view(['GET'])
def save_savinglist(request):
    api_key = settings.API_KEY1# api 키를 가져옴
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json() # api 데이터를 response에 저장

     # 상품 리스트가 담긴 baseList를 for문으로 조회하면서 데이터를 저장
    for li in response["result"].get("baseList"):
        save_data = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'bank_name' : li.get('kor_co_nm'),
            'deposit_name' : li.get('fin_prdt_nm'),
            'join_way' : li.get('join_way'),
            'join_member' : li.get('join_member'),  
            'option6' : '-',
            'option12' : '-',
            'option24' : '-',
            'option36' : '-',
            'maxoption6' : '-',
            'maxoption12' : '-',
            'maxoption24' : '-',
            'maxoption36' : '-',
        }
        for option in response["result"].get("optionList"):
            if option['fin_prdt_cd'] == save_data['fin_prdt_cd']:
                if option['save_trm'] == '6':
                    save_data['option6'] = option['intr_rate']
                    save_data['maxoption6'] = option['intr_rate2']
                if option['save_trm'] == '12':
                    save_data['option12'] = option['intr_rate'] 
                    save_data['maxoption12'] = option['intr_rate2']
                if option['save_trm'] == '24':
                    save_data['option24'] = option['intr_rate'] 
                    save_data['maxoption24'] = option['intr_rate2']
                if option['save_trm'] == '36':
                    save_data['option36'] = option['intr_rate'] 
                    save_data['maxoption36'] = option['intr_rate2']
        # 묶어줘서 유효하면 저장
        serializer = SavingSerializer(data=save_data)
        if serializer.is_valid():
            serializer.save()
    return JsonResponse({'message': 'okay'})


# 대출 리스트 DB에 저장
@api_view(['GET'])
def save_rentalloanlist(request):
    api_key = settings.API_KEY1 # api 키를 가져옴
    url = f'http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={api_key}&topFinGrpNo=050000&pageNo=1'
    response = requests.get(url).json() # api 데이터를 response에 저장

    # 상품 리스트가 담긴 baseList를 for문으로 조회하면서 데이터를 저장
    for li in response["result"].get("baseList"):
        save_data = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'bank_name' : li.get('kor_co_nm'),
            'deposit_name' : li.get('fin_prdt_nm'),
            'erly_rpay_fee' : li.get('erly_rpay_fee'),
            'dly_rate' : li.get('dly_rate'),
            'loan_lmt' : li.get('loan_lmt'),
            'join_way' : li.get('join_way'),
            'loan_inci_expn' : li.get('loan_inci_expn'),
            'dcls_strt_day' : li.get('dcls_strt_day'),
            'dcls_end_day' : li.get('dcls_end_day') or 'null',
        }
        # 묶어줘서 유효하면 저장
        serializer = RentalLoanSerializer(data=save_data)
        if serializer.is_valid():
            serializer.save()
    
    # 옵션이 들어가 있는 optionList에서 데이터 조회 및 저장
    for li in response["result"].get("optionList"):
        try:
            # 만약에 지금의 fin_prdt_cd가 있다면, 가져와서 저장
            nowproduct = RentalLoan.objects.get(fin_prdt_cd=li.get('fin_prdt_cd'))
            option_data = {
                    "fin_prdt_cd" : nowproduct.fin_prdt_cd,
                    "rpay_type_nm" : li.get("rpay_type_nm"),
                    "lend_rate_type_nm" : li.get("lend_rate_type_nm"),
                    "lend_rate_min" : li.get("lend_rate_min"),
                    "lend_rate_max" : li.get("lend_rate_max"),
                }
            serializer2 = RentalLoanOptionSerializer(data=option_data)
        # 해당 상품이 없다면, 저장안함
        except RentalLoan.DoesNotExist:
            pass
        if serializer2.is_valid(raise_exception=True):
            serializer2.save(rentalloan=nowproduct)    # 외래키 저장
    
    return JsonResponse({'message': 'okay'})


# 전체 데이터 반환
@api_view(['GET'])
def get_bankings(request):
    deposits = get_list_or_404(Deposit)
    # depositoptions = get_list_or_404(DepositOption)
    savings = get_list_or_404(Saving)
    # savingoptions = get_list_or_404(SavingOption)
    rentalloans = get_list_or_404(RentalLoan)
    rentalloanoptions = get_list_or_404(RentalLoanOption)
    if request.method == 'GET':
        combination = {
            'deposits' : deposits,
            # 'depositoptions' : depositoptions,
            'savings' : savings,
            # 'savingoptions' : savingoptions,
            'rentalloans' : rentalloans,
            'rentalloanoptions' : rentalloanoptions,
        }
        serializer = CombinationSerializer(combination)
        return Response(serializer.data)
    


# 각각 조회
@api_view(['GET'])
def deposit_detail(request, id):
    deposit = get_object_or_404(Deposit,fin_prdt_cd=id)
    serializer = DepositSerializer(deposit)
    return Response(serializer.data)

@api_view(['GET'])
def saving_detail(request, id):
    saving = get_object_or_404(Saving,fin_prdt_cd=id)
    serializer = SavingSerializer(saving)
    return Response(serializer.data)

@api_view(['GET'])
def rentalloan_detail(request, id):
    rentalloan = get_object_or_404(RentalLoan,fin_prdt_cd=id)
    serializer = RentalLoanSerializer(rentalloan)
    return Response(serializer.data)