from fastapi import APIRouter, Depends, Query
from fastapi.responses import StreamingResponse
from backend.api.dependencies import get_current_user
from backend.services.report_service import ReportService
from backend.services.csv_service import CSVService
from backend.models.database import get_db
from datetime import date

router = APIRouter()


@router.get("/daily")
def daily_report(current_user=Depends(get_current_user), db=Depends(get_db)):
    service = ReportService(db)
    return service.get_daily_report(current_user.id)


@router.get("/weekly")
def weekly_report(current_user=Depends(get_current_user), db=Depends(get_db)):
    service = ReportService(db)
    return service.get_weekly_report(current_user.id)


@router.get("/monthly")
def monthly_report(current_user=Depends(get_current_user), db=Depends(get_db)):
    service = ReportService(db)
    return service.get_monthly_report(current_user.id)


@router.get("/custom")
def custom_report(
    start: date = Query(...),
    end: date = Query(...),
    current_user=Depends(get_current_user),
    db=Depends(get_db),
):
    service = ReportService(db)
    return service.get_custom_report(current_user.id, start, end)


@router.get("/export/csv")
def export_csv(
    start: date = Query(default=None),
    end: date = Query(default=None),
    current_user=Depends(get_current_user),
    db=Depends(get_db),
):
    service = CSVService(db)
    csv_data = service.export_user_csv(current_user.id, start, end)
    return StreamingResponse(
        iter([csv_data]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=report.csv"},
    )
