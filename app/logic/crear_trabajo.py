from ..models.Empleador.tbl_aichamba_trabajos import tbl_aichamba_trabajos


def crear_trabajo(data, latitud, longitud):
    nuevo_trabajo = tbl_aichamba_trabajos(
        idempleador=data.get("idEmpleador"),
        descripcion=data.get("Descripcion"),
        imagen=data.get("Imagen"),
        latitud=latitud,
        longitud=longitud
    )

    return nuevo_trabajo