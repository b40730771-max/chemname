import random

def run_telescope_photo_quiz():
    telescope_data = {
        "가. 경통 (굴절 망원경)": {
            "1": "후드",
            "2": "렌즈셀",
            "3": "경통밴드",
            "4": "경통플레이트",
            "5": "파인더",
            "6": "파인더정렬나사",
            "7": "파인더브라켓",
            "8": "파인더고정나사",
            "9": "초점조절나사",
            "10": "초점고정나사",
            "11": "접안부고정나사",
            "12": "접안렌즈",
            "13": "직각프리즘"
        },
        "나. 가대 (적도의식)": {
            "1": "경통플레이트고정나사",
            "2": "적위축고정클램프",
            "3": "적위축수동클러치",
            "4": "적위미동나사",
            "5": "적경축수동클러치",
            "6": "무게추",
            "8": "적경축미동나사",
            "9": "고도조절나사",
            "11": "경통플레이트안전나사",
            "16": "무게추봉",
            "17": "무게추잠금나사",
            "18": "무게추안전나사"
        }
    }

    print("="*60)
    print("사진 속 망원경 구조 맞추기 퀴즈 (가 & 나)")
    print("="*60)
    print("사진을 준비하세요.(옆에 이름은 가리고 ^^)")
    print("문제가 지정하는 번호의 부품 이름을 한글로 정확히 입력하세요.")
    print("퀴즈를 종료하려면 '종료'를 입력하세요.\n")

    score = 0
    question_count = 0

    all_questions = []
    for category, parts in telescope_data.items():
        for number, answer in parts.items():
            all_questions.append((category, number, answer))
            

    random.shuffle(all_questions)

    for category, number, answer in all_questions:
        question_count += 1
        print(f"[{question_count}/{len(all_questions)}] ")
        print(f"이미지: {category}")
        print(f"문제: 사진 속 [{number}번] 부품의 이름은 무엇입니까?")
        
        user_answer = input("정답 입력 >> ").strip()

        if user_answer == "종료":
            question_count -= 1
            break

        if user_answer == answer:
            print("정답입니다!\n")
            score += 1
        else:
            print(f"틀렸습니다. 정답은 [{answer}]입니다.\n")

    print("\n" + "="*60)
    if question_count > 0:
        print(f"퀴즈 종료! 최종 점수: {score} / {question_count}")
        percentage = (score / question_count) * 100
        if percentage == 100:
            print("결과: A+")
        elif percentage >= 70:
            print("결과: A0")
        else:
            print("결과: A-")
    else:
        print("B")
    print("="*60)

if __name__ == "__main__":
    run_telescope_photo_quiz()