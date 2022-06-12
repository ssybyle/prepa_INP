CREATE TABLE personne (
    numero INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL
);

INSERT INTO personne (numero, nom, prenom)
VALUES
    (0, "Egérie", "Tom"),
    (1, "Covaire", "Harry"),
    (2, "Stick", "Hella"),
    (3, "Hémique", "Paul"),
    (4, "Terrieur", "Alain"),
    (5, "Embett", "Akim"),
    (6, "Sion", "Eva"),
    (7, "Ochon", "Paul"),
    (8, "Tom", "Dereck"),
    (9, "Ution", "Paul"),
    (14, "Provist", "Alain"),
    (10, "Sion", "Sarah");

.mode box
.echo on

SELECT nom FROM personne;

INSERT INTO personne (numero, nom, prenom) VALUES
    (12, "Bien", "Samira");
