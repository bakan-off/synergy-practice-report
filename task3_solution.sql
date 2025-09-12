-- Создание таблицы-справочника "Страны"
CREATE TABLE Countries (
    country_id INT PRIMARY KEY AUTO_INCREMENT,
    country_name VARCHAR(100) NOT NULL UNIQUE
);

-- Создание таблицы-справочника "Отели"
CREATE TABLE Hotels (
    hotel_id INT PRIMARY KEY AUTO_INCREMENT,
    hotel_name VARCHAR(150) NOT NULL,
    stars TINYINT,
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES Countries(country_id)
);

-- Создание таблицы-справочника "Туры"
CREATE TABLE Tours (
    tour_id INT PRIMARY KEY AUTO_INCREMENT,
    tour_name VARCHAR(200) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    duration_days INT,
    hotel_id INT,
    FOREIGN KEY (hotel_id) REFERENCES Hotels(hotel_id)
);

-- Создание таблицы переменной информации "Заказы"
CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    tour_id INT,
    client_name VARCHAR(200) NOT NULL,
    order_date DATE NOT NULL,
    status VARCHAR(50),
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (tour_id) REFERENCES Tours(tour_id)
);

-- Добавление нескольких записей для демонстрации
INSERT INTO Countries (country_name) VALUES ('Турция'), ('Египет'), ('Таиланд');

INSERT INTO Hotels (hotel_name, stars, country_id) VALUES 
('Rixos Sungate', 5, 1),
('Steigenberger Aqua Magic', 5, 2),
('Dusit Thani Pattaya', 4, 3);

INSERT INTO Tours (tour_name, price, duration_days, hotel_id) VALUES 
('Все включено в Анталье', 150000.00, 7, 1),
('Дайвинг в Хургаде', 120000.00, 10, 2),
('Отдых в Паттайе', 180000.00, 14, 3);

INSERT INTO Orders (tour_id, client_name, order_date, status, total_amount) VALUES
(1, 'Иванов Иван Иванович', '2025-08-10', 'Оплачен', 150000.00),
(3, 'Петрова Анна Сергеевна', '2025-08-15', 'Забронирован', 180000.00);