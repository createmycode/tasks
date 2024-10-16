class Person:                                       # person클래스 생성
    def __init__(self, name, gender, age):          # 속성 초기화          
        self.name = name                            # 속성 생성
        self.gender = gender
        self.age = age

    def display(self):                               # 메서드 정의
        print (f"이름: {self.name}, 성별: {self.gender}")
        print (f"나이: {self.age}")
        while self.gender not in ['male','female']:                           # 성별이 male female이 아닐경우의 반복문
            print("잘못된 성별을 입력하셨습니다. 'male' 또는 'female'을 입력하세요.")
            a = (input('성별:'))                                               # 입력문을 받아 올바른 입력이 나오지않으면 무한 반복
            if a in ['male','female']:                                        # 입력문이 male female이면 반복문을 끝낸다는 조건문
                break

    def greet(self):                # 매서드 정의
        if self.age < 20:                                          # 20세를 기준으로 미성년자와 성인을 나누는 조건문
            print(f'안녕하세요, {self.name}님! 미성년자시군요!!')
        else:
            print(f'안녕하세요, {self.name}님! 성인이시군요!!')
        
                

person1 = Person('페이커','male',28)                #객체 생성
person1.display()                       # 각 매서드들을 호출한다
person1.greet()