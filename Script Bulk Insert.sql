USE STREAMING
GO

Create table Cliente(
ClienteID int primary key,
Nombre varchar(50),
Apellido varchar(50),
Genero Char(1),
Email varchar(100)
);

SELECT * FROM Cliente

TRUNCATE TABLE Cliente;

BULK INSERT Cliente
FROM 'C:\SQL Server Integration Services\Bulk Insert\Clientes.csv'
WITH(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n'
)