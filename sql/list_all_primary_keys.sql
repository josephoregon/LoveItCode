/* List all primary keys (PKs) and their columns in SQL Server database */

-- Source: https://dataedo.com/kb/query/sql-server/list-all-primary-keys-and-their-columns 


SELECT  schema_name(tab.schema_id) AS [schema_name]
       ,pk.[name]                  AS pk_name
       ,ic.index_column_id         AS column_id
       ,col.[name]                 AS column_name
       ,tab.[name]                 AS table_name
FROM sys.tables tab
INNER JOIN sys.indexes pk
ON tab.object_id = pk.object_id AND pk.is_primary_key = 1
INNER JOIN sys.index_columns ic
ON ic.object_id = pk.object_id AND ic.index_id = pk.index_id
INNER JOIN sys.columns col
ON pk.object_id = col.object_id AND col.column_id = ic.column_id
ORDER BY schema_name(tab.schema_id), pk.[name], ic.index_column_id

