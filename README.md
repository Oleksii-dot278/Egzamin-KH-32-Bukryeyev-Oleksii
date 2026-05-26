# Екзамен з ООП, Букрєєв Олексій
# Варіант 4

## Опис проекту:

## Проект реалізує систему обліку успішності студентів з використанням AI-агента
## У коді (`agent.py`) продемонстровано всі 4 парадигми ООП:

### 1. Абстракція (абстрактний клас `Person`)
### 2. Інкапсуляція (приватний список `__grades` у класі `Student`)
### 3. Наслідування (`Student` та `Teacher` успадковують `Person`)
### 4. Поліморфізм (перевизначений метод `get_role()`)

## Агент використовує інструмент (tool) `calculate_grade` для розрахунку середнього бала, рейтингу та надання порад студентам

## 1. Активація середовища: `pipenv shell`
## 2. Запуск агента: `adk run`

## Ось результати з діалогів:

![alt text](https://github.com/Oleksii-dot278/Egzamin_KH_32_Bukryeyev_Oleksii/blob/main/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-05-26%20221552.png)

![alt-text](https://github.com/Oleksii-dot278/Egzamin_KH_32_Bukryeyev_Oleksii/blob/main/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-05-26%20221605.png)

![alt-text](https://github.com/Oleksii-dot278/Egzamin_KH_32_Bukryeyev_Oleksii/blob/main/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-05-26%20221634.png)