import random

elements_dict = {
    "H": ["수소", "Hydrogen"],
    "Li": ["리튬", "Lithium"], "Be": ["베릴륨", "Beryllium"],
    "B": ["붕소", "Boron"], "C": ["탄소", "Carbon"],
    "N": ["질소", "Nitrogen"], "O": ["산소", "Oxygen"],
    "F": ["플루오린", "Fluorine"],
    "Na": ["소듐", "Sodium"], "Mg": ["마그네슘", "Magnesium"],
    "Al": ["알루미늄", "Aluminum"], "Si": ["규소", "Silicon"],
    "P": ["인", "Phosphorus"], "S": ["황", "Sulfur"],
    "Cl": ["염소", "Chlorine"],
    "K": ["포타슘", "Potassium"], "Ca": ["칼슘", "Calcium"],
    "Sc": ["스칸듐", "Scandium"], "Ti": ["티타늄", "Titanium"],
    "V": ["바나듐", "Vanadium"], "Cr": ["크로뮴", "Chromium"],
    "Mn": ["망가니즈", "Manganese"], "Fe": ["철", "Iron"],
    "Co": ["코발트", "Cobalt"], "Ni": ["니켈", "Nickel"],
    "Cu": ["구리", "Copper"], "Zn": ["아연", "Zinc"],
    "Ga": ["갈륨", "Gallium"], 
    "As": ["비소", "Arsenic"], "Se": ["셀레늄", "Selenium"],
    "Br": ["브로민", "Bromine"], "Rb": ["루비듐", "Rubidium"],
    "Sr": ["스트론튬", "Strontium"], "Ag": ["은", "Silver"],
    "Cd": ["카드뮴", "Cadmium"], "Sn": ["주석", "Tin"],
    "Sb": ["안티모니", "Antimony"], "Te": ["텔루륨", "Tellurium"],
    "I": ["아이오딘", "Iodine"], "Cs": ["세슘", "Cesium"],
    "Ba": ["바륨", "Barium"]
}

def run_quiz():
    print("명명법 테스트 v3")
    mode = input("모드를 선택하세요 (1: 한글명, 2: 영어명): ")
    
    idx = 0 if mode == '1' else 1
    lang_name = "한글" if idx == 0 else "영어"

    quiz_list = list(elements_dict.keys())
    random.shuffle(quiz_list)
    
    wrong_answers = []
    
    print(f"\n{lang_name} 명칭을 입력하세요. (종료하려면 'exit' 입력)")
    print("-" * 30)

    for symbol in quiz_list:
        answer = input(f"원소 기호 [{symbol}]의 {lang_name} 이름은? ").strip()
        
        if answer.lower() == 'exit':
            return

        if answer.lower() == elements_dict[symbol][idx].lower():
            print("정답입니다!")
        else:
            print(f"틀렸습니다. 정답은 [{elements_dict[symbol][idx]}]입니다.")
            wrong_answers.append(symbol)

    while wrong_answers:
        print("\n" + "="*30)
        print(f"틀린 문제 {len(wrong_answers)}개를 다시 풉니다.")
        print("="*30)
        
        retry_list = wrong_answers[:]
        wrong_answers = [] 
        
        for symbol in retry_list:
            answer = input(f"원소 기호 [{symbol}]의 {lang_name} 이름은? ").strip()
            if answer.lower() == elements_dict[symbol][idx].lower():
                print("정답입니다!")
            else:
                print(f"다시 틀렸습니다. 정답은 [{elements_dict[symbol][idx]}]입니다.")
                wrong_answers.append(symbol)
                
    print("\n모든 문제를 맞혔습니다! 수고하셨습니다.")

if __name__ == "__main__":
    run_quiz()
