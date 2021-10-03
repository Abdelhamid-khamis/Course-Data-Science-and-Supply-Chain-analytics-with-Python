/*      Revising the Select Query I     */
-- single line comment;

SELECT NAME
FROM CITY
WHERE population > 120000 AND CountryCode = "USA";


-- Weather Observation Station 3

SELECT DISTINCT CITY 
FROM STATION 
WHERE (ID % 2) = 0;
