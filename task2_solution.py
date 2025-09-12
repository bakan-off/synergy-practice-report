class Employee:
    """
    Базовый класс, представляющий сотрудника.
    """
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        """
        Выводит основную информацию о сотруднике.
        Этот метод будет унаследован производным классом.
        """
        print(f"Имя: {self.name}, Зарплата: {self.salary} руб.")

    def calculate_annual_bonus(self):
        """
        Рассчитывает стандартный годовой бонус (10% от зарплаты).
        Этот метод будет переопределен в производном классе.
        """
        return self.salary * 0.10


class Manager(Employee):
    """
    Производный класс, представляющий менеджера.
    Наследуется от класса Employee.
    """
    def __init__(self, name, salary, department):
        # Вызов конструктора базового класса для инициализации унаследованных полей
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        """
        Расширяет метод базового класса для вывода дополнительной информации.
        """
        print(f"Имя: {self.name}, Зарплата: {self.salary} руб., Отдел: {self.department}")

    def calculate_annual_bonus(self):
        """
        Переопределяет метод базового класса для расчета бонуса менеджера.
        Бонус менеджера = стандартный бонус + 15000 руб.
        """
        base_bonus = super().calculate_annual_bonus()
        return base_bonus + 15000

    def manage_team(self):
        """
        Уникальный метод только для класса Manager.
        """
        print(f"Менеджер {self.name} управляет командой отдела {self.department}.")


# --- Демонстрация работы ---

print("--- Информация об объектах ---")
# Создание объекта базового класса
employee = Employee("Иван Петров", 70000)
employee.display_info()

# Создание объекта производного класса
manager = Manager("Алексей Сидоров", 120000, "Разработки")
manager.display_info()

print("\n--- Демонстрация полиморфизма (переопределение метода) ---")
# Вызов метода calculate_annual_bonus для разных объектов
employee_bonus = employee.calculate_annual_bonus()
print(f"Годовой бонус сотрудника {employee.name}: {employee_bonus} руб.")

manager_bonus = manager.calculate_annual_bonus()
print(f"Годовой бонус менеджера {manager.name}: {manager_bonus} руб.")

print("\n--- Демонстрация уникального метода производного класса ---")
# Вызов метода, который есть только у менеджера
manager.manage_team()