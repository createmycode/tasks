class Person:                                       # person클래스 생성
    def __init__(self, name, gender, age):          # 속성 초기화          
        self.name = name                            # 속성 생성
        self.gender = gender
        self.age = age

    def display(self):                               # 메서드 정의
        print (f"이름: {self.name}, 성별: {self.gender}")
        print (f"나이: {self.age}")

person1 = Person('페이커','male',28)                #객체 생성
person1.display()                          # 매서드를 호출한다