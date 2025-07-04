from rest_framework import serializers
from .models import ExpenseIncome

class ExpenseAndIncomeSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ExpenseIncome
        fields = ['id', 'title', 'description', 'amount', 'transaction_type', 'tax', 'tax_type', 'created_at', 'updated_at', 'total']
        read_only_fields = ['id', 'created_at', 'updated_at', 'total']

    def get_total(self, obj):
        return obj.total

class ExpenseListSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = ExpenseIncome
        fields = ['id', 'title', 'amount', 'transaction_type', 'total', 'created_at']

    def get_total(self, obj):
        return obj.total