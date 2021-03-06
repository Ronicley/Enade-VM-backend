from django.urls import path

from plataforma_api import views

urlpatterns = [
    path('resultados', views.ResultList.as_view()),
    path('areas', views.AreaList.as_view()),
    path('cursos', views.CursosList.as_view()),
    path('regioes', views.RegioesList.as_view()),
    path('anos', views.AnoList.as_view()),
    path('resultados/<int:id_curso>', views.ResultByCursoList.as_view()),
    path('resultados-por-anos', views.ResultByAno.as_view()),
    path('resultados/<int:ano>/<int:id_curso>', views.ResultByAnoAndCurso.as_view()),
    path('resultados/<int:ano>/<int:curso>/<int:area>', views.ResultByAnoCursoAndArea.as_view()),
    path('resultados-associacao/<int:ano>/<int:id_curso>', views.Ft_associacaoList.as_view()),
    path('errosbyregion/<int:ano>', views.ResultForCourseThatHadMoreErrorsByRegion.as_view()),
    path('hitsbyregion/<int:ano>', views.ResultForCourseThatHadMoreHitsByRegion.as_view()),
    path('nullsbyregion/<int:ano>', views.ResultForCourseThatHadMoreNullsByRegion.as_view()),
    path('number-of-questions-by-area', views.ResultNumberOfQuestionsByArea.as_view()),
    path('students-by-region/<int:ano>/<int:province>', views.ResultStudentsByAno.as_view()),
    path('result-by-areas-for-coursers', views.ResultByAreasForCoursers.as_view()),

]
