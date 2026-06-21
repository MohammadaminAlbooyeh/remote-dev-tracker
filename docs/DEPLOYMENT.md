# Deployment

## Local Development

1. Clone the repo:
   ```bash
   git clone https://github.com/MohammadaminAlbooyeh/remote-dev-tracker.git
   cd remote-dev-tracker
   ```

2. Set up environment:
   ```bash
   cp .env.example .env
   ```

3. Run with Docker:
   ```bash
   docker-compose up --build
   ```

4. Or run manually:
   ```bash
   make install
   make run
   ```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | JWT signing secret |
| `CORS_ORIGINS` | Allowed CORS origins |
| `TIMEZONE` | Application timezone |
