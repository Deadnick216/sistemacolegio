"""
URL configuration for sistemaColegio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sistema_Colegio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login_estudiante/', views.login_estudiante_view, name='login_estudiante'),
    path('login_docente/', views.login_docente_view, name='login_docente'),
    path('login_nodocente/', views.login_nodocente_view, name='login_nodocente'),
    path('estudiante_menu/', views.estudiante_menu, name='estudiante_menu'),
    path('docente_menu/', views.docente_menu, name='docente_menu'),
    path('nodocente_menu/', views.nodocente_menu, name='nodocente_menu'),
    path('admin_menu/', views.admin_menu_view, name='admin_menu'),
    path('create_estudiante/', views.create_estudiante_view, name='create_estudiante'),
    path('create_docente/', views.create_docente_view, name='create_docente'),
    path('create_nodocente/', views.create_nodocente_view, name='create_nodocente'),
    path('create_asignatura/', views.create_asignatura_view, name='create_asignatura'),
    path('assign_asignatura/', views.assign_asignatura_view, name='assign_asignatura'),
    path('assign_docente/<int:asignatura_id>/', views.assign_docente_view, name='assign_docente'),
    path('list_estudiantes/', views.list_estudiantes_view, name='list_estudiantes'),
    path('list_asignaturas/', views.list_asignaturas_view, name='list_asignaturas'),
    path('list_docentes/', views.list_docentes_view, name='list_docentes'),
    path('list_eventos/', views.list_eventos_view, name='list_eventos'),
    path('select_estudiante/', views.select_estudiante_view, name='select_estudiante'),
    path('create_evento/', views.create_evento_view, name='create_evento'),
    path('registro_asistencia/<int:asignatura_id>/', views.registro_asistencia, name='registro_asistencia'),
    path('select_asignatura/', views.select_asignatura_view, name='select_asignatura'),
    path('asistencia_matriz/<int:asignatura_id>/', views.asistencia_matriz_view, name='asistencia_matriz'),
    path('list_asistencia/', views.list_asistencia_view, name='list_asistencia'),
    path('select_estudiante_anotacion/', views.select_estudiante_anotacion_view, name='select_estudiante_anotacion'),
    path('create_anotacion/<int:estudiante_id>/', views.create_anotacion_view, name='create_anotacion'),
    path('select_asignatura_nota/', views.select_asignatura_nota_view, name='select_asignatura_nota'),
    path('create_nota/<int:asignatura_id>/', views.create_nota_view, name='create_nota'),
    path('ver_notas_estudiante/', views.ver_notas_estudiante_view, name='ver_notas_estudiante'),
    path('reporte_asistencia/', views.reporte_asistencia_view, name='reporte_asistencia'),
    path('reporte_notas/', views.reporte_notas_view, name='reporte_notas'),
    path('reporte_anotaciones/', views.reporte_anotaciones_view, name='reporte_anotaciones'),
    path('estadisticas_rendimiento/', views.estadisticas_rendimiento_view, name='estadisticas_rendimiento'),
    path('list_notas/<int:asignatura_id>/', views.list_notas_view, name='list_notas'),
    path('perfil_estudiante/<int:estudiante_id>/', views.perfil_estudiante_view, name='perfil_estudiante'),
    path('select_estudiante_reporte_asistencia/', views.select_estudiante_reporte_asistencia_view, name='select_estudiante_reporte_asistencia'),
    path('reporte_asistencia_estudiante/<int:estudiante_id>/', views.reporte_asistencia_estudiante_view, name='reporte_asistencia_estudiante'),
    path('generar_word_asistencia/<int:estudiante_id>/', views.generar_word_asistencia_view, name='generar_word_asistencia'),
    path('select_estudiante_reporte_notas/', views.select_estudiante_reporte_notas_view, name='select_estudiante_reporte_notas'),
    path('reporte_notas_estudiante/<int:estudiante_id>/', views.reporte_notas_estudiante_view, name='reporte_notas_estudiante'),
    path('generar_word_notas/<int:estudiante_id>/', views.generar_word_notas_view, name='generar_word_notas'),
    path('select_estudiante_reporte_anotaciones/', views.select_estudiante_reporte_anotaciones_view, name='select_estudiante_reporte_anotaciones'),
    path('reporte_anotaciones_estudiante/<int:estudiante_id>/', views.reporte_anotaciones_estudiante_view, name='reporte_anotaciones_estudiante'),
    path('generar_word_anotaciones/<int:estudiante_id>/', views.generar_word_anotaciones_view, name='generar_word_anotaciones'),
    path('select_estudiante_certificado/', views.select_estudiante_certificado_view, name='select_estudiante_certificado'),
    path('generar_word_certificado/<int:estudiante_id>/', views.generar_word_certificado_view, name='generar_word_certificado'),
    path('select_estudiante_reporte_completo/', views.select_estudiante_reporte_completo_view, name='select_estudiante_reporte_completo'),
    path('generar_word_reporte_completo/<int:estudiante_id>/', views.generar_word_reporte_completo_view, name='generar_word_reporte_completo'),
    path('ver_asignaturas_notas/', views.ver_asignaturas_notas, name='ver_asignaturas_notas'),
    path('ver_anotaciones/', views.ver_anotaciones, name='ver_anotaciones'),
    path('ver_eventos/', views.ver_eventos, name='ver_eventos'),
    path('list_nodocentes/', views.list_nodocentes_view, name='list_nodocentes'),  
    path('edit_estudiante/<int:estudiante_id>/', views.edit_estudiante_view, name='edit_estudiante'),
    path('create_reclamo/', views.create_reclamo_view, name='create_reclamo'),
    path('ver_reclamos_docente/', views.ver_reclamos_docente_view, name='ver_reclamos_docente'),
]