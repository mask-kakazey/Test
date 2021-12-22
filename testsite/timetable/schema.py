import graphene
from graphene_django import DjangoObjectType
from .models import Training


class TrainingType(DjangoObjectType):
    class Meta:
        model = Training
        fields = ('id', 'name', 'start')


class Query(graphene.ObjectType):
    all_training = graphene.List(TrainingType)
    one_training = graphene.Field(TrainingType, id=graphene.Int())
    training_at_the_time = graphene.List(TrainingType, l_time=graphene.DateTime(), r_time=graphene.DateTime())

    @staticmethod
    def resolve_all_training(root, info):
        return Training.objects.all()

    @staticmethod
    def resolve_one_training(root, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Training.objects.get(pk=id)
        return None

    @staticmethod
    def resolve_training_at_the_time(root, info, **kwargs):
        l_time = kwargs.get('l_time')
        r_time = kwargs.get('r_time')
        if l_time and r_time is not None:
            return Training.objects.filter(start__gte=l_time, start__lte=r_time)


schema = graphene.Schema(query=Query)
