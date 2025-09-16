docker compose down --volumes --remove-orphans
docker compose pull
docker compose --env-file .env up --build