CREATE MATERIALIZED VIEW total_sales_per_country
AS SELECT c.country, sum(f.amount) as Total_Sales
FROM "DimCountry" c, "FactSales" f
WHERE c.countryid = f.countryid
GROUP BY c.country