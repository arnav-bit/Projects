select *
from dbo.retail_store


--create view for easy access of data --

create view product_cost as
SELECT CustomerID, ROUND(SUM(Quantity * UnitPrice), 2) AS Cost
FROM dbo.retail_store
WHERE Quantity >= 0 AND CustomerID IS NOT NULL
GROUP BY CustomerID;


--this proves there are no duplicates in the customerId column and all data is unique
select CustomerID, count(CustomerID) as Count from product_cost
group by CustomerID
having count(CustomerID) > 1;

--Q1: What is the distribution of order values across all customers in the dataset?--

select * from product_cost
order by Cost desc;

-- Q2 : How many unique products has each customer purchased?

select count(DISTINCT StockCode) countOfProducts, CustomerID from dbo.retail_store
where CustomerID is not null 
group by CustomerID
order by 1 desc
;

-- Q3: Which customers have only made a single purchase from the company?

select count(StockCode) countOfProducts, CustomerID from dbo.retail_store
where CustomerID is not null
group by CustomerID
having count(StockCode) = 1
order by 1 desc
;

-- Q4: Which products are most commonly purchased together by customers in the dataset?
SELECT a.StockCode AS Product1, b.StockCode AS Product2, COUNT(*) AS Frequency
FROM dbo.retail_store AS a
JOIN dbo.retail_store AS b ON a.InvoiceNo = b.InvoiceNo AND a.StockCode < b.StockCode
GROUP BY a.StockCode, b.StockCode
ORDER BY Frequency DESC;