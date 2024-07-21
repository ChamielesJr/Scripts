import os
import gzip

input_file_path = r"C:\SQL Integration Services\Execute Process Task\Reporte Cliente.txt"
output_file_path = r"C:\SQL Integration Services\Execute Process Task\Comprimido\Reporte Cliente.txt.gz"

if os.path.exists(input_file_path):
    try:
        with open(input_file_path, 'rb') as input_file:
            with gzip.GzipFile(output_file_path, 'wb') as output_file:
                output_file.writelines(input_file)
        print("Done")
    except FileNotFoundError as e:
        print(f"Error: {e}")
else:
    print(f"Error: El archivo {input_file_path} no existe.")
