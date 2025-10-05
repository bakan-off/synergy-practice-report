CREATE TABLE Tours (
    tour_id INT PRIMARY KEY IDENTITY(1,1),
    tour_name NVARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    duration_days INT
);

INSERT INTO Tours (tour_name, description, price, duration_days) VALUES 
('Все включено в Анталье', 'Отличный семейный отдых на побережье Средиземного моря.', 150000.00, 7),
('Дайвинг в Хургаде', 'Погрузитесь в удивительный подводный мир Красного моря.', 120000.00, 10),
('Отдых в Паттайе', 'Яркая ночная жизнь и экзотические пляжи Таиланда.', 180000.00, 14),
('Экскурсионный тур по Стамбулу', 'Посетите главные достопримечательности древнего города.', 95000.00, 5);