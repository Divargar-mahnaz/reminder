from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from common import messages
from ..models.reminder import Reminder
from ...account.serializer.account import UserInfoSerializer


class ReminderPostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Reminder
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Reminder.objects.all(),
                message=messages.UNIQ_REMINDERR,
                fields=['datetime', 'name']
            )
        ]


class ReminderGetSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = UserInfoSerializer(read_only=True)

    class Meta:
        model = Reminder
        fields = '__all__'
