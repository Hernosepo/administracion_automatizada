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