from .models import Ft_resultado, Dim_area_enquadramento, Dim_curso, Dim_regiao, Dim_ano, Ft_associacao
from rest_framework import serializers

class AreasByCoursers(serializers.Serializer):
    id_curso = serializers.SlugRelatedField(slug_field='id', read_only=True)
    id_area = serializers.SlugRelatedField(slug_field='area', read_only=True)

class ErrosRigaoByCurso(serializers.Serializer):
    id_curso = serializers.SlugRelatedField(slug_field='id', read_only=True)
    id_regiao = serializers.SlugRelatedField(slug_field='regiao', read_only=True)
    volume_incidencias = serializers.IntegerField()
    qtd_questoes = serializers.IntegerField()
    qtd_erradas = serializers.IntegerField()


class HitsRigaoByCurso(serializers.Serializer):
    ano = serializers.SlugRelatedField(slug_field='ano', read_only=True)
    id_curso = serializers.SlugRelatedField(slug_field='id', read_only=True)
    id_regiao = serializers.SlugRelatedField(slug_field='regiao', read_only=True)
    volume_incidencias = serializers.IntegerField()
    qtd_questoes = serializers.IntegerField()
    qtd_certas = serializers.IntegerField()


class ResultadoSerializerAno(serializers.Serializer):
    ano = serializers.SlugRelatedField(slug_field='ano', read_only=True)
    volume_incidencias = serializers.IntegerField()

    class Meta:
        model = Ft_resultado
        fields = ('volume_incidencias', 'ano')


class ResultadoSerializerByAreaQuestions(serializers.Serializer):
    id_area = serializers.SlugRelatedField(slug_field='area', read_only=True)
    qtd_questoes = serializers.IntegerField()

    class Meta:
        model = Ft_resultado
        fields = ('area', 'qtd_questoes')

class ResultadoSerializer(serializers.Serializer):
    ano = serializers.SlugRelatedField(slug_field='ano', read_only=True)
    id_area = serializers.SlugRelatedField(slug_field='area', read_only=True)
    id_curso = serializers.SlugRelatedField(slug_field='curso', read_only=True)
    id_regiao = serializers.SlugRelatedField(slug_field='regiao', read_only=True)
    volume_incidencias = serializers.IntegerField()
    porcentagem_incidencias = serializers.FloatField()
    qtd_questoes = serializers.IntegerField()
    qtd_certas = serializers.IntegerField()
    qtd_erradas = serializers.IntegerField()
    qtd_branco_invalidas = serializers.IntegerField()
    porcentagem_certas = serializers.FloatField()
    porcentagem_erradas = serializers.FloatField()
    porcentagem_branco_invalida = serializers.FloatField()

    class Meta:
        model = Ft_resultado
        fields = ('volume_incidencias', 'porcentagem_incidencias')


class AreaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    area = serializers.CharField()

    class Meta:
        model = Dim_area_enquadramento
        fields = ('id', 'area')


class CursoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    curso = serializers.CharField()

    class Meta:
        model = Dim_curso
        fields = ('id', 'curso')


class RegiaoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    regiao = serializers.CharField()

    class Meta:
        model = Dim_regiao
        fields = ('id', 'regiao')


class AnoSerializer(serializers.Serializer):
    ano = serializers.IntegerField()

    class Meta:
        model = Dim_ano
        fields = ('ano')


class Ft_associacaoSerializer(serializers.Serializer):
    name = serializers.CharField()
    value = serializers.IntegerField()

    class Meta:
        model = Ft_associacao
        fields = '__all__'
