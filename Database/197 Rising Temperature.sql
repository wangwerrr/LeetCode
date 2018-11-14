SELECT b.Id 
FROM Weather a JOIN Weather b
ON DATEDIFF(b.RecordDate, a.RecordDate) = 1 
AND b.Temperature > a.Temperature;
