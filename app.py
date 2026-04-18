import streamlit as st
import json
import os
import random

# --- [기타 설정] ---
DB_FILE = 'database.json'

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"users": {"admin": "1234"}, "posts": []}

def save_db(data):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

db = load_db()

if 'user' not in st.session_state:
    st.session_state.user = None

# --- [메인 화면에 로그인/회원가입 표시] ---
if st.session_state.user is None:
    st.title("🔐 접속이 필요합니다")
    
    # 탭으로 로그인과 회원가입 구분
    tab1, tab2 = st.tabs(["로그인", "회원가입"])
    
    with tab1:
        u_id = st.text_input("아이디", key="login_id")
        u_pw = st.text_input("비밀번호", type="password", key="login_pw")
        if st.button("로그인"):
            if u_id in db["users"] and db["users"][u_id] == u_pw:
                st.session_state.user = u_id
                st.rerun()
            else:
                st.error("정보가 틀렸습니다.")
                
    with tab2:
        new_id = st.text_input("아이디 만들기", key="reg_id")
        new_pw = st.text_input("비밀번호 만들기", type="password", key="reg_pw")
        if st.button("회원가입 완료"):
            if new_id in db["users"]:
                st.error("이미 있는 아이디입니다.")
            elif new_id and new_pw:
                db["users"][new_id] = new_pw
                save_db(db)
                st.success("가입 성공! 로그인 탭에서 로그인하세요.")
    st.stop() # 로그인 안 하면 아래 코드는 실행 안 됨

# --- [로그인 후 화면] ---
st.title(f"👋 {st.session_state.user}님, 환영합니다!")
if st.button("로그아웃"):
    st.session_state.user = None
    st.rerun()

# 마스터 기능
if st.session_state.user == "admin":
    st.divider()
    st.subheader("🛠️ 마스터 관리 도구")
    title = st.text_input("제목")
    content = st.text_area("내용")
    if st.button("업로드"):
        db["posts"].append({"title": title, "content": content})
        save_db(db)
        st.success("업로드 완료!")

# 게시물 보기
st.subheader("📚 올라온 자료")
for p in reversed(db["posts"]):
    with st.container(border=True):
        st.write(f"**{p['title']}**")
        st.write(p['content'])

# --- [메뉴 설정] ---
menu = st.sidebar.radio("활동 선택", ["📢 게시판", "🧪 화학 명명법", "🔭 망원경 구조", "🔭 망원경 운용 퀴즈", "🔢 지학 계산기"])

# 1. 게시판 (기존 코드 유지)
if menu == "📢 게시판":
    st.subheader("📚 올라온 자료")
    for p in reversed(db["posts"]):
        with st.container(border=True):
            st.write(f"**{p['title']}**")
            st.write(p['content'])

