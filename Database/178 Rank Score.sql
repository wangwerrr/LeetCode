SELECT 
    Score, 
    (SELECT count(distinct Score) FROM Scores s1 WHERE s1.Score >= s2.Score) Rank 
FROM Scores s2
ORDER BY Rank




SELECT
  Score,
  @rank := @rank + (@prev <> (@prev := Score)) Rank
FROM
  Scores,
  (SELECT @rank := 0, @prev := -1) init
ORDER BY Score desc
