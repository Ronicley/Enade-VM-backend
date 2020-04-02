from rest_framework import generics
from django.db.models import Q
from plataforma_api.serializers import *
from .models import Ft_resultado, Dim_area_enquadramento, Dim_curso, Dim_regiao, \
    Dim_ano, Ft_associacao


class ResultList(generics.ListAPIView):
    queryset = Ft_resultado.objects.all()
    serializer_class = ResultadoSerializer


class ResultByCursoList(generics.ListAPIView):
    serializer_class = ResultadoSerializer

    def get_queryset(self):
        curso = self.kwargs['id_curso']
        return Ft_resultado.objects.filter(id_curso=curso)


class ResultByRegiaoList(generics.ListAPIView):
    serializer_class = ResultadoSerializer

    def get_queryset(self):
        regiao = self.kwargs['id_regiao']
        return Ft_resultado.objects.filter(id_regiao=regiao)


class ResultByCursoAndArea(generics.ListAPIView):
    serializer_class = ResultadoSerializer

    def get_queryset(self):
        curso = self.kwargs['id_curso']
        area = self.kwargs['id_area']
        return Ft_resultado.objects.filter(id_curso=curso).filter(id_area=area)


class ResultForCourseThatHadMoreErrorsByRegion(generics.ListAPIView):
    serializer_class = ErrosRigaoByCurso

    def get_queryset(self):
        regiao = self.kwargs['id_regiao']
        curso = self.kwargs['id_curso']
        ftResult = Ft_resultado
        objetos = ftResult.objects

        return objetos.filter(id_regiao=regiao).filter(porcentagem_erradas__gt=0.0).filter(id_curso=curso)


class ResultByAnoAndCurso(generics.ListAPIView):
    serializer_class = ResultadoSerializer

    def get_queryset(self):
        ano = self.kwargs['ano']
        curso = self.kwargs['id_curso']
        return Ft_resultado.objects.filter(ano=ano).filter(id_curso=curso)


class ResultByAnoCursoAndArea(generics.ListAPIView):
    serializer_class = ResultadoSerializer

    def get_queryset(self):
        ano = self.kwargs['ano']
        curso = self.kwargs['curso']
        area = self.kwargs['area']
        return Ft_resultado.objects.filter(ano=ano).filter(id_curso=curso).filter(id_area=area).order_by('qtd_certas',
                                                                                                         'qtd_erradas')


class AreaList(generics.ListAPIView):
    serializer_class = AreaSerializer

    def get_queryset(self):
        return Dim_area_enquadramento.objects.all()[:12]


class CursosList(generics.ListAPIView):
    queryset = Dim_curso.objects.all()
    serializer_class = CursoSerializer


class RegioesList(generics.ListAPIView):
    queryset = Dim_regiao.objects.all()
    serializer_class = RegiaoSerializer


class AnoList(generics.ListAPIView):
    queryset = Dim_ano.objects.all()
    serializer_class = AnoSerializer


class Ft_associacaoList(generics.ListAPIView):
    serializer_class = Ft_associacaoSerializer

    def get_queryset(self):
        curso = self.kwargs['id_curso']
        ano_id = self.kwargs['ano']
        return Ft_associacao.objects.filter(id_curso=curso, ano=ano_id)
