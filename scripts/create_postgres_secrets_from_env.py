import os
import base64
from dotenv import load_dotenv

def load_environment_variables():
    """Carga las variables de entorno desde el archivo .env."""
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(dotenv_path)

def create_postgres_secret(secret_dir):
    """Crea el secreto de PostgreSQL en un archivo YAML."""
    try:
        postgres_user = os.getenv('POSTGRES_USER')
        postgres_password = os.getenv('POSTGRES_PASSWORD')
        postgres_host = os.getenv('POSTGRES_HOST')
        postgres_db = os.getenv('POSTGRES_DB')

        os.makedirs(secret_dir, exist_ok=True)

        with open(os.path.join(secret_dir, 'postgres-references-secrets.yaml'), 'w') as f:
            f.write(f'''apiVersion: v1
kind: Secret
metadata:
  name: postgres-references-secrets
type: Opaque
data:
  POSTGRES_USER: {base64.b64encode(postgres_user.encode('utf-8')).decode('utf-8')}
  POSTGRES_PASSWORD: {base64.b64encode(postgres_password.encode('utf-8')).decode('utf-8')}
  POSTGRES_HOST: {base64.b64encode(postgres_host.encode('utf-8')).decode('utf-8')}
  POSTGRES_DB: {base64.b64encode(postgres_db.encode('utf-8')).decode('utf-8')}
''')
        print('Secreto de PostgreSQL creado exitosamente.')
    except Exception as e:
        print(f'Error al crear el secreto de PostgreSQL: {str(e)}')

if __name__ == "__main__":
    load_environment_variables()  
    SECRET_DIR = os.path.join(os.path.dirname(__file__), '..', 'k8s')
    create_postgres_secret(SECRET_DIR)
