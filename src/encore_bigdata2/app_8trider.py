def randomMember():
    import random
    members = ["서형원", "오동균", "탁정균", "한지웅", "이태경", "백승아"]

    # 랜덤으로 한 명을 선택
    selected_member = random.choice(members)

    # 밥 쏠 사람 출력
    print(f"오늘 밥 쏠 사람은 {selected_member} !!!, 잘 먹겠습니다!")