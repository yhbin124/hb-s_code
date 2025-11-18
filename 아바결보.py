import streamlit as st #외부 프로그램 불러오기
#컴퓨터에 python을 설치한 상태에서
#관리자 권한으로 CMD 실행
#pip install streamlit 입력 및 엔터
#cmd에 "run streamlit (파일위치)" 입력
# #이 프로그램 실행을 위해서는 python이 아니라 cmd를 통해 run시켜야함
#https://hb-scode-35df.streamlit.app/
recommended_books = {
    "STJ": ["일 잘하는 사람은 단순하게 합니다", "그릿"],
    "SFJ": ["나는 나로 살기로 했다", "말 그릇"],
    "SFP": ["시선으로부터,", "모든 순간이 너였다"],
    "STP": ["초집중", "행동의 기술"],
    "NFJ": ["어른의 문답법", "나는 생각이 너무 많아"],
    "NFP": ["죽고 싶지만 떡볶이는 먹고 싶어", "우리는 모두 조금 이상하다"],
    "NTJ": ["사피엔스", "리더의 조건"],
    "NTP": ["논리의 기술", "미움받을 용기"]
} #도서 추천 목록
questionsE = [
    "나는 책을 고를 때 장르나 분야를 따지지 않고 흥미가 가는 대로 선택한다.", #E
    "새로운 책을 읽다 흥미 있는 내용이 나오면 관련된 다른 분야의 책도 찾아본다.",#E
    "서점이나 도서관을 방문하면 여러 코너를 돌아다니며 다양한 책을 살펴본다.", #E
    "책 한 권을 읽고 나면 전혀 다른 스타일의 책을 선택해 기분을 전환하는 편이다.",#E
    "새로운 추천 도서가 들어오면 관심 분야가 아니어도 일단 시도해 본다.",#E
]
questionsI = [
    "독서 중에 나오는 새로운 개념이나 정보는 깊게 파고들기보다 대략적인 이해로 넘어간다.",
    "나는 여러 장르를 ‘얕고 넓게’ 경험하는 것이 한 장르를 깊게 파는 것보다 더 즐겁다.",
    "독서 모임에서 여러 책에 대해 가볍게 이야기하는 시간이 더 흥미롭다.",
    "책을 선택할 때 ‘새롭고 신선한 경험을 줄 수 있는가?’가 가장 중요한 기준이다.",
    "나는 독서를 통해 한 분야를 깊이 이해하기보다 다양한 세계를 경험하고 싶다."
]

questionsN =[
    "내용이 전부 기억나는 책이라도 재미있어서 거듭 읽고는 한다.",
    "내가 읽는 책은 대체로 소설, 에세이처럼 이야기가 있는 책이다.",
    "책 속 세계에 빠져 현실을 잠시 잊는 느낌이 좋다.",
    "책을 읽을 때 줄거리나 인물의 감정 변화에 몰입하는 편이다.",
    "책을 다 읽은 뒤, 내용보다는 인상적인 장면이나 문장이 기억에 오래 남는다.",#N
]
questionsS =[
    "책을 읽으면서 ‘이건 나중에 써먹어야겠다’는 생각을 자주 한다.",
    "책을 읽는 목적은 새로운 지식이나 정보를 얻기 위해서이다.",
    "책을 읽는 것은 나에게 휴식보다는 자기계발의 시간이다.",
    "모르는 단어나 개념이 책에서 나오면 반드시 찾아보고 넘어간다.",
    "구입한 책을 읽는 동안 밑줄을 치거나 메모를 자주 한다."
]

questionsF = [
    "책을 읽으며 내 삶이나 감정을 돌아보게 되는 경우가 많다.",
    "읽은 내용을 분석하기보다는 느낀 점이나 인상에 집중한다.",
    "책을 통해 인간의 본성이나 삶의 의미를 생각한다.",
    "책을 읽을 때 구체적인 사실이나 정보를 얻는 데 중점을 둔다.",
    "내용을 이해하는 것에 집중한다.", #F
]
questionsT =[
    "책을 통해 문제를 해결하거나 실생활에 적용할 수 있는 지식을 얻고자 한다.",
    "논리적이고 체계적인 설명이 담긴 글을 선호한다.",
    "저자의 주장과 근거가 논리적으로 타당한지 살펴본다.",
    "책을 읽을 때 기분보다는 내용을 중요시한다.",
    "책에 메시지나 주제가 없다면 읽지 않는 편이다."
]

questionsJ =[
    "나는 책을 읽기 전에 읽을 분량과 일정을 미리 정해두는 편이다.",
    "읽고 싶은 책이 생기면 현재 읽는 책을 마무리한 후 새 책을 시작한다.",
    "책을 읽을 때는 책갈피나 메모를 체계적으로 활용한다.",
    "독서 중 흥미가 떨어져도 끝까지 완독하려고 노력한다.",
    "나는 정해진 시간(예: 자기 전, 주말 오전)에 책을 읽는 습관이 있다.", #J
]
questionsP=[
    "서점이나 도서관에 가면 계획 없이 즉흥적으로 책을 고르는 경우가 많다.",
    "읽다 보면 그때그때 기분에 따라 다른 책으로 바꾸는 일이 자주 있다.",
    "책을 읽을 때는 줄거리나 목차를 미리 확인하지 않고 바로 본문부터 읽는다.",
    "독서 목표를 세워도 중간에 다른 흥미로운 책으로 갈아타는 경우가 많다.",
    "나는 독서 계획보다는 순간의 흥미나 직감을 더 중요하게 생각한다."
]

