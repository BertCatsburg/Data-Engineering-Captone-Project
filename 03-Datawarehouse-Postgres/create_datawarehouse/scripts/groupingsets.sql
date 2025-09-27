SELECT
    co.country,
    ca.category,
    sum(f.amount) as TotalSales
FROM
    "FactSales" f
INNER JOIN
    "DimCategory" ca ON f.categoryid = ca.categoryid
INNER JOIN
    "DimCountry" co ON f.countryid = co.countryid
GROUP BY
    GROUPING SETS (
        (co.country, ca.category),
        co.country,
        ca.category,
        ()
    )
ORDER BY
    ca.category,
    co.country
