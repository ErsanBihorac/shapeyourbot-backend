from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "repeated_password"]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def save(self):
        pw = self.validated_data["password"]
        repeated_pw = self.validated_data["repeated_password"]
        email = self.validated_data["email"]
        username = self.validated_data["username"]

        if pw != repeated_pw:
            raise serializers.ValidationError({"error": "Passwords do not match"})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "Please use a different email to register"})
        
        account = User(email=email, username=username)
        account.set_password(pw)
        account.save()
        return account
    
class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ["username", "email", "new_password"]

    def save(self):
        new_password = self.validated_data["new_password"]
        email = self.validated_data["email"]
        username = self.validated_data["username"]
        
        if not User.objects.filter(email=email, username=username).exists():
            raise serializers.ValidationError({"error": "This user doesn't exist"})

        user = User.objects.get(email=email, username=username)
        user.set_password(new_password)
        user.save()
        return user