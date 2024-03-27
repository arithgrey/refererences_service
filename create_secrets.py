import subprocess

def execute_script(script_name):
    """Ejecuta un script de Python."""
    try:
        subprocess.run(['python', script_name])
    except Exception as e:
        print(f'Error al ejecutar el script {script_name}: {str(e)}')

def main():
    
    postgres_script = 'scripts/create_postgres_secrets_from_env.py'
    django_script = 'scripts/create_django_secrets_from_env.py'
    
    execute_script(postgres_script)
    execute_script(django_script)

if __name__ == "__main__":
    main()
