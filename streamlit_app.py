import streamlit as st
from ranking import check_rankings
from display import display_rankings
from fetch import validate_api_key

st.title("自然検索順位アプリ")

# Step 1: API Key and Custom Search Engine ID
if 'api_key' not in st.session_state:
    st.session_state.api_key = ''
if 'cse_id' not in st.session_state:
    st.session_state.cse_id = ''

if not st.session_state.api_key or not st.session_state.cse_id:
    api_key = st.text_input("Google Search API Key")
    cse_id = st.text_input("Google Engine ID")

    if st.button("確認"):
        if validate_api_key(api_key, cse_id):
            st.session_state.api_key = api_key
            st.session_state.cse_id = cse_id
            st.experimental_rerun()  # 入力後に再読み込みしてAPIキーとIDをセッションに保存
        else:
            st.error("無効なAPIキーまたはカスタム検索エンジンIDです。再度確認してください。")
else:
    st.success("APIキーとカスタム検索エンジンIDが設定されました。")

    # Step 2: Target URL and Keywords
    target_url = st.text_input("ターゲットURL", "https://porely.jp/")
    keywords_input = st.text_area("キーワード（カンマ区切り）", "妊娠, 出産, 育児, キャリア, 育休, 医師, 職場 復帰, パートナーシップ")

    if 'max_results' not in st.session_state:
        st.session_state.max_results = 30

    max_results = st.number_input("最大の検索結果の件数", min_value=10, max_value=100, value=st.session_state.max_results, step=10)

    if target_url and keywords_input:
        st.session_state.target_url = target_url
        st.session_state.keywords_input = keywords_input
        st.session_state.max_results = max_results

        if st.button("検索"):
            keywords = [keyword.strip() for keyword in keywords_input.split(",")]
            rankings = check_rankings(keywords, target_url, st.session_state.api_key, st.session_state.cse_id, max_results=max_results)
            display_rankings(rankings)
