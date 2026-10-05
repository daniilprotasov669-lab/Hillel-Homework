CREATE TABLE books(
    id       INTEGER       PRIMARY KEY       AUTOINCREMENT,
    title    TEXT                                         ,
    author   TEXT                                         ,
    year     INTEGER                                      ,
    price    INTEGER                                      ,
);

INSERT INTO books(title, author, year, price)
VALUES(
    ('Кобзар', 'Тарас Шевченко', 1840, 250),
    ('Лісова пісня', 'Леся Українка', 1911, 180),
    ('Захар Беркут', 'Іван Франко', 1883, 220),
    ('Тигролови', 'Іван Багряний', 1944, 300);
)

UPDATE books
    SET price = 270
    WHERE id = 1;

DELETE FROM books 
WHERE id = 4;