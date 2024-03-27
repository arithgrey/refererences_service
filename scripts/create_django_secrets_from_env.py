import os
import subprocess
from dotenv import load_dotenv
import base64

def load_environment_variables():
    """Carga las variables de entorno desde el archivo .env."""
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(dotenv_path)

def create_secret(secret_name, data, output_file):
    """Crea un secreto en Kubernetes y escribe la definición en un archivo YAML."""
    try:
        # Crear el secreto en Kubernetes
        subprocess.run([
            'kubectl', 'create', 'secret', 'generic', secret_name,
            *[f'--from-literal={key}={value}' for key, value in data.items()]
        ])

        # Escribir la definición del secreto en un archivo YAML
        with open(output_file, 'w') as f:
            f.write(f'''apiVersion: v1
kind: Secret
metadata:
  name: {secret_name}
type: Opaque
data:
''')
            for key, value in data.items():
                # Codificar el valor en Base64 antes de escribirlo en el archivo
                encoded_value = base64.b64encode(value.encode()).decode('utf-8')
                f.write(f'  {key}: {encoded_value}\n')

        print(f'Secreto "{secret_name}" creado exitosamente en Kubernetes.')
        print(f'La definición del secreto se ha guardado en el archivo: {output_file}')
    except Exception as e:
        print('Error al crear el secreto en Kubernetes:', str(e))

def main():
    load_environment_variables()
    
    secret_name = 'django-allowed-hosts'
    env_variables = ['ALLOWED_HOSTS']
    
    env_data = {var: os.getenv(var) for var in env_variables}
    env_data = {var: value for var, value in env_data.items() if value is not None}

    if env_data:
        output_directory = os.path.join(os.path.dirname(__file__), '..', 'k8s')
        os.makedirs(output_directory, exist_ok=True)
        output_file = os.path.join(output_directory, f'{secret_name}-references-secret.yaml')
        create_secret(secret_name, env_data, output_file)
    else:
        print('No se encontraron variables de entorno válidas en el archivo .env.')

if __name__ == "__main__":
    main()
