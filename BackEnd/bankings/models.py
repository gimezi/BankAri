from django.db import models

# 정기 예금
class Deposit(models.Model):
    # 금융 상품 코드(pk)
    fin_prdt_cd = models.TextField(primary_key=True)
    # 금융 회사 이름
    bank_name = models.CharField(max_length=300)
    # 금융 상품 명
    deposit_name = models.TextField()
    # 가입방법
    join_way = models.TextField()
    # 가입 대상
    join_member = models.TextField()
    # 옵션(6, 12, 24, 36)
    option6 = models.TextField(default='-')
    option12 = models.TextField(default='-')
    option24 = models.TextField(default='-')
    option36 = models.TextField(default='-')
    # 최고 우대 금리(6, 12, 24, 36)
    maxoption6 = models.TextField(default='-')
    maxoption12 = models.TextField(default='-')
    maxoption24 = models.TextField(default='-')
    maxoption36 = models.TextField(default='-')
    


# 정기 적금
class Saving(models.Model):
    # 금융 상품 코드
    fin_prdt_cd = models.TextField(primary_key=True)
    # 금융 회사 이름
    bank_name = models.CharField(max_length=300)
    # 금융 상품 명
    deposit_name = models.TextField()
    # 가입방법
    join_way = models.TextField()
    # 가입 대상
    join_member = models.TextField()
    # 옵션(6, 12, 24, 36)
    option6 = models.TextField(default='-')
    option12 = models.TextField(default='-')
    option24 = models.TextField(default='-')
    option36 = models.TextField(default='-')
    # 최고 우대 금리(6, 12, 24, 36)
    maxoption6 = models.TextField(default='-')
    maxoption12 = models.TextField(default='-')
    maxoption24 = models.TextField(default='-')
    maxoption36 = models.TextField(default='-')



# 전세 자금 대출
class RentalLoan(models.Model):
    # 금융 상품 코드(pk)
    fin_prdt_cd = models.TextField(primary_key=True)
    # 금융 회사 이름
    bank_name = models.CharField(max_length=300)
    # 금융 상품 명
    deposit_name = models.TextField()
    # 중도상환 수수료
    erly_rpay_fee = models.TextField()
    # 연체 이자율
    dly_rate = models.TextField()
    # 대출 한도
    loan_lmt = models.TextField()
    # 가입 방법
    join_way = models.TextField()
    # 대출 부대비용
    loan_inci_expn = models.TextField()
    # 공시 시작일
    dcls_strt_day = models.TextField()
    # 공시 종료일
    dcls_end_day = models.TextField()

class RentalLoanOption(models.Model):
    # 해당 상품
    rentalloan = models.ForeignKey(RentalLoan, related_name='options', on_delete=models.CASCADE)
    # 금융 상품 코드
    fin_prdt_cd = models.TextField()
    # 대출 상환 유형
    rpay_type_nm = models.TextField()
    # 대출 금리 유형
    lend_rate_type_nm = models.TextField()
    # 대출 금리(최저)
    lend_rate_min = models.FloatField()
    # 대출 금리(최고)
    lend_rate_max = models.FloatField()
    