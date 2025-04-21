class Proyecto:
    
    def __init__(self):
        self.datos_proyecto = {
        "cliente": None, #str
        "codigo_proyecto": None, #str
        "nombre_proyecto": None, #str
        "agencia": None, #str
        "productora": None, #str
        "productor": None, #str
        "director": None #str
        }

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
