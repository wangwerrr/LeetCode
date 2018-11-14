
SELECT Email FROM
(
  SELECT Email, count(Email) AS cnt
  FROM Person
  GROUP BY Email
) AS Statisitcs
WHERE cnt > 1;


SELECT Email 
FROM Person
GROUP BY EMAIL
HAVING count(EMAIL) > 1;
