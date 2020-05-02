import json

from rest_framework import generics
from django.db.models import Q, Sum, Count
from plataforma_api.serializers import *
from .models import Ft_resultado, Dim_area_enquadramento, Dim_curso, Dim_regiao, \
    Dim_ano, Ft_associacao
from django.http import JsonResponse, HttpResponse


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

    def get(self, request, *args, **kwargs):
        year = self.kwargs['ano']
        regiao_id = list(Dim_regiao.objects.all().values_list('id', flat=True))
        regiao_name = list(Dim_regiao.objects.all().values_list('regiao', flat=True))
        curso_id = list(Dim_curso.objects.all().values_list('id', flat=True))
        total = []

        if (year == 1):
            for i in regiao_id:
                porcentagemcc = 0;
                porcentagemss = 0;
                porcentagemeng = 0;
                for j in curso_id:

                    result = Ft_resultado.objects.filter(Q(id_curso=j) & Q(id_regiao=i)).aggregate(
                        qtd_erradas=Sum('qtd_erradas'), qtd_questoes=Sum('qtd_questoes'))

                    if j == 1:
                        qtd_erradas = int(result.get('qtd_erradas'))
                        qtd_questoes = int(result.get('qtd_questoes'))
                        porcentagemcc = (qtd_erradas / qtd_questoes) * 100
                    elif j == 2:
                        qtd_erradas = int(result.get('qtd_erradas'))
                        qtd_questoes = int(result.get('qtd_questoes'))
                        porcentagemss = (qtd_erradas / qtd_questoes) * 100
                    elif j == 3:
                        qtd_erradas = int(result.get('qtd_erradas'))
                        qtd_questoes = int(result.get('qtd_questoes'))
                        porcentagemeng = (qtd_erradas / qtd_questoes) * 100

                total.append(json.loads(
                    '{"regiao": "' + str(regiao_name[i - 1]) + '", "cc": ' + str(
                        round(porcentagemcc, 2)) + ', "ss": ' + str(
                        round(porcentagemss, 2)) + ', "eng": ' + str(round(porcentagemeng, 2)) + ' }'))
        else:
            for i in regiao_id:
                porcentagemcc = 0;
                porcentagemss = 0;
                porcentagemeng = 0;
                for j in curso_id:

                    result = Ft_resultado.objects.filter(Q(id_curso=j) & Q(id_regiao=i) & Q(ano=year)).aggregate(
                        qtd_erradas=Sum('qtd_erradas'), qtd_questoes=Sum('qtd_questoes'))

                    if j == 1:
                        qtd_erradas = int(result.get('qtd_erradas'))
                        qtd_questoes = int(result.get('qtd_questoes'))
                        porcentagemcc = (qtd_erradas / qtd_questoes) * 100
                    elif j == 2:
                        qtd_erradas = int(result.get('qtd_erradas'))
                        qtd_questoes = int(result.get('qtd_questoes'))
                        porcentagemss = (qtd_erradas / qtd_questoes) * 100
                    elif j == 3:
                        qtd_erradas = int(result.get('qtd_erradas'))
                        qtd_questoes = int(result.get('qtd_questoes'))
                        porcentagemeng = (qtd_erradas / qtd_questoes) * 100

                total.append(json.loads(
                    '{"regiao": "' + str(regiao_name[i - 1]) + '", "cc": ' + str(
                        round(porcentagemcc, 2)) + ', "ss": ' + str(
                        round(porcentagemss, 2)) + ', "eng": ' + str(round(porcentagemeng, 2)) + ' }'))

        return JsonResponse(total, safe=False)


