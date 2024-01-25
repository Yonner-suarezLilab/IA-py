from ..models.Empleador.tbl_aichamba_empleador import tbl_aichamba_empleador

def create_empleador_from_json(args_dict):
    nuevo_empleador = tbl_aichamba_empleador(
      nombre=args_dict.get("Nombre"),
      email=args_dict.get("Email"),
      apellido=args_dict.get("Apellido"),
      documento=args_dict.get("Documento"),
      direccion=args_dict.get("Direccion"),
      telefono=args_dict.get("Telefono"),
      foto=args_dict.get("Foto"),
      rol=args_dict.get("Rol"),
      activo=1  # O el valor que necesites para activo
      )

    return nuevo_empleador