# order, name, phone, major
# 열제목 field name 필드명 필드
# 개수 4개
students = [
    {"order":1, "name":"a","phone":"1", "major":"경제학" },
    {"order":2, "name":"b","phone":"2", "major":"심리학" },
    {"order":3, "name":"c","phone":"3", "major":"컴공" },
    {"order":4, "name":"d","phone":"4", "major":"법학" }
]

# list는 for문을 쓸 수 있다. for each, 이터레이터 iterator
for student in students:
    # order에 1000을 곱해서 출력을 해보세요.
    print(student['name'], student['order'] * 1000)


