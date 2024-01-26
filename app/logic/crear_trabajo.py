from ..models.Empleador.tbl_aichamba_trabajos import tbl_aichamba_trabajos


def crear_trabajo(data):
    nuevo_trabajo = tbl_aichamba_trabajos(
        idempleador=data.get("idEmpleador"),
        descripcion=data.get("Descripcion"),       
      )

    return nuevo_trabajo