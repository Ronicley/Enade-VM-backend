from django.urls import path

from plataforma_api import views

urlpatterns = [
    path('resultados', views.ResultList.as_view()),
    path('areas', views.AreaList.as_view()),
    path('cursos', views.CursosList.as_view()),
    path('regioes', views.RegioesList.as_view()),
    path('anos', views.AnoList.as_view()),
    path('resultados/<int:id_curso>', views.ResultByCursoList.as_view()),
    path('resultados-por-anos/<int:ano>', views.ResultByAno.as_view()),
    path('resultados/<int:ano>/<int:id_curso>', views.ResultByAnoAndCurso.as_view()),
    path('resultados/<int:ano>/<int:curso>/<int:area>', views.ResultByAnoCursoAndArea.as_view()),
    path('resultados-associacao/<int:ano>/<int:id_curso>', views.Ft_associacaoList.as_view()),
    path('errosbyregion/<int:id_regiao>/<int:id_curso>', views.ResultForCourseThatHadMoreErrorsByRegion.as_view()),
    path('hitsbyregion/<int:id_regiao>/<int:id_curso>', views.ResultForCourseThatHadMoreHitsByRegion.as_view()),
    path('number-of-questions-by-area', views.ResultNumberOfQuestionsByArea.as_view()),
]
