
# Документация #
## Общее описание проекта ##
### Файл circle.py ###
Содержит реализацию нахождения площади круга, периметра окружности
```
def area(r: int) -> float
def perimeter(r: int) -> float
```

### Файл square.py ###
Содержит реализацию нахождения площади квадрата, периметра квадрата
```
def area(a: int) -> int
def perimeter(a: int) -> int
```

## Примеры использования ##
### Примеры использования circle.py
```
import circle

def sphere_volume(r: int) -> float:
    return 2 / 3 * circle.area(r) * circle.perimeter(r)

print(sphere_volume(3 / 2)) # (math.pi ** 2) * (r ** 3) * 2
```

### Пример использования square.py ###
```
import square

size = int(input())

area = square.area(size) # size ** 2
per  = square.perimeter(size) # 4 * size

print(area, per)
```
## История коммитов ##
Здесь вы найдете историю коммитов
```
7ee7c67 Delete information about branches in commit history (docs\docx.md)
c914b9a Add commits history block in docs/docx.md
d139556 Added code examples, open commit history log
69bd516 Added docx.md with information about square.py and circle.py
4b17085 Added documentation to cicrle.py and square.py
d078c8d L-03: Docs added
8ba9aeb L-03: Circle and square added
```
