def randomMember():
    import random
    members = ["서형원", "오동균", "탁정균", "한지웅", "이태경", "백승아"]

    # 랜덤으로 한 명을 선택
    selected_member = random.choice(members)

    # 밥 쏠 사람 출력
    print(f"오늘 밥 쏠 사람은 {selected_member} !!!, 잘 먹겠습니다!")

def menuRecommend():
    import random
    menu = ["짜장면", "제육", "돈까스(경양식)", "돈까스(일식)", "순대국", "설렁탕", "추어탕", "쌀국수", "피자", "생선구이백반", "라멘", "칼국수", "굶기"]

    # 랜덤으로 메뉴를 선택
    selected_menu = random.choice(menu)

    # 메뉴 출력
    print(f"{selected_menu} 드시러 가시죠")