class ResultForCourseThatHadMoreHitsByRegion(generics.ListAPIView):
    serializer_class = ErrosRigaoByCurso

    def get(self, request, *args, **kwargs):
        regiao_id = list(Dim_regiao.objects.all().values_list('id', flat=True))
        regiao_name = list(Dim_regiao.objects.all().values_list('regiao', flat=True))
        curso_id = list(Dim_curso.objects.all().values_list('id', flat=True))
        total = []
        porcentagemcc = 0;
        porcentagemss = 0;
        porcentagemeng = 0;
        year = self.kwargs['ano']

        if (year == 1):

            for i in regiao_id:

                for j in curso_id:

                    result = Ft_resultado.objects.filter(Q(id_curso=j) & Q(id_regiao=i)).aggregate(
                        qtd_certas=Sum('qtd_certas'), qtd_questoes=Sum('qtd_questoes'))

                    if j == 1:
                        qtd_certas = int(result.get('qtd_certas'))
                        qtd_questoes = int(result.get('qtd_questoes'))
                        porcentagemcc = (qtd_certas / qtd_questoes) * 100
                    elif j == 2:
                        qtd_certas = int(result.get('qtd_certas'))
                        qtd_questoes = int(result.get('qtd_questoes'))
                        porcentagemss = (qtd_certas / qtd_questoes) * 100
                    elif j == 3:
                        qtd_certas = int(result.get('qtd_certas'))
                        qtd_questoes = int(result.get('qtd_questoes'))
                        porcentagemeng = (qtd_certas / qtd_questoes) * 100

                total.append(json.loads(
                    '{"regiao": "' + str(regiao_name[i - 1]) + '", "cc": ' + str(
                        round(porcentagemcc, 2)) + ', "ss": ' + str(
                        round(porcentagemss, 2)) + ', "eng": ' + str(round(porcentagemeng, 2)) + ' }'))
        else:
            for i in regiao_id:
                for j in curso_id:
                    result = Ft_resultado.objects.filter(Q(id_curso=j) & Q(id_regiao=i) & Q(ano=year)).aggregate(
                        qtd_certas=Sum('qtd_certas'), qtd_questoes=Sum('qtd_questoes'))

                    if j == 1:
                        qtd_certas = int(result.get('qtd_certas'))
                        qtd_questoes = int(result.get('qtd_questoes'))
                        porcentagemcc = (qtd_certas / qtd_questoes) * 100
                    elif j == 2:
                        qtd_certas = int(result.get('qtd_certas'))
                        qtd_questoes = int(result.get('qtd_questoes'))
                        porcentagemss = (qtd_certas / qtd_questoes) * 100
                    elif j == 3:
                        qtd_certas = int(result.get('qtd_certas'))
                        qtd_questoes = int(result.get('qtd_questoes'))
                        porcentagemeng = (qtd_certas / qtd_questoes) * 100

                total.append(json.loads(
                    '{"regiao": "' + str(regiao_name[i - 1]) + '", "cc": ' + str(
                        round(porcentagemcc, 2)) + ', "ss": ' + str(
                        round(porcentagemss, 2)) + ', "eng": ' + str(round(porcentagemeng, 2)) + ' }'))

        return JsonResponse(total, safe=False)


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


# class ResultByAno(generics.ListCreateAPIView):
#     serializer_class = ResultadoSerializerAno

#     def get(self, request, *args, **kwargs):
#         anos = list(Dim_ano.objects.all().values_list('ano', flat=True))        
#         results2008=''
#         results2011=''
#         results2014=''

#         for i in anos:            
#             if i == '2008':
#                 results2008 = Ft_resultado.objects.filter(ano=i).aggregate(volume_incidencias=Sum('volume_incidencias')
#             elif i =='2011':
#                 results2011 = Ft_resultado.objects.filter(ano=i).aggregate(volume_incidencias=Sum('volume_incidencias')
#             elif i == '2014':
#                 results2014 = Ft_resultado.objects.filter(ano=i).aggregate(volume_incidencias=Sum('volume_incidencias')

#         result = json.loads(
#             '{"ano2008" : '+ str(results2008.get('volume_incidencias')) +
#             ',"ano2011" : '+ str(results2008.get('volume_incidencias')) +
#             ',"ano2014" : '+ str(results2008.get('volume_incidencias')) +
#             '}'
#         )

#         return JsonResponse(result)


class ResultByAno(generics.ListCreateAPIView):
    serializer_class = ResultadoSerializerAno

    def get(self, request, *args, **kwargs):
        result = json.loads(
            '{"ano2008": 47459,  "ano2011": 27253 , "ano2014": 28336}'
        )

        return JsonResponse(result)


class AreaList(generics.ListAPIView):
    serializer_class = AreaSerializer

    def get_queryset(self):
        return Dim_area_enquadramento.objects.all()[:12]


