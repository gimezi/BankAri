from rest_framework import serializers
from .models import Deposit, Saving, RentalLoan, RentalLoanOption

# class DepositOptionSerializer(serializers.ModelSerializer):
#     deposit = serializers.ReadOnlyField(source='deposit.fin_prdt_cd')
#     class Meta:
#         model = DepositOption
#         fields = '__all__'

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

# class SavingOptionSerializer(serializers.ModelSerializer):
#     saving = serializers.ReadOnlyField(source='Saving.saving')
#     class Meta:
#         model = SavingOption
#         fields = '__all__'

class SavingSerializer(serializers.ModelSerializer):
    # options = SavingOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Saving
        fields = '__all__'

class RentalLoanOptionSerializer(serializers.ModelSerializer):
    rentalloan = serializers.ReadOnlyField(source='RentalLoan.rentalloan')
    class Meta:
        model = RentalLoanOption
        fields = '__all__'

class RentalLoanSerializer(serializers.ModelSerializer):
    # RentalLoanOption_set = RentalLoanOptionSerializer(many=True, read_only=True)
    options = RentalLoanOptionSerializer(many=True, read_only=True)
    class Meta:
        model = RentalLoan
        fields = '__all__'

class CombinationSerializer(serializers.Serializer):
    deposits = DepositSerializer(many=True)
    # depositoptions = DepositOptionSerializer(many=True)
    savings = SavingSerializer(many=True)
    # savingoptions = SavingOptionSerializer(many=True)
    rentalloans = RentalLoanSerializer(many=True)
    rentalloanoptions = RentalLoanOptionSerializer(many=True)
    