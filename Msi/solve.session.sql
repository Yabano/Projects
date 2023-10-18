--@block
SELECT nome, funcao, nomeObra, hora_do_dia FROM funcionarios INNER JOIN obras ON obras.ref = funcionarios.id

--@block
SELECT * FROM funcionarios

--@block
SELECT * FROM obras