class ResultStudentsByAno(generics.ListAPIView):
    serializer_class = ResultadoSerializer

    def get(self, request, *args, **kwargs):
        ano = self.kwargs['ano']
        result = []

        if ano == 1:
            result.append(json.loads('{"norte" : 5811 }'))
            result.append(json.loads('{"nordeste" : 16303 }'))
            result.append(json.loads('{"centrooeste" : 9968 }'))
            result.append(json.loads('{"sudeste" :  53096}'))
            result.append(json.loads('{"sul" : 17881 }'))

        elif ano == 2008:
            result.append(json.loads('{"norte" : 2338 }'))
            result.append(json.loads('{"nordeste" : 6404 }'))
            result.append(json.loads('{"centrooeste" : 4728 }'))
            result.append(json.loads('{"sudeste" :  25269}'))
            result.append(json.loads('{"sul" : 8724 }'))

        elif ano == 2011:
            result.append(json.loads('{"norte" : 1330 }'))
            result.append(json.loads('{"nordeste" : 4383 }'))
            result.append(json.loads('{"centrooeste" : 2660 }'))
            result.append(json.loads('{"sudeste" :  14439}'))
            result.append(json.loads('{"sul" : 4445 }'))

        elif ano == 2014:
            result.append(json.loads('{"norte" : 2143 }'))
            result.append(json.loads('{"nordeste" : 5517 }'))
            result.append(json.loads('{"centrooeste" : 2580 }'))
            result.append(json.loads('{"sudeste" :  13388}'))
            result.append(json.loads('{"sul" : 4712 }'))

        return JsonResponse(result, safe=False)


class ResultStudentsByAno(generics.ListAPIView):
    serializer_class = ResultadoSerializer

    def get(self, request, *args, **kwargs):
        ano = self.kwargs['ano']
        regions = list(Dim_regiao.objects.all().values_list('id', flat=True))
        regions_name = list(Dim_regiao.objects.all().values_list('regiao', flat=True))
        result = []
        if ano == 1:
            for i in regions:
                results = Ft_resultado.objects.filter(Q(id_regiao=i)).aggregate(volume_incidencias=Sum('volume_incidencias')
                )
                result.append(json.loads('{"' + str(regions_name[i - 1]).replace('-', '').lower() + '" : ' + str(results.get('volume_incidencias')) + '}'))
        elif ano == 2008:
            for i in regions:
                results = Ft_resultado.objects.filter(Q(id_regiao=i) & Q(ano=ano)).aggregate(volume_incidencias=Sum('volume_incidencias'))
                result.append(json.loads('{"' + str(regions_name[i - 1]).replace('-', '').lower() + '" : ' + str( results.get('volume_incidencias')) + '}'))
        elif ano == 2011:
            for i in regions:
                results = Ft_resultado.objects.filter(Q(id_regiao=i) & Q(ano=ano)).aggregate(volume_incidencias=Sum('volume_incidencias'))
                result.append(json.loads('{"' + str(regions_name[i - 1]).replace('-', '').lower() + '" : ' + str(results.get('volume_incidencias')) + '}'))
        elif ano == 2014:
            for i in regions:
                results = Ft_resultado.objects.filter(Q(id_regiao=i) & Q(ano=ano)).aggregate(volume_incidencias=Sum('volume_incidencias'))
                result.append(json.loads('{"' + str(regions_name[i - 1]).replace('-', '').lower() + '" : ' + str(results.get('volume_incidencias')) + '}' ))
        return JsonResponse(result, safe=False)


class ResultNumberOfQuestionsByArea(generics.ListAPIView):
    serializer_class = ResultadoSerializerByAreaQuestions

    def get(self, request, *args, **kwargs):
        lista = []

        lista.append(
            json.loads(
                '{"area":"Area", "qtd_questoes": "Areas" }'
            )
        )
        for i in (range(1, 13)):
            total = list(
                Ft_resultado.objects.filter(id_area=i).filter(Q(id_regiao_id=4)).values('qtd_questoes').distinct())

            area = str(Dim_area_enquadramento.objects.values_list('area', flat=True).filter(id=i))
            a = area.replace("<QuerySet ['", '').replace("']>", '')
            count = 0
            for j in total:
                count = count + int(j.get('qtd_questoes'))

            lista.append(
                json.loads(
                    '{"area":"' + a + '", "qtd_questoes": ' + str(count) + '}'
                )
            )

        return JsonResponse(lista, safe=False)


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
