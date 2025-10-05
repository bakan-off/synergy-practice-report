from flask import Flask, render_template
import pyodbc

# Настройка приложения Flask
app = Flask(__name__)

# --- Конфигурация подключения к MS SQL Server ---
# Имя вашего сервера, которое мы выяснили
SERVER = 'DESKTOP-Q96S8PD'
# Имя базы данных, которую мы создали
DATABASE = 'TourismDB'

# Строка подключения для Windows Authentication
# Trusted_Connection=yes означает, что используется ваша учетная запись Windows
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'

def get_db_connection():
    """Функция для установления соединения с базой данных."""
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        print(f"Ошибка подключения к БД: {e}")
        return None

# Маршрут для главной страницы
@app.route('/')
def index():
    tours_list = []
    conn = get_db_connection()
    if conn:
        print("Соединение с БД установлено успешно!")
        cursor = conn.cursor()
        # Выбираем все поля из таблицы Tours
        cursor.execute("SELECT tour_id, tour_name, description, price, duration_days FROM Tours")
        # .fetchall() забирает все строки, которые вернул запрос
        tours_list = cursor.fetchall()
        conn.close()
        print("Соединение с БД закрыто.")
    else:
        print("Не удалось установить соединение с БД.")

    # Передаем список туров в HTML-шаблон для отображения
    return render_template('index.html', tours=tours_list)

# Эта часть позволяет запустить приложение напрямую из PyCharm
if __name__ == '__main__':
    app.run(debug=True)