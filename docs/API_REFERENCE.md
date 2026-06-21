# API Reference

## Auth

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register` | Register a new developer |
| POST | `/api/v1/auth/login` | Login and get JWT token |
| POST | `/api/v1/auth/logout` | Logout |
| GET | `/api/v1/auth/me` | Get current user info |

## Sessions

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/sessions/clock-in` | Start a work session |
| POST | `/api/v1/sessions/clock-out` | End current session |
| GET | `/api/v1/sessions` | List my sessions |
| GET | `/api/v1/sessions/active` | Get active session |
| GET | `/api/v1/sessions/{id}` | Get session by ID |

## Reports

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/reports/daily` | Today's report |
| GET | `/api/v1/reports/weekly` | This week's report |
| GET | `/api/v1/reports/monthly` | This month's report |
| GET | `/api/v1/reports/custom` | Custom date range report |
| GET | `/api/v1/reports/export/csv` | Download CSV export |

## Admin

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/admin/developers` | List all developers |
| POST | `/api/v1/admin/developers` | Add a developer |
| PUT | `/api/v1/admin/developers/{id}` | Update developer |
| DELETE | `/api/v1/admin/developers/{id}` | Deactivate developer |
| GET | `/api/v1/admin/sessions` | All sessions |
| GET | `/api/v1/admin/summary` | Global summary |
| GET | `/api/v1/admin/export/csv` | Export all data as CSV |
