# %%
import csv


def load_member_list(directory='./pearl_maple.csv'):
    member_list = {}
    with open(directory, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            member_list[row['길드원명']] = int(row['점수'])
    return member_list


def input_score(member_list):
    while True:
        name = input("""플래그에 참여한 길드원 닉을 입력하세요.\n입력을 종료하려면 end를 입력하세요""")
        if name in member_list.keys():
            member_list[name] += 1
        elif name == 'end':
            return
        else:
            print('길드원 닉을 다시 입력하세요')


def reset_score(member_list):
    for key in member_list.keys():
        member_list[key] = 0


def new_member(member_list):
    new_member_name = input('새 길드원의 닉을 입력하세요 ')
    name_check = int(input('길드원 닉이 " ' + str(new_member_name) + ' " 이 맞나요? 맞으면 1, 아니면 2를 입력하세요'))
    if name_check == 1:
        member_list[new_member_name] = 0
    else:
        print('닉을 다시 입력해주세요')
        new_member(member_list)


def delete_member(member_list):
    delete_member_name = input('탈퇴한 길드원 닉을 입력하세요 ')
    if delete_member_name in member_list.keys():
        del member_list[delete_member_name]
    else:
        print('없는 길드원입니다 닉을 다시 입력하세요 ')
        delete_member(member_list)


def print_cut(member_list):
    for key in member_list.keys():
        if member_list[key] >= 3:
            print(key, str(member_list[key]))


def print_total(member_list):
    for key in member_list.keys():
        print(format(key, "<8"), ":", member_list[key])


def file_save(member_list, directory='./pearl_maple.csv'):
    previous_num_of_members = len(load_member_list(directory))  # 기존에 파일에 저장된 길드원 수
    with open(directory, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["길드원명", "점수"])
        for key in member_list.keys():  # 새로운 정보로 덮어씌우기
            writer.writerow([key, member_list[key]])
        for i in range(previous_num_of_members - len(member_list)):  # 기존 길드원 수가 많이 끝부분이 안 덮어졌으면 공백으로 덮는다.
            writer.writerow(["", ""])
    file.close()
    return

