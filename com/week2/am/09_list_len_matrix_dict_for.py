# for, if, elif, print, type
# constants, variable, parameter
# function
# name	age	rating
# 해리	23	10
# 론	25	7
# 헤르미온느	24	6
employees = [
    {"name":"해리", "age":23, "rating":10},
    {"name":"론", "age":25, "rating":7},
    {"name":"헤르미온느", "age":24, "rating":6},
]
# 함수 parameter를 age, rating을 받아서
# salary = age *1000 + rating * 100
# getSalary라는 이름으로
# employees에 있는 모든 사원의 salary를 구해보세요.
def getSalary(age, rating):
    salary = age * 1000 + rating * 100
    return salary

for employee in employees:
    salary = getSalary(employee['age'], employee['rating'])
    print(employee['name'], salary)