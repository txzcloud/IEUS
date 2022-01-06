--1
SELECT firstname,lastname,cid 
FROM coaches_season 
GROUP BY firstname,lastname,cid HAVING COUNT(DISTINCT tid) < 2;

--2
SELECT PR.firstname 
FROM teams T, player_rs PR 
WHERE T.tid = PR.tid AND T.location = 'Miami N league' 
UNION SELECT PR2.firstname FROM teams T2, player_rs PR2 WHERE T2.tid = PR2.tid AND T2.location = 'New York A league';

--3
SELECT C.firstname, C.lastname, T.location, C.year 
FROM coaches_season C, player_rs P, teams T 
WHERE C.cid = P.ilkid AND C.tid = P.tid AND T.tid = P.tid AND C.year = P.year;

--4
SELECT T.name, AVG(P.h_feet*30.48 + P.h_inches*2.54), PR.year 
FROM teams T, players P, player_rs PR 
WHERE P.ilkid = PR.ilkid AND PR.tid = T.tid AND PR.year = 2002 GROUP BY T.tid, T.name, PR.year 
ORDER BY AVG(P.h_feet*30.48 + P.h_inches*2.54)DESC;

--5
SELECT C.firstname, C.lastname, C.cid
FROM coaches_season C, player_rs PR 
WHERE C.year = 2000 AND PR.year = 2000 AND C.tid = PR.tid 
GROUP BY C.cid, C.firstname, C.lastname 
ORDER BY COUNT(PR.ilkid)DESC LIMIT 1;

--6
SELECT C.firstname, C.lastname, C.cid
FROM coaches_season C, teams T
WHERE C.tid = T.tid 
GROUP BY C.cid, C.firstname, C.lastname HAVING COUNT(DISTINCT T.league) IN (SELECT COUNT(DISTINCT T1.league) FROM teams T1);

--7
SELECT C.firstname, C.lastname, C.year, T.name, T1.name
FROM coaches_season C, player_rs PR, teams T, teams T1
WHERE C.cid = PR.ilkid  
AND T.tid = C.tid AND T1.tid = PR.tid AND T.tid != T1.tid AND C.year = PR.year ORDER BY C.year ASC;

--8
SELECT A.firstname, A.lastname, A.year, (A.pts-B.pts) AS points_difference
FROM player_rs A, player_rs B
WHERE A.year = B.year AND B.firstname = 'Michael' AND B.lastname = 'Jordan' AND A.pts > B.pts;

--9
SELECT A.firstname, A.lastname, (SUM(A.season_win)*1.0)/(SUM(A.season_win)+SUM(A.season_loss)) AS success
FROM coaches_season A
GROUP BY A.firstname, A.lastname ORDER BY success DESC LIMIT 1 OFFSET 2;

--10
SELECT draft_from, COUNT(ilkid) AS temp FROM draft WHERE league = 'N' or league = 'B' or league = 'A' GROUP BY draft_from ORDER BY temp DESC LIMIT 3;

