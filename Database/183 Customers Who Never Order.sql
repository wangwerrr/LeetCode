SELECT Name AS Customers 
FROM Customers LEFT JOIN Orders
ON Customers.Id = Orders.CustomerId
WHERE Orders.CustomerId is NULL;


SELECT Name AS Customers FROM Customers
WHERE Customers.Id NOT IN (SELECT CustomerId FROM Orders);
