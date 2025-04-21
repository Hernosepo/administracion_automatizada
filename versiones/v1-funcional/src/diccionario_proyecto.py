datos_proyecto = {
    # Datos generales
    "datos_generales" :{
    "cliente": None, #str
    "codigo_proyecto": None, #str
    "nombre_proyecto": None, #str
    "agencia": None, #str
    "productora": None, #str
    "productor": None, #str
    "director": None, #str
    },

    # Terminos contractuales
    "terminos_contractuales":{
    "Medios": None, #str
    "Temporalidad": None, #str o int
    "Vigencia": None, #str o int
    "Territorio": None, #str o int
    },
    # Presupuestos
    "presupuestos": {
    "Protagonista": None, #int
    "Secundario": None, ##int
    "Terciario": None, #int
    "Comision": None, #int o str porque puede ser una observacion o un calculo depende
    },
    # Personajes
    "personajes":{
    "Cantidad protagonico": None, #int
    "Cantidad secundario": None, #int
    "Cantidad Terciario": None, #int
    },
    
    # Fechas importantes
    "fechas_importantes":{
    "fecha_ingreso": None, #fecha
    "inicio_casting": None, #fecha
    "fecha_fitting": None, #fecha
    "inicio_callback": None, #fecha
    "fecha_filmacion": None, #fecha
    },

    # Información técnica para archivos (esto no se bien como iria por el momento)
    "info_tecnica":{
    "tipo_documento": None,
    "fecha_documento": None,
    },

    # Extras
    "extras":{
    "observaciones": None, #str
    "responsable_administrativo": None, #str
    }
}