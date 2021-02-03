from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import pandas as pd
import psycopg2 as pg

# Create your views here.

from escuelas.models import Unidad_Operativa, Coordinaciones, Municipios, EDOMEX


def ineageojson(request):
    Unidades_Operativas = Unidad_Operativa.objects.all()
    from django.core.serializers import serialize
    string_salida = serialize('geojson', Unidades_Operativas, geometry_field='Geolocalización', fields=[
                              'Clave_Unidad_Operativa', 'Tipo_Unidad_Operativa', 'Nombre_Unidad_Operativa', 'Municipio', 'Coordinación', 'Domicilio', 'Colonia', 'Codigo_Postal'])
    from django.http import HttpResponse
    response = HttpResponse(string_salida, content_type='json')
    response['Access-Control-Allow-Origin'] = '*'
    return response


def ineamapa(request):
    return render(request, 'vistas_escuelas/mapa.html', {})


class HomePageView(TemplateView):
    template_name = 'index.html'


class casa(TemplateView):
    template_name = 'inicio.html'


class webmapi(TemplateView):
    template_name = 'webmap.html'


class rutasmap(TemplateView):
    template_name = 'rutas.html'


def estadis(request):
            # Postgresql
            # Parámetros de conexión
        param_dic = {
            "host": "localhost",
            "database": "postgres",
            "user": "postgres",
            "password": "postgres",
            "port":  5432
        }
        def connect(params_dic):
            """ Conéctese al servidor de la base de datos PostgreSQL """
            conn = None
            try:
                # conectarse al servidor PostgreSQL
                print('Conectado a la base de datos PostgreSQL...')
                conn = pg.connect(**params_dic)
            except (Exception, pg.DatabaseError) as error:
                print(error)
                sys.exit(1)
            print("Conexión exitosa")
            return conn
        def postgresql_to_dataframe(conn, select_query, column_names):
            """
            Transforma una consulta SELECT en un marco de datos de pandas
            """
            cursor = conn.cursor()
            try:
                cursor.execute(select_query)
            except (Exception, pg.DatabaseError) as error:
                print("Error: %s" % error)
                cursor.close()
                return 1
            # Obtenemos una lista de tuplas.
            tupples = cursor.fetchall()
            cursor.close()
            # Solo tenemos que convertirlo en un marco de datos de pandas
            df = pd.DataFrame(tupples, columns=column_names)
            return df
        # Conectarse a la base de datos
        conn = connect(param_dic)
        column_names = ["CVEMUN", "Municipio",
                        "%analfa", "%sinprim", "%sinsec", "%rezago"]
        # Ejecute la consulta "SELECT *"
        data = postgresql_to_dataframe(
            conn, "SELECT cve_geomun, municipio,panalfa,psinprim,psinsec,prezago FROM rezago", column_names)
        data.set_index("CVEMUN", inplace=True)
        data['%analfa'] = [float(x.replace(',', '.')) for x in data['%analfa']]
        data['%sinprim'] = [float(x.replace(',', '.')) for x in data['%sinprim']]
        data['%sinsec'] = [float(x.replace(',', '.')) for x in data['%sinsec']]
        data['%rezago'] = [float(x.replace(',', '.')) for x in data['%rezago']]
        datos = data
        totalconteo=datos[datos.columns[-1]].sum()
        af=datos['%analfa'].values.tolist()
        sp=datos['%sinprim'].values.tolist()
        ss=datos['%sinsec'].values.tolist()
        rz=datos['%rezago'].values.tolist()
        muni=datos['Municipio'].values.tolist()
        contex = {'totalconteo': totalconteo,'rz':rz,'muni':muni,'af':af,'sp':sp,'ss':ss}
        return render(request, 'estadistica.html', contex)


def edomex_datasets(request):
    edo = serialize('geojson', EDOMEX.objects.all())
    return HttpResponse(edo, content_type='json')