# 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "E" #시작 페이지 E
for trait in ["EI", "NS", "FT", "JP"]: #영역별 결과값 정의
    if trait not in st.session_state:
        st.session_state[trait] = 0
if "responses" not in st.session_state:#응답값 정의
    st.session_state.responses = {}
EI=0 #변수 선언
NS=0
FT=0
JP=0

# 페이지 전환 함수
def go_to(page_name):
    st.session_state.page = page_name



# --- IE ---
if st.session_state.page == "E": #페이지 불러오기
    st.title("독서 유형 검사 📚") #페이지 제목
    for i, q in enumerate(questionsE, 1):#리스트에서 문항 받아오기
        response1 = st.radio(q, [1, 2, 3, 4, 5], horizontal=True, key=f"E{i}")#선택창 띄우고 값 받기
        EI += response1 #값 누적
    for i, q in enumerate(questionsI, 1):
        response2 = st.radio(q, [1, 2, 3, 4, 5], horizontal=True, key=f"I{i}")
        EI += (6 - response2)
    st.session_state.EI= EI #값 정리
    st.button("다음 섹션으로 이동", on_click=lambda: go_to("NS")) #다음페이지 이동


# --- NS ---
elif st.session_state.page == "NS":
    st.markdown("""
    <script>
        window.scrollTo({top: 0, behavior: 'auto'});
    </script>
""", unsafe_allow_html=True)

    st.title('page 2')
    for i, q in enumerate(questionsN, 1):
        response = st.radio(q, [1, 2, 3, 4, 5], horizontal=True, key=f"N{i}")
        NS += response
    for i, q in enumerate(questionsS, 1):
        response = st.radio(q, [1, 2, 3, 4, 5], horizontal=True, key=f"S{i}")
        NS += (6 - response)
    st.session_state.NS = NS
    st.button("다음 섹션으로 이동", on_click=lambda: go_to("FT"))



# --- FT ---
elif st.session_state.page == "FT":
    st.title('page 3')
    for i, q in enumerate(questionsF, 1):
        response = st.radio(q, [1, 2, 3, 4, 5], horizontal=True, key=f"F{i}")
        FT += response
    for i, q in enumerate(questionsT, 1):
        response = st.radio(q, [1, 2, 3, 4, 5], horizontal=True, key=f"T{i}")
        FT += (6 - response)
    st.session_state.FT=FT
    st.button("다음 섹션으로 이동", on_click=lambda: go_to("JP"))




# --- JP ---
elif st.session_state.page == "JP":
    st.title('page 4')
    for i, q in enumerate(questionsJ, 1):
        response = st.radio(q, [1, 2, 3, 4, 5], horizontal=True, key=f"J{i}")
        JP += response
    for i, q in enumerate(questionsP, 1):
        response = st.radio(q, [1, 2, 3, 4, 5], horizontal=True, key=f"P{i}")
        JP += (6 - response)
    st.session_state.JP=JP
    st.button("제출", on_click=lambda: go_to("RESULT"))





elif st.session_state.page == "RESULT":
    s1 = st.session_state.EI #값 재정의
    s2 = st.session_state.NS
    s3 = st.session_state.FT
    s4 = st.session_state.JP
    ss1= int(s1/6*10)#비율 표시 위함
    ss2= int(s2/6*10)
    ss3= int(s3/6*10)
    ss4= int(s4/6*10)

    ei_type = "E" if s1 >= (60 - EI) else "I"# 비교를 통한 우위 항목 선택
    ns_type = "N" if s2 >= (60 - NS) else "S"
    ft_type = "F" if s3 >= (60 - FT) else "T"
    jp_type = "J" if s4 >= (60 - JP) else "P"
    mbti_result = ei_type + ns_type + ft_type + jp_type #독서성향 정의
    book_recommend = ns_type + ft_type + jp_type #도서 추천 용 독서성향
    result = "/ ".join(recommended_books[book_recommend])

    st.title("📊 결과 페이지")
    st.success("응답이 제출되었습니다!")
    st.write("당신의 응답 결과:")
    st.write("당신의 독서성향 유형은:", f"**{mbti_result}**")
    st.write("다음은 추천 도서 목록입니다!")
    st.write(result)
    st.write("꼭 한 번 읽어봐주세요")
    st.write()
    st.write(f"E = {ss1} : I = {100 - ss1}")
    st.write(f"N = {ss2} : S = {100 - ss2}")
    st.write(f"F = {ss3} : T = {100- ss3}")
    st.write(f"J = {ss4} : P = {100- ss4}")

    #최대점수 50 최저점수 10

