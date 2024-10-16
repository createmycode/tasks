import random                              
number = random.randrange(1, 11)                                     # 랜덤숫자를 불러오는 코드
print('QUIZ 1~10사이의 숫자중에서 하나 골라보세요!') 

# 도전과제까지 전부 추가한 완성본 
while True:                                                          # 루프 구성
    select = int(input('무엇을 고르실건가요?'))                           # 범위안의 숫자를 입력하도록 하는 입력문
    
    if number > select:                                              # 랜덤 숫자가 입력숫자보다 클경우를 조건하는 조건문과 구문
        print('up')
    elif number < select:                                            # 랜덤 숫자가 입력숫자보다 작을 경우를 조건하는 조건문과 구문
        print('down')
    else:                                                            # 크거나 작지 않을 경우 즉, 같을 경우를 처리하는 조건문과 구문
        print('success')
        ask = input('게임을 다시 하시겠습니까? (y/n) :')                   # 정답을 맞췄을때 게임을 끝낼건지 다시할건지를 물어보는 입력문
        if ask in ['y','Y']:                                         # y 를 입력하면 게임이 계속 진행되고
            continue
        else:
            print('게임을 종료합니다. 언젠가 다시 만나요!')                   # n 을 입력하면 break를 통해 반복문을 종료한다.
            break









