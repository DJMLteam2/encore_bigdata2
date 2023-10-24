import random
import itertools
import time

def coin_game(num):

    member = []
    for i in range(65, 65+int(num)):
        member.append(chr(i))

    s_member = list(itertools.permutations(member))
    f_member = random.choice(s_member)
    start = input(f"멤버는 :{member}입니다 게임이 진행될 방향을 정하세요! 정하셨다면 [Enter]")

    if not start:
        print(f"{f_member[0]}부터 게임을 시작합니다!")

        count = 0
        coin = ['■', '□']
        game = True

        while game:
            for mem in f_member:
                count+=1
                print('='*90)
                print(f"{mem}가 마셔야할 술 {count}잔, 싫다면 코인을 던지세요")
                answer = input("코인이 모두 뒷면(■,■)일 경우 당첨!! 코인을 던지시겠습니까?(Y/N) :")

                if answer == 'Y':
                    result = random.choice(coin),random.choice(coin)
                    print("1......")
                    time.sleep(0.7)
                    print("2............")
                    time.sleep(0.7)
                    print("3..................")
                    time.sleep(0.7)

                    print(f"코인 결과: {result} !!!!")
                    time.sleep(2)
                    
                    if result[0] == '■' and result[1] == '■':
                        print('='*90)
                        print("🌺팡팡💥파라바라~팡팡팡 🎊ヲヲヲヲヲヲヲヲヲヲヲ"*count)

                        print(f">>>>>>>>>>>>>  {mem} 당첨!! {count}잔을 마셔야합니다!")
                        
                        game = False
                        break
                    else:
                        continue
                
                else:
                    print('='*90)
                    print(f">>>>>>>>>>>>>포기하셨습니다!!! {mem}가 {count}잔을 마셔야합니다!")
                    game = False
                    break
