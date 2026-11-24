from fastapi import HTTPException, status

def require_roles(user: dict, allowed_roles: set[str]) -> None:
    \"\"\"Dependencia lógica inicial. Sustituir user por el contexto autenticado real.\"\"\"
    if not user or user.get("role") not in allowed_roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para realizar esta operación."
        )

def ensure_owner_or_staff(user: dict, resource_user_id: str) -> None:
    if user.get("role") not in {"staff", "admin"} and user.get("id") != resource_user_id:
        raise HTTPException(status_code=403, detail="Acceso denegado.")
