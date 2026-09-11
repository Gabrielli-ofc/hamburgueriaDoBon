create database ingredientes;
use ingredientes;
create table hamburguer(
id INT PRIMARY KEY,
nome VARCHAR(50),
tipo VARCHAR(50),
valor DECIMAL(10,2)
);

insert into hamburguer (id, nome, tipo, valor) values
(1, 'pao brioche', 'pao', 12.00),
(2, 'pao francês', 'pao', 12.00), 
(3, 'carne bovina', 'carne', 9999.00),
(4, 'carne suína', 'carne', 45.00),
(5, 'carne vegana', 'carne', 38.00),
(6, 'alface americana', 'verdura', 7.00),
(7, 'Rúculla', 'veruda', 9.00),
(8, 'repolho roxo', 'legume', 10.00),
(9, 'cebola roxa', 'legume', 8.00),
(10, 'queijo prato', 'laticinio', 14.00),
(11, 'queijo gorgonzola', 'laticinio', 17.50),
(12, 'queijo mussarela', 'laticinio',  10.00),
(13, 'Catupiry', 'laticinio', 14.50),
(14, 'Bacon', 'carne', 15.00),
(15, 'barbecue', 'molho', 11.30),
(16, 'Hetchup', 'molho', 11.50),
(17, 'Mostarda', 'molho', 11.00),
(18, 'Maionese Tradicional', 'molho', 11.99),
(19, 'Maionese de Bacon defumada','molho', 12.00),
(20, 'maionese de azeitona preta', 'molho', 12.50),
(21, 'maionese de salsinha', 'molho', 11.00),
(22, 'Nuggets', 'acompanhamento', 12.00),
(23, 'batata frita', 'acompanhamento', 11.50),
(24, 'caixa de Nuggets', 'pack', 6.00),
(25, 'caixa de batat frita', 'pack', 6.00),
(26, 'farinha panko', 'farinha de rosca', 14.99),
(27, 'Coca-Cola tradicional 2l', 'bebida', 15.00),
(28, 'Coca-cola Zero Açucar 2l', 'bebida', 16.50),
(29, 'Coca-cola Tradicional 1,5l', 'bebida', 12.50),
(30, 'Coca-cola Zero Açúcar 1,5l', 'bebida', 13.99),
(31, 'coca-cola tradiciopnal 600ml', 'bebida', 8.50),
(32, 'coca-cola zero açúcar 600ml', 'bebida', 9.89),
(33, 'coca-cola tradciional lata 350ml', 'bebida', 5.00),
(34, 'coca-cola zero açúcar lata 350ml', 'bebida', 5.89);




















































































