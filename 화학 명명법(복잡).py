import random

compounds_data = {
    "NaBr": ["브로민화 소듐", "Sodium bromide"],
    "Rb2O": ["산화 루비듐", "Rubidium oxide"],
    "CaS": ["황화 칼슘", "Calcium sulfide"],
    "AlI3": ["아이오딘화 알루미늄", "Aluminum iodide"],
    "SrF2": ["플루오린화 스트론튬", "Strontium fluoride"],
    "Al2Se3": ["셀레늄화 알루미늄", "Aluminum selenide"],
    "K3N": ["질소화 포타슘", "Potassium nitride"],
    "Mg3P2": ["인화 마그네슘", "Magnesium phosphide"],
    "Hg2O": ["산화 수은(I)", "Mercury(I) oxide"],
    "FeBr3": ["브로민화 철(III)", "Iron(III) bromide"],
    "CoS": ["황화 코발트(II)", "Cobalt(II) sulfide"],
    "TiCl4": ["염화 티타늄(IV)", "Titanium(IV) chloride"],
    "Sn3N2": ["질소화 주석(II)", "Tin(II) nitride"],
    "CoI3": ["아이오딘화 코발트(III)", "Cobalt(III) iodide"],
    "HgO": ["산화 수은(II)", "Mercury(II) oxide"],
    "Cr2S3": ["황화 크로뮴(III)", "Chromium(III) sulfide"],
    "CsF": ["플루오린화 세슘", "Cesium fluoride"],
    "Li3N": ["질소화 리튬", "Lithium nitride"],
    "Ag2S": ["황화 은", "Silver sulfide"],
    "MnO2": ["산화 망가니즈(IV)", "Manganese(IV) oxide"],
    "TiO2": ["산화 티타늄(IV)", "Titanium(IV) oxide"],
    "Sr3P2": ["인화 스트론튬", "Strontium phosphide"], 
    "ZnCl2": ["염화 아연", "Zinc chloride"],
    "SnF4": ["플루오린화 주석(IV)", "Tin(IV) fluoride"],
    "Ca3N2": ["질소화 칼슘", "Calcium nitride"],
    "Al2S3": ["황화 알루미늄", "Aluminum sulfide"],
    "Hg2Se": ["셀레늄화 수은(I)", "Mercury(I) selenide"],
    "AgI": ["아이오딘화 은", "Silver iodide"],
    "BaSO3": ["아황산 바륨", "Barium sulfite"],
    "NaNO2": ["아질산 소듐", "Sodium nitrite"],
    "KMnO4": ["과망가니즈산 포타슘", "Potassium permanganate"],
    "K2Cr2O7": ["중크로뮴산 포타슘", "Potassium dichromate"],
    "Cr(OH)3": ["수산화 크로뮴(III)", "Chromium(III) hydroxide"],
    "Mg(CN)2": ["사이안화 마그네슘", "Magnesium cyanide"],
    "Pb(CO3)2": ["탄산 납(IV)", "Lead(IV) carbonate"],
    "NH4C2H3O2": ["아세트산 암모늄", "Ammonium acetate"],
    "SO2": ["이산화 황", "Sulfur dioxide"],
    "P2S5": ["오황화 이인", "Diphosphorus pentasulfide"],
    "As2O3": ["삼산화 이비소", "Diarsenic trioxide"],
    "AsF5": ["오플루오린화 비소", "Arsenic pentafluoride"],
    "N2O": ["일산화 이질소", "Dinitrogen monoxide"],
    "SF6": ["육플루오린화 황", "Sulfur hexafluoride"],
    "CuI": ["아이오딘화 구리(I)", "Copper(I) iodide"],
    "CuI2": ["아이오딘화 구리(II)", "Copper(II) iodide"],
    "S4N4": ["사질소 사황", "Tetrasulfur tetranitride"],
    "SeCl4": ["사염화 셀레늄", "Selenium tetrachloride"],
    "Na2CO3": ["탄산 소듐", "Sodium carbonate"],
    "NaHCO3": ["탄산수소 소듐", "Sodium hydrogen carbonate"],
    "NaOCl": ["차아염소산 소듐", "Sodium hypochlorite"],
    "BaCrO4": ["크로뮴산 바륨", "Barium chromate"],
    "NH4NO3": ["질산 암모늄", "Ammonium nitrate"],
    "H2SO4": ["황산", "Sulfuric acid"],
    "HClO": ["차아염소산", "Hypochlorous acid"],
    "HNO2": ["아질산", "Nitrous acid"],
    "H3PO4": ["인산", "Phosphoric acid"]
}

def run_quiz():
    print(" 화합물 명명법 테스트 ")
    mode = input("정답 언어를 선택하세요 (1: 한글명, 2: 영어명): ")
    
    idx = 0 if mode == '1' else 1
    lang_name = "한글" if idx == 0 else "영어"

    quiz_list = list(compounds_data.keys())
    random.shuffle(quiz_list)
    
    wrong_answers = []
    
    print(f"\n[{lang_name}] 명칭을 입력하세요. (종료: 'exit')")
    print("-" * 40)

    for formula in quiz_list:
        correct_name = compounds_data[formula][idx]
        answer = input(f"화학식 [{formula}]의 {lang_name} 이름은? ").strip()
        
        if answer.lower() == 'exit':
            return

        user_ans_check = answer.replace(" ", "").lower()
        correct_ans_check = correct_name.replace(" ", "").lower()

        if user_ans_check == correct_ans_check:
            print("정답입니다!")
        else:
            print(f"틀렸습니다. 정답은 [{correct_name}]입니다.")
            wrong_answers.append(formula)

    while wrong_answers:
        print("\n" + "="*30)
        print(f"오답 재도전: {len(wrong_answers)}문제")
        print("="*30)
        
        retry_list = wrong_answers[:]
        wrong_answers = [] 
        
        for formula in retry_list:
            correct_name = compounds_data[formula][idx]
            answer = input(f"화학식 [{formula}]의 {lang_name} 이름은? ").strip()
            
            user_ans_check = answer.replace(" ", "").lower()
            correct_ans_check = correct_name.replace(" ", "").lower()

            if user_ans_check == correct_ans_check:
                print("정답입니다!")
            else:
                print(f"다시 틀렸습니다. 정답은 [{correct_name}]입니다.")
                wrong_answers.append(formula)
                
    print("\n축하합니다! 모든 화합물 명칭을 맞혔습니다.")

if __name__ == "__main__":
    run_quiz()