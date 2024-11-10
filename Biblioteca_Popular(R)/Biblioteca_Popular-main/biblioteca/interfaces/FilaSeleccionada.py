from PrestamosMostrar import *



    
    seleccionado = grilla_prestamos.selection()
    
   
    if seleccionado:
        item = seleccionado[0]
        valores = grilla_prestamos.item(item, 'values')
        return valores
    else:
        return None
