import streamlit as st

# 초기화
if "page" not in st.session_state:
    st.session_state.page = "home"

# 페이지 이동 함수
def go_to(page_name):
    st.session_state.page = page_name

# 페이지 라우팅
if st.session_state.page == "home":
    st.markdown("""
    <h1 style='text-align: center;'>예비 판매자님을 위한<br>리뷰 기반 판매 예측 시스템</h1>
    """, unsafe_allow_html=True)

    # 박스 스타일 정의
    box_style = """
        width: 100%;
        height: 200px;
        border: 3px solid #4CAF50;
        border-radius: 15px;
        background-color: #e0f7fa;
        font-size: 24px;
        font-weight: bold;
        color: #333;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        white-space: pre-line;
        cursor: pointer;
    """

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.form("to_step1"):
            submitted = st.form_submit_button(
                label="STEP1\n어떤 카테고리의 물건을\n판매해야 할 지 모르겠어요", 
                use_container_width=True
            )
            if submitted:
                go_to("step1")


    with col2:
        with st.form("to_step2"):
            submitted = st.form_submit_button(
                label="STEP2\n판매전략은 짰는데\n이게 잘 될 지 모르겠어요", 
                use_container_width=True
            )
            if submitted:
                go_to("step2")


elif st.session_state.page == "step1":
    st.button("⬅️ 홈으로", on_click=go_to, args=("home",))
    st.title("STEP1")
    st.subheader("카테고리별 상위 판매자의 정보를 알려드려요")

elif st.session_state.page == "step2":
    st.button("⬅️ 홈으로", on_click=go_to, args=("home",))
    st.title("STEP2")
    st.subheader("판매 전략 적용 시 예상 결과 및 비슷한 제품을 알려드려요")
