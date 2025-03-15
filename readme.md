# Data Engineering Zoocamp

```bash
services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - postgres-db-volume:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "airflow"]
      interval: 5s
      retries: 5
    restart: always
```
```bash
docker run -it  \
  -e  POSTGRES_USER="root" \
  -e  POSTGRES_PASSWORD="root" \
  -e  POSTGRES_DB="ny_taxi" \
  -v <yourpath>\2_docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
 postgres:13
```
```bash
 docker run -it  \
  -e  POSTGRES_USER="root" \
  -e  POSTGRES_PASSWORD="root" \
  -e  POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
 posgres:13

 https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
```

```bash
docker-run -it `
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" `
  -e PGADMIN_DEFAULT_PASSWORD="root" `
  -p 8080:80 `
  dpage/pgadmin4
```
```bash
#powershell
docker run -it `
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" `
  -e PGADMIN_DEFAULT_PASSWORD="root" `
  -p 8080:80 `
  dpage/pgadmin4
```
```bash
#cmd
docker run -it -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" -e PGADMIN_DEFAULT_PASSWORD="root" -p 8080:80 dpage/pgadmin4
```
```bash
 docker run -it `
  -e POSTGRES_USER="root" `
  -e POSTGRES_PASSWORD="root" `
  -e POSTGRES_DB="ny_taxi" `
  -v "<yourpath>\2_docker_sql\ny_taxi_postgres_data:/var/lib/postgresql/data" `
  -p 5432:5432 `
  postgres:13
```
```bash
## network 
docker network create pg-network
```
```bash
 docker run -it `
  -e POSTGRES_USER="root" `
  -e POSTGRES_PASSWORD="root" `
  -e POSTGRES_DB="ny_taxi" `
  -v "<yourpath>\2_docker_sql\ny_taxi_postgres_data:/var/lib/postgresql/data" `
  -p 5432:5432 `
  --network=pg-network `
  --name pg-database `
  postgres:13
```
```bash
  docker run -it `
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" `
  -e PGADMIN_DEFAULT_PASSWORD="root" `
  -p 8080:80 `
  --network=pg-network `
  --name pgadmin-2 `
  dpage/pgadmin4
  ```