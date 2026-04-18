import streamlit as st

st.set_page_config(page_title="과학 퀴즈 통합 플랫폼", layout="wide")

# 세션 상태 초기화 (로그인/데이터 저장용)
if 'user' not in st.session_state:
    st.session_state.user = None

# 1. 로그인/회원가입 로직 (간단 버전)
if st.session_state.user is None:
    st.title("🔐 과학 퀴즈 플랫폼 접속")
    tab1, tab2 = st.tabs(["로그인", "회원가입"])
    with tab1:
        u_id = st.text_input("아이디")
        u_pw = st.text_input("비밀번호", type="password")
        if st.button("로그인"):
            if u_id == "admin" and u_pw == "1234": # 마스터 계정 예시
                st.session_state.user = u_id
                st.rerun()
            else:
                st.error("아이디 또는 비밀번호가 틀립니다.")
    st.stop()

# 2. 메인 화면 (로그인 성공 후)
st.sidebar.title(f"👤 {st.session_state.user}님")
if st.sidebar.button("로그아웃"):
    st.session_state.user = None
    st.rerun()

menu = st.sidebar.selectbox("메뉴를 선택하세요", ["공지사항", "🔭 망원경 퀴즈", "🧪 화학 명명법", "🔢 지학 계산기"])

if menu == "공지사항":
    st.title("📢 알림판")
    st.write("마스터가 올린 공지나 퀴즈 정보를 여기서 확인하세요.")
    if st.session_state.user == "admin":
        st.info("관리자 모드: 아래에 퀴즈 데이터를 업데이트할 수 있는 기능을 추가할 예정입니다.")

elif menu == "🔭 망원경 퀴즈":
    st.title("🔭 망원경 구조 및 설치 퀴즈")
    st.write("`망원경.py`와 `망원경 구조.py` 로직이 여기에 들어갑니다.")

elif menu == "🧪 화학 명명법":
    st.title("🧪 화학 명명법 테스트")
    st.write("`화학 명명법.py` 로직이 여기에 들어갑니다.")

elif menu == "🔢 지학 계산기":
    st.title("🔢 지학 계산 문제")
    st.write("`지학.py` 로직이 여기에 들어갑니다.")
