from ..models.Empleado.tbl_aichamba_empleado import tbl_aichamba_empleado


def create_empleado_from_json(args_dict):
   
    nuevo_empleado = tbl_aichamba_empleado(
    nombre=args_dict.get("Name"),
    email=args_dict.get("Email"),
    apellido=args_dict.get("Apellido"),
    documento=args_dict.get("Documento"),
    ocupacion=args_dict.get("Ocupacion"),
    reputacion=args_dict.get("Reputacion"),
    direccion=args_dict.get("Direccion"),
    telefono=args_dict.get("Telefono"),
    imagen=args_dict.get("Imagen"),
    rol=args_dict.get("Rol"),
    trabajos_realizados=args_dict.get("TrabajosRealizados"),
    resumen=args_dict.get("Resumen"),
    latitud=args_dict.get("Latitud"),
    longitud=args_dict.get("Longitud")
    )

    return nuevo_empleado
