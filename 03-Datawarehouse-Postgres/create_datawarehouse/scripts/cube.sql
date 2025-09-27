SELECT
    d.year,
    c.country,
    round(avg(f.amount)::numeric, 2) as Average_Sales
FROM "FactSales" f
INNER JOIN "DimCountry" c ON f.countryid = c.countryid
INNER JOIN "DimDate" d ON f.dateid = d.dateid
GROUP BY CUBE (d.year, c.country)
ORDER BY d.year, c.country