# %%
from pearl_maple_func import *

# %%
directory = './pearl_maple.csv'
members = load_member_list(directory)

while True:
    print("""
    ======================================
    플래그 횟수 계산기에 오신걸 환영합니다  
    참여한 길드원 입력: 1                  
    점수 초기화: 2
    길드원 추가: 3
    길드원 삭제: 4
    조건 맞춘 길드원 출력: 5
    전체 성적표 출력: 6
    작업 종료: (아무 키)
    =====================================""")

    a = input('다음 중 기능을 선택하세요 ')
    if a == "1":
        input_score(members)
    elif a == "2":
        reset_score(members)
    elif a == "3":
        new_member(members)
    elif a == "4":
        delete_member(members)
    elif a == "5":
        print_cut(members)
    elif a == "6":
        print_total(members)
    else:
        break

file_save(members)
