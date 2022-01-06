
CREATE OR REPLACE FUNCTION Harmonic (n integer) RETURNS float AS $$
DECLARE  
  counter integer;
  incre float := 2;
  harmonicSum float8 := 1.0;
  maxInput integer := 1000000;
  outRange integer := -1;
BEGIN
  counter := 1; 
  IF n = 1 THEN
    RETURN harmonicSum;
  
  ELSEIF n <= maxInput AND n > 0 THEN
    LOOP
      harmonicSum := harmonicSum + 1/incre; 
      incre := incre + 1; -- increments counter by 1
      counter := counter + 1;
      IF counter = n THEN
        EXIT; --exit loop
      END IF;
    END LOOP;
    RETURN harmonicSum; 
    
  ELSE
    RETURN outRange;
    
  END IF;

RETURN harmonicSum;
END;
$$ LANGUAGE plpgsql;

------------------------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION player_height_rank (a integer, b integer) RETURNS INTEGER AS $$
DECLARE
  counter integer := 0;
  rank integer := 0;
  offs integer := 0;
  tempValue float := NULL;
  r record;

BEGIN

IF a > b OR a < 1 OR b < 1 THEN
  RETURN 0;
END IF;

FOR r IN SELECT (P.h_feet*12*2.54 + P.h_inches*2.54) AS height, P.firstname, P.lastname
    FROM players P
    ORDER BY height DESC
  
  LOOP 
    IF r.height = tempValue THEN
      offs := offs + 1; 
      
    ELSE 
      rank := rank + offs + 1;
      offs := 0;
      tempValue := r.height;
    
    END IF;
     
    IF rank >= $1 AND rank <= $2 THEN
      RAISE NOTICE '% % %', r.firstname, r.lastname, r.height;
      counter := counter + 1;
      --RETURN rank;
    END IF;
    
  END LOOP;

RETURN counter;

END;
$$ LANGUAGE plpgsql;



