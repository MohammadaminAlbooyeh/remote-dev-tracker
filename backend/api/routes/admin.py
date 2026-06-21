from fastapi import APIRouter, Depends, HTTPException
from backend.api.schemas import UserCreate, UserResponse
from backend.api.dependencies import get_admin_user
from backend.models.database import get_db
from backend.services.auth_service import AuthService
from backend.services.report_service import ReportService
from backend.services.csv_service import CSVService
from fastapi.responses import StreamingResponse

router = APIRouter(dependencies=[Depends(get_admin_user)])


@router.get("/developers", response_model=list[UserResponse])
def list_developers(db=Depends(get_db)):
    service = AuthService(db)
    return service.get_all_developers()


@router.post("/developers", response_model=UserResponse)
def add_developer(payload: UserCreate, db=Depends(get_db)):
    service = AuthService(db)
    return service.register(payload)


@router.put("/developers/{dev_id}", response_model=UserResponse)
def update_developer(dev_id: str, payload: dict, db=Depends(get_db)):
    service = AuthService(db)
    user = service.update_profile(dev_id, payload)
    if not user:
        raise HTTPException(status_code=404, detail="Developer not found")
    return user


@router.delete("/developers/{dev_id}")
def deactivate_developer(dev_id: str, db=Depends(get_db)):
    service = AuthService(db)
    service.deactivate(dev_id)
    return {"message": "Developer deactivated"}


@router.get("/sessions")
def all_sessions(db=Depends(get_db)):
    service = ReportService(db)
    return service.get_all_sessions()


@router.get("/summary")
def summary(db=Depends(get_db)):
    service = ReportService(db)
    return service.get_global_summary()


@router.get("/export/csv")
def export_csv(db=Depends(get_db)):
    service = CSVService(db)
    csv_data = service.export_all_csv()
    return StreamingResponse(
        iter([csv_data]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=all_reports.csv"},
    )
