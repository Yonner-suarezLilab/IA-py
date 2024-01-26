from ..models.Empleador.tbl_aichamba_trabajos_postulaciones import tbl_aichamba_trabajos_postulaciones


def crear_postulacion(data):
    nueva_postulacion = tbl_aichamba_trabajos_postulaciones(
        idtrabajo=data.get("id_trabajo"),
        idempleado=data.get("id_empleado"),
        activo=1
      )

    return nueva_postulacion