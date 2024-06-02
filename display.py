import streamlit as st

def display_rankings(rankings):
    for ranking in rankings:
        st.write(f"キーワード: {ranking['keyword']}")
        if ranking['rank'] is not None:
            st.write(f"順位: {ranking['rank']}")
            st.write(f"タイトル: {ranking['title']}")
            st.write(f"スニペット: {ranking['snippet']}")
            st.write(f"リンク: {ranking['url']}")
        else:
            st.write("順位: 圏外")
        st.write("\n")
