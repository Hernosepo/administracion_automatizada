from pathlib import Path
import shutil

class Proyecto:

    def __init__(self):
        # Datos generales
        self.datos_proyecto = {
        "cliente": None, #str
        "codigo_proyecto": None, #str
        "nombre_proyecto": None, #str
        "agencia": None, #str
        "productora": None, #str
        "productor": None, #str
        "director": None #str
        }

        # Terminos contractuales
        self.terminos_contractuales = {
        "Medios": None, #str
        "Temporalidad": None, #str o int
        "Vigencia": None, #str o int
        "Territorio": None #str o int
        }

        # Presupuestos
        self.presupuestos = {
        "Protagonista": None, #int
        "Secundario": None, ##int
        "Terciario": None, #int
        "Comision": None #int o str porque puede ser una observacion o un calculo depende
        }
    
        # Personajes
        self.personajes = {
        "cantidad_protagonico": None, #int
        "cantidad_secundario": None, #int
        "cantidad_terciario": None #int
        }
    
        # Fechas importantes
        self.fechas_importantes = {
        "fecha_ingreso": None, #fecha
        "inicio_casting": None, #fecha
        "fecha_fitting": None, #fecha
        "inicio_callback": None, #fecha
        "fecha_filmacion": None #fecha
        }

        # Información técnica para archivos (esto no se bien como iria por el momento)
        self.info_tecnica = {
        "tipo_documento": None,
        "fecha_documento": None
        }

        # Extras
        self.extras = {
        "observaciones": None, #str
        "responsable_administrativo": None #str
        }

    def mostrar_estado(self):
        print('DATOS GENERALES')
        print(self.datos_proyecto)
        print('\nTERMINOS CONTRACTUALES')
        print(self.terminos_contractuales)
        print('\nPRESUPUESTOS')
        print(self.presupuestos)
        print('\nPERSONAJES')
        print(self.personajes)
        print('\nFECHAS IMPORTANTES')
        print(self.fechas_importantes)
        print('\nINFO TECNICA')
        print(self.info_tecnica)
        print('\nEXTRAS')
        print(self.extras)
    
    def capturar_datos_interactivamente(self):
        for nombre_bloque, bloque in [
            ('DATOS GENERALES', self.datos_proyecto),
            ('TERMINOS CONTRACTUALES', self.terminos_contractuales),
            ('PRESUPUESTOS', self.presupuestos),
            ('PERSONAJES', self.personajes),
            ('FECHAS IMPORTANTES', self.fechas_importantes),
            ('INFO TECNICA', self.info_tecnica),
            ('EXTRAS', self.extras)
        ]:
            print(f"\n--- {nombre_bloque} ---")
            for campo in bloque:
                valor = input(f"Ingresá {campo}: ").strip()
                bloque[campo] = valor

    def crear_documento_desde_template(self, nombre_template="orden_compra_modelo.txtt", carpeta_destino="/Users/hernangeller/Shamoun Dropbox/Hernan Geller/ACTIVIDADES/DEVELOPMENT/PROYECTOS/ADMINISTRACION AUTOMATIZADA/administracion_automatizada/versiones/v2-orientado-objetos/src"):
        # Definir rutas
        origen = Path("templates") / nombre_template
    
        if not origen.exists():
            print(f"⚠️ El archivo de plantilla no existe: {origen}")
            return

        # Generar nombre final del archivo
        nombre_archivo = f"{self.datos_proyecto['codigo_proyecto']}_{self.datos_proyecto['cliente']}_{self.datos_proyecto['nombre_proyecto']}_ORDEN.txt"
        nombre_archivo = nombre_archivo.replace(" ", "").upper()  # Limpieza opcional
    
        # Definir ruta destino
        destino = Path(carpeta_destino) / nombre_archivo

        # Copiar el archivo
        shutil.copy(origen, destino)
        print(f"✅ Documento creado: {destino}")

    def crear_estructura_carpetas(self, base_path="."):
        carpeta_principal_nombre = (f"{self.datos_proyecto['codigo_proyecto']}_{self.datos_proyecto['cliente']}_{self.datos_proyecto['nombre_proyecto']}")
        carpeta_principal_nombre = carpeta_principal_nombre.upper().replace(" ", "")
        carpeta_principal = Path(base_path) / carpeta_principal_nombre
        carpeta_principal.mkdir(parents=True, exist_ok=True)

        estructuras = {
        'TALENTO': {
            'CONTRACTUALES': {
                'CONTRATOS': {},
                'SOLICITUDES DE CASTING': {},
                'SELECCION DE TALENTO': {},
            },
            'CIERRE TALENTO':{},
            'ORDENES DE COMPRA Y PORTADA TALENTO': {},
        },
        'PROVEEDORES':{
            'CIERRE PROVEEDORES': {},
            'ORDENES DE COMPRA PROVEEDORES': {},
        },    
        'CIERRE GENERAL': {},
        }

        def crear_subcarpetas(base_path, estructura):
            for nombre, subestructura in estructura.items():
                nueva_ruta = base_path / nombre
                nueva_ruta.mkdir(exist_ok=True)
            crear_subcarpetas(nueva_ruta, subestructura)    