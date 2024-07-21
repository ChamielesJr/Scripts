import gzip

input = open(":\Users\chami\Documents\2024-1\gestion de base de datos\Exportando datos con SQL Server\Exportando datos con Sql Server\Execute Process Task/Reporte Cliente.txt",'rb')
s=input.read()
input.close()

output = gzip.GzipFile("C:\Users\chami\Documents\2024-1\gestion de base de datos\Exportando datos con SQL Server\Exportando datos con Sql Server\Execute Process Task/Comprimido/Reporte Cliente.txt.gz",'wb')
output.write(s)
output.close()

print("Done")