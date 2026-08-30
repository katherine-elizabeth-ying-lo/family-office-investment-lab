import streamlit as st

st.set_page_config(
    page_title="Family Office Investment Lab",
    page_icon="📊",
    layout="wide"
)

st.title("Family Office Investment Lab")
st.caption("Multi-Asset Portfolio Construction, Benchmarking & Risk Analysis")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Illustrative Portfolio NAV", "£250m")

with col2:
    st.metric("Base Currency", "GBP")

with col3:
    st.metric("Investment Horizon", "Long-term")

st.info(
    "Mandate: Long-term capital preservation & growth"
)

st.caption(
    "Illustrative portfolio for analytical purposes only. "
    "Portfolio assumptions do not represent any specific family office."
)

st.header("Strategic Asset Allocation")

st.write("Portfolio model coming next.")
