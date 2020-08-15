-- count specific values by given date
SELECT
  DISTINCT RTRIM(UPPER(a.ID1 + ' ' + a.ID2)) AS ID1Nbr,
  RTRIM(UPPER(a.Group)) AS Lessee,
  RTRIM(UPPER(a.SubGroup)) AS Fleet,
  CONVERT(varchar(10), a.EndDate, 120) AS EndDate,
  COUNT(*) AS [Count]
FROM
  Table1 a
  INNER JOIN Table2 b ON a.ID1 = b.ID1
  AND a.ID2 = b.ID2
  LEFT JOIN Table3 sel ON b.column = sel.column
WHERE
  a.EndDate IS NOT NULL
  AND a.Group <> 'string'
GROUP BY
  a.ID1 + ' ' + a.ID2,
  a.Group,
  a.SubGroup,
  a.EndDate
ORDER BY
  EndDate
