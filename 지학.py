import random

def telescope_quiz_game():
    print("="*50)
    print(" 지학 조현웅t 계산 문제 ")
    print("   (그만하고 싶다면 'q'를 입력하세요)   ")
    print("="*50)

    problems = [
        "집광력", 
        "초점비", 
        "배율", 
        "분해능"
    ]

    while True:
        current_problem = random.choice(problems)
        
        if current_problem == "집광력":
            aperture = random.randint(5, 30) * 10
            correct_ans = round((aperture / 7)**2, 1)
            msg = f"\n[문제] 구경이 {aperture}mm인 망원경의 집광력은? (소수점 첫째자리 반올림)"
            
        elif current_problem == "초점비":
            aperture = random.randint(5, 20) * 10
            f_ratio = random.randint(5, 12)
            f_length = aperture * f_ratio
            correct_ans = float(f_ratio)
            msg = f"\n[문제] 구경 {aperture}mm, 초점거리 {f_length}mm인 망원경의 초점비(F)는 얼마인가?"

        elif current_problem == "배율":
            obj_fl = random.randint(500, 1500)
            eye_fl = random.choice([10, 50])
            correct_ans = round(obj_fl / eye_fl, 1)
            msg = f"\n[문제] 주경 초점거리 {obj_fl}mm, 접안렌즈 초점거리 {eye_fl}mm일 때 배율은?"

        elif current_problem == "분해능":
            aperture = random.choice([1000, 1100, 1200, 1300, 1600, 3000, 2500, 2300, 1900, 2000])
            wavelength_nm = 550 
            res_val = (1.22 * (wavelength_nm * 1e-6) / aperture) * 206265
            correct_ans = round(res_val, 2)
            msg = f"\n[문제] 구경 {aperture}mm, 파장 {wavelength_nm}nm일 때 분해능은 몇 초(\")인가? (소수점 둘째자리까지 반올림)"
        
        while True:
            print(msg)
            user_input = input("답안 입력: ").lower()

            if user_input == 'q':
                print("\n게임을 종료합니다. 수고하셨습니다!")
                return

            try:
                user_ans = float(user_input)
                if abs(user_ans - correct_ans) < 0.1:
                    print("정답입니다! 다음 문제로 넘어갑니다.")
                    break
                else:
                    print("틀렸습니다. 다시 계산해 보세요!")
            except ValueError:
                print("숫자만 입력하거나 종료하려면 'q'를 입력하세요.")

if __name__ == "__main__":
    telescope_quiz_game()