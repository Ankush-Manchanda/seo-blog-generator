import streamlit as st
from scrape_amazon import get_trending_products
from get_keywords import get_keywords
from generate_blog import generate_blog

st.set_page_config(page_title="SEO Blog Generator", page_icon="📝")
st.title("📝 AI-Powered SEO Blog Generator")

# ✅ Cache product scraping to avoid refreshing on every rerun
@st.cache_data
def fetch_products():
    return get_trending_products()

# ✅ Fetch products once
products = fetch_products()

# ✅ Check if products were scraped successfully
if not products:
    st.error("❌ Could not load trending products. Please check your internet or scraping script.")
    st.stop()

# ✅ Session state to store blog and keywords
if "blog" not in st.session_state:
    st.session_state.blog = ""
    st.session_state.keywords = []

# ✅ UI: Product selector
selected = st.selectbox("Choose a trending product", products)

# ✅ Button to generate blog
if st.button("Generate Blog"):
    with st.spinner("🔍 Researching keywords and writing blog..."):
        keywords = get_keywords(selected)
        blog = generate_blog(selected, keywords)
        st.session_state.blog = blog
        st.session_state.keywords = keywords

# ✅ Display blog if available
if st.session_state.blog:
    st.subheader("🔑 SEO Keywords Used:")
    for kw in st.session_state.keywords:
        st.write(f"• {kw}")

    st.subheader("📝 Generated Blog:")
    st.write(st.session_state.blog)
