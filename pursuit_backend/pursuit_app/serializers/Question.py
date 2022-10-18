from rest_framework import serializers
from pursuit_app.models import Question
from . Score import ScoreSerializer
                            
class QuestionSerializer(serializers.ModelSerializer) :

    # score = ScoreSerializer(many=True)

    class Meta :
        model = Question
        fields = '__all__'
