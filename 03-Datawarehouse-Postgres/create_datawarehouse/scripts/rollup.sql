SELECT
    d.year,
    c.country,
    sum(f.amount) as TotalSales
FROM
    "FactSales" f
JOIN
    "DimDate" d ON f.dateid = d.dateid
JOIN
    "DimCountry" c ON f.countryid = c.countryid
GROUP BY
    ROLLUP (d.year, c.country)
ORDER BY
    d.year, c.country