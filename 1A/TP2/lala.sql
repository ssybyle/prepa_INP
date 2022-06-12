.read "hotel-schema.sql"
.read "hotel-insertion.sql"

.echo on
.mode box

.schema

SELECT nom, ville FROM hotel;

SELECT nom, ville FROM hotel WHERE etoiles>=4;

SELECT MIN(prixnuitht), MAX(prixnuitht), AVG(prixnuitht) FROM chambre;

SELECT MIN(prixnuitht), MAX(prixnuitht), AVG(prixnuitht) FROM chambre WHERE "type"="double";

SELECT COUNT(numchambre) FROM chambre WHERE prixnuitht<74.5;

SELECT DISTINCT nom FROM hotel NATURAL JOIN chambre WHERE "type"="suite";

SELECT DISTINCT nom FROM hotel WHERE nom NOT IN (SELECT DISTINCT nom FROM hotel NATURAL JOIN chambre WHERE "type"="simple");

SELECT DISTINCT nom, ville FROM hotel H WHERE (SELECT COUNT(*) FROM chambre C WHERE C.numhotel=H.numhotel AND "type"="double")>=5;

SELECT DISTINCT nom, ville FROM hotel NATURAL JOIN chambre WHERE "type"="simple"
INTERSECT
SELECT DISTINCT nom, ville FROM hotel NATURAL JOIN chambre WHERE "type"="double";

SELECT COUNT(nom) FROM hotel WHERE nom IN (SELECT DISTINCT nom FROM hotel NATURAL JOIN chambre WHERE nom="Hotel des ambassadeurs" AND "type"="triple");

SELECT DISTINCT (prixnuitht) FROM chambre WHERE prixnuitht IN (SELECT DISTINCT prixnuitht FROM hotel NATURAL JOIN chambre WHERE nom="Hotel terminus" AND ville="Grenoble" AND "type"="simple");

SELECT nom,ville FROM hotel WHERE numhotel IN (SELECT DISTINCT numhotel FROM reservation);

SELECT nom FROM client WHERE numclient IN (SELECT numclient FROM occupation WHERE datearrivee<DATE("2014-03-10") );

SELECT numhotel num, ville, nom, COUNT(numchambre) chambres FROM hotel NATURAL JOIN chambre GROUP BY nom ORDER BY ville;

///

SELECT nom from personne;

INSERT INTO personne (numero, nom, prenom) VALUES
    (12, "Bien", "Samira");

SELECT * FROM personne ORDER BY nom;

SELECT prenom FROM personne;

SELECT DISTINCT prenom FROM personne ORDER BY prenom;

SELECT COUNT(DISTINCT prenom) FROM personne;

SELECT * FROM personne WHERE numero < 4 AND prenom!="Paul";

SELECT prenom FROM personne WHERE prenom NOT IN ("Hella", "Paul", "Pierre");

SELECT T1.nom FROM personne T1 INNER JOIN personne T2 ON T1.nom=T2.prenom;

SELECT COUNT(*) FROM personne GROUP BY prenom;

SELECT prenom, COUNT(*) FROM personne GROUP BY prenom ORDER BY COUNT(prenom) DESC, prenom;

SELECT prenom, ct FROM  A WHERE ct>=2