# 2. 화학 명명법 (화학 명명법.py + 복잡.py 통합)
elif menu == "🧪 화학 명명법":
    st.header("🧪 화학 명명법 테스트")
    
    # 두 파일의 데이터를 하나로 합침
    all_chem = {
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
    "Ba": ["바륨", "Barium"],
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
    
    mode = st.radio("정답 언어 선택", ["한글명", "영어명"], horizontal=True)
    idx = 0 if mode == "한글명" else 1
    
    # 세션 상태를 이용해 문제를 고정 (안 하면 입력할 때마다 문제가 바뀜)
    if 'chem_q' not in st.session_state:
        st.session_state.chem_q = random.choice(list(all_chem.keys()))
    
    q_formula = st.session_state.chem_q
    st.subheader(f"문제: [{q_formula}]")
    
    user_ans = st.text_input("이름을 입력하세요 (엔터키를 눌러 제출)")
    
    col1, col2 = st.columns(2)
    if col1.button("정답 확인"):
        correct = all_chem[q_formula][idx]
        if user_ans.replace(" ","").lower() == correct.replace(" ","").lower():
            st.success(f"정답입니다! : {correct}")
        else:
            st.error(f"오답입니다. 정답은: {correct}")
            
    if col2.button("다음 문제"):
        st.session_state.chem_q = random.choice(list(all_chem.keys()))
        st.rerun()

# 3. 망원경 구조 (망원경 구조.py)
elif menu == "🔭 망원경 구조":
    st.header("🔭 망원경 부품 명칭 퀴즈")
    
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
    cat = st.selectbox("영역 선택", ["가. 경통 (굴절 망원경)", "나. 가대 (적도의식)"])
    parts = telescope_data[cat]
    
    if 'tele_num' not in st.session_state:
        st.session_state.tele_num = random.choice(list(parts.keys()))
        
    q_num = st.session_state.tele_num
    st.info(f"질문: {cat} 파트의 **[{q_num}번]** 부품 이름은 무엇입니까?")
    
    ans_t = st.text_input("부품 이름 입력", key="tele_ans")
    
    if st.button("채점하기"):
        if ans_t.strip() == parts[q_num]:
            st.success("정답입니다! 🎉")
        else:
            st.error(f"틀렸습니다. 정답은 [{parts[q_num]}]입니다.")
            
    if st.button("다른 번호 풀기"):
        st.session_state.tele_num = random.choice(list(parts.keys()))
        st.rerun()

# 4. 망원경 운용 (망원경.py)
elif menu == "🔭 망원경 운용 퀴즈":
    st.header("🔭 망원경 설치 및 운용 4지선다")
    
    quiz_bank = {
        "설치법": [
            {"question": "삼각대 설치 시 방위지침봉의 'N' 자는 어느 방향을 향해야 하는가?", "options": ["동쪽", "서쪽", "남쪽", "북쪽"], "answer": 3, "explan": "북극성 방향인 북쪽을 향해야 적도식 가대가 정상 작동합니다."},
            {"question": "가대를 삼각대에 올린 후 가장 먼저 해야 할 일은?", "options": ["경통 끼우기", "아래쪽 고정 나사 돌려 고정", "무게추 달기", "전원 켜기"], "answer": 1, "explan": "가대가 추락하지 않도록 아래쪽 고정 나사를 조여 삼각대와 합체시켜야 합니다."},
            {"question": "설치 순서 중 가장 먼저 선행되어야 하는 것은?", "options": ["가대 조립", "경통 설치", "평평하고 단단한 바닥에 삼각대 설치", "무게추 달기"], "answer": 2, "explan": "모든 설치의 기본은 평평하고 단단한 지면 확보입니다."},
            {"question": "무게추 설치 시 가장 주의해야 할 점은?", "options": ["색깔 맞추기", "안전 나사를 반드시 잠그기", "최대한 위로 올리기", "두 개를 동시에 끼우기"], "answer": 1, "explan": "무게추가 발등으로 떨어지는 사고를 막기 위해 안전 나사 체결은 필수입니다."},
            {"question": "액세서리 선반의 역할은?", "options": ["장식용", "삼각대 다리 지지 및 부품 거치", "망원경 수평 맞추기", "무게 중심 잡기"], "answer": 1, "explan": "다리의 벌어짐을 방지하여 지지력을 높이고 아이피스 등을 보관합니다."},
            {"question": "경통을 가대에 부착할 때 사용하는 부품은?", "options": ["무게추 봉", "경통 플레이트와 고정나사", "파인더", "천정 미러"], "answer": 1, "explan": "경통 하단의 플레이트를 가대의 홈에 맞춰 끼우고 나사로 고정합니다."},
            {"question": "설치 시 '역순으로 분리해야 함'이라고 명시된 단계는?", "options": ["삼각대 설치", "경통 및 가대 해체", "파인더 정렬", "초점 맞추기"], "answer": 1, "explan": "설치의 반대 순서로 안전하게 해체해야 장비 파손을 막을 수 있습니다."},
            {"question": "가대 설치 후 경통을 올리기 전 상태는?", "options": ["클램프를 꽉 잠근 상태", "무게추가 이미 달린 상태", "전원이 켜진 상태", "파인더가 조립된 상태"], "answer": 1, "explan": "안전을 위해 경통보다 무게추가 먼저 설치되어 있어야 합니다."},
            {"question": "삼각대 다리 길이를 조절하는 이유는?", "options": ["높게 보기 위해", "수평을 맞추기 위해", "배율을 높이기 위해", "가볍게 하기 위해"], "answer": 1, "explan": "지면이 고르지 않을 때 다리 길이로 수평을 잡습니다."},
            {"question": "경통 설치 시 '도브테일 홈'에 끼운 뒤 무엇을 확인해야 하는가?", "options": ["렌즈의 색깔", "고정 나사가 완전히 조여졌는지", "바람의 방향", "현재 시간"], "answer": 1, "explan": "경통이 미끄러져 떨어지지 않도록 고정 나사 체결 확인이 제일 중요합니다."},
        ],
        "균형 맞추기": [
            {"question": "적경축(1차) 균형을 잡을 때 수평으로 놓아야 하는 것은?", "options": ["경통", "무게추 봉", "삼각대 다리", "파인더"], "answer": 1, "explan": "무게추 봉을 지면과 수평으로 두고 무게추 위치를 조절합니다."},
            {"question": "적위축(2차) 균형을 잡을 때 이동시켜야 하는 것은?", "options": ["무게추", "경통 자체의 위치", "삼각대 위치", "접안렌즈 종류"], "answer": 1, "explan": "경통 플레이트를 앞뒤로 밀어 경통 자체의 무게 중심을 잡습니다."},
            {"question": "무게추 쪽이 무거워 아래로 처진다면 어떻게 해야 하는가?", "options": ["무게추를 가대 쪽으로 올린다", "무게추를 봉 끝으로 내린다", "경통을 뒤로 민다", "경통을 앞으로 민다"], "answer": 0, "explan": "무거운 쪽의 모멘트를 줄이기 위해 무게추를 회전축(가대) 쪽으로 가깝게 이동시킵니다."},
            {"question": "대물렌즈 쪽이 무거워 앞으로 쏠릴 때 조치 방법은?", "options": ["무게추를 내린다", "경통을 뒤(접안부 쪽)로 민다", "경통을 앞으로 민다", "클램프를 더 꽉 잠근다"], "answer": 1, "explan": "경통 전체를 뒤로 이동시켜 중심을 맞춥니다."},
            {"question": "균형을 맞출 때 클램프(잠금장치)의 상태는?", "options": ["꽉 잠근 상태", "풀어서 자유롭게 움직이는 상태", "반만 잠근 상태", "제거한 상태"], "answer": 1, "explan": "어느 쪽으로 기우는지 확인해야 하므로 클램프를 풀어야 합니다."},
            {"question": "균형 잡기 전 반드시 장착 완료해야 하는 것은?", "options": ["전원 케이블", "관측에 사용할 모든 액세서리(아이피스 등)", "망원경 덮개", "노트북"], "answer": 1, "explan": "실제 관측 무게와 동일한 상태에서 균형을 잡아야 정확합니다."},
            {"question": "적경축 균형이 완벽하다는 것은 어떤 상태인가?", "options": ["무게추가 바닥에 닿은 상태", "손을 놓아도 수평을 유지하는 상태", "클램프가 부러진 상태", "무게추를 뺀 상태"], "answer": 1, "explan": "어느 쪽으로도 기울지 않고 정지해 있어야 균형이 맞는 것입니다."},
            {"question": "적위축 균형을 잡기 위해 경통을 움직일 때 주의할 점은?", "options": ["경통을 손으로 꼭 잡고 이동", "최대한 빠르게 이동", "렌즈를 만지며 이동", "무게추를 빼고 이동"], "answer": 0, "explan": "클램프를 푼 상태에서 경통이 갑자기 돌아가 부딪힐 수 있으므로 꼭 붙잡아야 합니다."},
            {"question": "균형 확인 시 '적경'과 '적위' 중 무엇을 먼저 하는 것이 일반적인가?", "options": ["적경(1차)", "적위(2차)", "상관없음", "동시에 수행"], "answer": 0, "explan": "보통 무게추 봉을 이용한 적경축 균형을 먼저 잡습니다."},
            {"question": "균형이 잘 맞으면 클램프를 살짝만 조여도 망원경이 고정되는가?", "options": ["네", "아니오", "알 수 없음", "무게추에 따라 다름"], "answer": 0, "explan": "균형이 맞으면 작은 힘으로도 장비를 안정적으로 고정하고 움직일 수 있습니다."},
        ],
        "파인더 정렬": [
            {"question": "파인더 정렬의 가장 큰 목적은?", "options": ["배율 확대", "주망원경과 파인더의 시야 일치", "망원경 청소", "사진 촬영"], "answer": 1, "explan": "파인더 십자선 중앙에 있는 물체가 주망원경 중앙에도 보이게 하기 위함입니다."},
            {"question": "파인더 정렬 시 추천하는 목표물은?", "options": ["빨리 지나가는 비행기", "멀리 있는 고정된 지상물(안테나 등)", "떠다니는 구름", "근처의 나무 잎사귀"], "answer": 1, "explan": "움직이지 않는 먼 목표물(500m 이상)이 정렬에 적합합니다."},
            {"question": "파인더 정렬 시 주망원경의 아이피스는 어떤 것이 좋은가?", "options": ["고배율", "저배율(시야가 넓은 것)", "아이피스 없음", "카메라 연결"], "answer": 1, "explan": "대상을 찾기 쉬운 저배율 아이피스로 먼저 중앙을 잡습니다."},
            {"question": "파인더 경통 주변에 있는 3개의 작은 나사의 용도는?", "options": ["파인더 분해용", "파인더 정렬(방향 조절)용", "초점 조절용", "디자인"], "answer": 1, "explan": "나사들을 조금씩 조이고 풀면서 파인더의 조준 방향을 미세하게 바꿉니다."},
            {"question": "정렬 순서로 옳은 것은?", "options": ["파인더 먼저 보고 주망원경 맞추기", "주망원경으로 중앙 잡고 파인더 맞추기", "동시에 보기", "렌즈 닦기 먼저 하기"], "answer": 1, "explan": "기준이 되는 주망원경 시야 중앙에 물체를 먼저 두고 파인더를 그에 맞춥니다."},
            {"question": "파인더 정렬은 언제 하는 것이 가장 효율적인가?", "options": ["한밤중", "밝은 낮 또는 해질녘", "비오는 날", "상관없음"], "answer": 1, "explan": "밝을 때 지상 물체를 보고 미리 정렬해두어야 밤에 별을 찾기 쉽습니다."},
            {"question": "파인더 내부의 십자선 모양은 보통 어떤 형태인가?", "options": ["원형", "십자(+) 모양", "삼각형", "없음"], "answer": 1, "explan": "정확한 중심을 가리키기 위해 십자선이 그려져 있습니다."},
            {"question": "파인더의 상이 흐리다면 어디를 돌려야 하는가?", "options": ["가대 나사", "파인더의 접안부 쪽(초점 조절부)", "주망원경 포커서", "무게추"], "answer": 1, "explan": "파인더 자체에도 별도의 초점 조절 기능이 있습니다."},
            {"question": "정렬이 끝난 후 최종 확인 방법은?", "options": ["눈을 감아본다", "두 망원경 중앙에 같은 물체가 있는지 확인", "망원경을 흔들어본다", "무게추를 옮겨본다"], "answer": 1, "explan": "주망원경과 파인더가 동일한 지점을 가리키는지 더블 체크합니다."},
            {"question": "파인더 정렬을 건너뛰면 발생하는 문제는?", "options": ["상이 어두워짐", "원하는 별을 찾기가 매우 힘들어짐", "배율이 낮아짐", "망원경이 쓰러짐"], "answer": 1, "explan": "시야가 좁은 주망원경만으로는 작은 별을 찾기가 거의 불가능합니다."},
        ],
        "초점 맞추기": [
            {"question": "초점을 맞출 때 돌리는 손잡이의 명칭은?", "options": ["클램프", "초점 조절 나사(Focus Knob)", "위도 나사", "방위 나사"], "answer": 1, "explan": "포커서 옆의 둥근 나사를 돌려 상을 뚜렷하게 만듭니다."},
            {"question": "초점이 맞지 않았을 때 별의 모습은?", "options": ["작고 날카로운 점", "크고 흐릿한 도넛이나 원형", "보이지 않음", "빨간색으로 보임"], "answer": 1, "explan": "초점이 맞지 않으면 빛이 퍼져서 흐릿한 원형으로 보입니다."},
            {"question": "초점 조절 시 가장 주의해야 할 사항은?", "options": ["최대한 빨리 돌리기", "천천히 돌리며 상의 변화 관찰", "힘껏 조이기", "아이피스 빼고 돌리기"], "answer": 1, "explan": "초점 구간을 지나치지 않도록 아주 천천히 조절해야 합니다."},
            {"question": "아이피스를 교체할 때마다 초점을 다시 잡아야 하는가?", "options": ["네", "아니오", "망원경마다 다름", "낮에만 해당"], "answer": 0, "explan": "렌즈마다 초점이 맺히는 위치가 다르므로 교체 시마다 미세 조정이 필요합니다."},
            {"question": "초점이 가장 잘 맞은 상태는?", "options": ["별이 가장 크게 보일 때", "별이 가장 작고 뚜렷한 점으로 보일 때", "상이 겹쳐 보일 때", "무지개색이 보일 때"], "answer": 1, "explan": "별이 가장 작은 점으로 응축되었을 때가 정초점 상태입니다."},
            {"question": "초점 나사를 돌려도 상이 계속 흐리다면 확인해야 할 것은?", "options": ["천정 미러 장착 여부", "관측자의 시력", "렌즈 캡 제거 여부", "전부 다"], "answer": 3, "explan": "기본적인 조립 상태와 캡 제거 여부를 먼저 확인해야 합니다."},
            {"question": "굴절 망원경에서 초점 조절은 무엇을 이동시키는가?", "options": ["대물렌즈", "접안부(아이피스)의 위치", "삼각대", "가대"], "answer": 1, "explan": "접안부의 길이를 변화시켜 상이 맺히는 위치를 맞춥니다."},
            {"question": "안경 쓴 사용자가 관측할 때 초점은 어떻게 맞추는가?", "options": ["안경 쓴 채로 그대로 둠", "자신의 시력에 맞게 초점 나사 재조절", "초점을 맞출 수 없음", "안경을 벗고 봐도 똑같음"], "answer": 1, "explan": "망원경 초점 나사가 시력 보정 역할을 하므로 본인 눈에 맞게 돌리면 됩니다."},
            {"question": "초점 조절 나사가 헛돈다면?", "options": ["나사가 부러진 것", "포커서 고정 나사가 잠겨 있는지 확인", "기름칠 하기", "망원경 교체"], "answer": 1, "explan": "포커서 하단에 이동 방지 고정 나사가 잠겨 있으면 조절 나사가 움직이지 않습니다."},
            {"question": "사진 촬영 시 초점 맞추기는 안구 관측보다?", "options": ["더 쉽다", "훨씬 정밀하고 어렵다", "똑같다", "할 필요 없다"], "answer": 1, "explan": "사진은 미세한 핀트 어긋남이 크게 나타나므로 훨씬 정밀해야 합니다."},
        ],
        "균형 맞추기가 필요한 이유": [
            {"question": "균형이 안 맞은 상태로 모터를 돌리면 생기는 문제는?", "options": ["배터리가 오래 감", "모터와 기어에 과부하 및 파손 위험", "별이 더 빨리 보임", "망원경이 가벼워짐"], "answer": 1, "explan": "한쪽으로 쏠린 무게를 억지로 돌리다 보면 정밀 기어에 무리가 갑니다."},
            {"question": "균형 잡기는 관측의 어떤 성능에 영향을 주는가?", "options": ["렌즈의 밝기", "정밀한 천체 추적(Tracking) 성능", "망원경의 배율", "관측지의 날씨"], "answer": 1, "explan": "무게 중심이 잘 맞아야 별을 따라가는 추적 장치가 부드럽게 작동합니다."},
            {"question": "클램프를 풀었을 때 경통이 휙 돌아가면 위험한 이유는?", "options": ["바람이 불어서", "사용자 부상 및 장비 충돌 파손", "별이 도망가서", "소음 발생"], "answer": 1, "explan": "무거운 경통이 삼각대 등에 부딪히면 렌즈나 가대가 크게 파손될 수 있습니다."},
            {"question": "균형이 잘 잡힌 망원경의 장점은?", "options": ["부드러운 조작감", "장비 수명 연장", "진동의 빠른 감쇠", "전부 다"], "answer": 3, "explan": "안전, 성능, 수명 모든 면에서 필수적입니다."},
            {"question": "장시간 사진 노출 촬영 시 균형이 중요한 이유는?", "options": ["필름 값을 아끼려고", "미세한 흔들림(가이드 오차) 방지", "배경을 검게 하려고", "카메라 배터리 절약"], "answer": 1, "explan": "균형이 안 맞으면 추적 속도가 미세하게 일정하지 않아 별이 흐르게 찍힙니다."},
            {"question": "균형을 맞추지 않아도 되는 망원경은?", "options": ["매우 비싼 망원경", "작은 장난감 망원경", "없음(모든 천체 망원경은 균형이 중요)", "낮에 보는 망원경"], "answer": 2, "explan": "어떤 망원경이든 정밀 관측 장비라면 무게 균형은 기본입니다."},
            {"question": "사용자의 안전과 가장 직결된 이유는?", "options": ["눈이 아플까 봐", "고정 나사 해제 시 급격한 회전 방지", "망원경이 무거워서", "추워서"], "answer": 1, "explan": "갑작스러운 회전으로 인한 손가락 끼임이나 장비 추락을 막아줍니다."},
            {"question": "매뉴얼에서 강조하는 균형의 핵심 키워드는?", "options": ["디자인", "안전과 정밀도", "속도", "색상"], "answer": 1, "explan": "장비 보호(안전)와 관측 품질(정밀도)이 핵심입니다."},
            {"question": "균형이 맞으면 모터 소음은?", "options": ["커진다", "조용하고 부드러워진다", "변화 없다", "끊겨서 들린다"], "answer": 1, "explan": "부하가 적어지므로 모터 구동음이 일정하고 조용해집니다."},
            {"question": "균형 잡기를 귀찮아서 건너뛰면?", "options": ["전문가처럼 보임", "장비 고장의 원인이 됨", "별이 더 잘 보임", "시간이 절약됨"], "answer": 1, "explan": "결국 기계적 결함으로 이어져 더 큰 비용과 시간을 낭비하게 됩니다."},
        ]
    }
    all_cats = list(quiz_bank.keys())
    sel_cat = st.selectbox("학습 주제 선택", all_cats)
    
    if f'quiz_idx_{sel_cat}' not in st.session_state:
        st.session_state[f'quiz_idx_{sel_cat}'] = random.randint(0, len(quiz_bank[sel_cat])-1)
    
    q_idx = st.session_state[f'quiz_idx_{sel_cat}']
    q_item = quiz_bank[sel_cat][q_idx]
    
    st.write(f"**Q. {q_item['question']}**")
    user_choice = st.radio("보기", q_item['options'])
    
    if st.button("결과 보기"):
        ans_idx = q_item['answer'] # 0, 1, 2, 3 형태
        if user_choice == q_item['options'][ans_idx]:
            st.success("정답입니다!")
        else:
            st.error(f"오답입니다. 정답은: {q_item['options'][ans_idx]}")
        st.info(f"해설: {q_item['explan']}")
    
    if st.button("다음 문제 넘어가기"):
        st.session_state[f'quiz_idx_{sel_cat}'] = random.randint(0, len(quiz_bank[sel_cat])-1)
        st.rerun()

# 5. 지학 계산기 (지학.py)
elif menu == "🔢 지학 계산기":
    st.header("🔢 지구과학 계산형 문제")
    st.write("문제를 풀고 답을 소수점 자리수에 맞춰 입력하세요.")
    
    # 세션에 문제 저장
    if 'geo_q' not in st.session_state:
        # 지학.py의 problems 리스트에서 랜덤 선택 및 수치 생성 로직 실행
        current_problem = random.choice(["집광력", "초점비", "배율", "분해능"])
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
        
        # 생성된 문제를 세션에 저장하는 이 줄이 빠져있었습니다.
        st.session_state.geo_q = (msg, correct_ans)
        
    # 세션에서 문제를 가져와 화면에 표시
    msg, correct_ans = st.session_state.geo_q
    st.warning(msg)
    user_val = st.number_input("정답 입력", value=0.0, step=0.01, key="geo_input") # 분해능 때문에 step을 0.01로 권장
    
    if st.button("정답 확인"):
        if abs(user_val - correct_ans) < 0.01: # 오차 범위 수정
            st.success("정답입니다! 계산 능력이 훌륭하시네요.")
        else:
            st.error(f"다시 계산해보세요. (정답: {correct_ans})")
            
    if st.button("새로운 문제 생성"):
        if 'geo_q' in st.session_state:
            del st.session_state.geo_q
        st.rerun() 
