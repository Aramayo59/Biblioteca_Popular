USE bibliodb;

CREATE TABLE libros (
    libro_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ISBN VARCHAR(40) NOT NULL,
    Título VARCHAR(40) NOT NULL,
    Categoría VARCHAR(40) NOT NULL,
    Subcategoría VARCHAR(40) NOT NULL,
    Autor VARCHAR(40) NOT NULL,
    Editorial VARCHAR(40) NOT NULL,
    Descripción VARCHAR(100) NOT NULL
);


SELECT ID FROM libros WHERE condición;

SHOW TABLES IN bibliodb;

INSERT INTO libros (ISBN, Título, Categoría, Subcategoría, Autor, Editorial, Descripción)
VALUES 
('978-987-3863-45-5', 'La Sombra de su secreto', 'Novela', 'Romantica', 'Cardoza Claudia', 'Vestalles', 'El amor surge entre dos personas con secretos'),
('978-84-16363-87-2', 'Sin límites', 'Novela', 'Novela Negra', 'Adler-Olsen Jussi', 'MAEVA', 'Oscuro asesinato no resuelto'),
('978-987-8474-16-8', 'Robada', 'Novela', 'Thriller Psicológico', 'Stimson Tess', 'MOTUS', 'Atrapante libro ¿Quien se llevó a Lottie?');

delete from libros 
where libro_id = 1;

alter table libros
modify Descripción varchar(100);

update libros set ISBN = '978-987-3863-45-5', Título = 'La Smbra de su secreto', Categoría = 'Novela',
Subcategoría = 'Muy Romantíca', Autor = 'Cardozo Claudia', Editorial = 'Vestalles',
Descripción = 'El amor surge entre dos personas con secretos'
where libro_id= 2;

select * from libros;

describe libros;



select * from socios;

update socios set apellido = 'carrasco', nombre = 'pedro', domicilio = 'aconcagua 200',
fechadepago = '13 noviembre', teléfono = '0000000', sexo = 'femenino' where id= 3;
select * from socios;
update socios set socios.apellido = 'pedraza', socios.nombre = 'pedro', socios.domicilio = 'aconcagua 200',
socios.fechadepago = '13 noviembre', socios.teléfono = '0000000', socios.sexo = 'femenino' where socios.id= 1;

select * from socios;

show columns from libros




-- Consultar las tablas
SELECT * FROM prestamos;
SELECT * FROM libros;
SELECT * FROM socios;
SELECT * FROM editorial;
SELECT * FROM autor;
SELECT * FROM categoria;
SELECT * FROM subcategoria;
