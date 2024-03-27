import subprocess

def main():
    # Ejecutar create_secrets.py
    print("Creando secretos para k8s...")
    subprocess.run(["python", "create_secrets.py"])
    
    # Ejecutar load_data.py
    print("Cargando datos para el microservicio...")
    subprocess.run(["python", "load_data.py"])
    print(f'End point en ->  api/business/enid-service/imagenes-referencia/')

if __name__ == "__main__":
    main()
