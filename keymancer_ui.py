import streamlit as st
from keymancer_core import GeneratorFactory 
from datetime import datetime
import csv
import io
from mnemonic import Mnemonic
from kemancer_tips import get_tip


st.set_page_config(
    page_title="Keymancer - Password Generator",
    page_icon="https://raw.githubusercontent.com/amirhosseinmirzaei9/Keymancer/main/img/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <meta name="google-site-verification" content="gukWY3PMRhLuWiRg7Q7cuX1tRZb__Ll7bDfqnwNwCbA" />
    """,
    unsafe_allow_html=True
)



st.title(":closed_lock_with_key: Keymancer")
st.subheader("The ultimate password & security wizard 🧙‍♂️")

col1, col2 = st.columns([2, 1])

with col1:

    st.markdown("---")
    st.subheader("Generator")
    kind = st.selectbox("Type", ["random", "pin", "passphrase"], index=0)

    if kind == "random":
        length = st.slider("Length", 8, 128, 16)
        use_upper = st.checkbox("Uppercase", True, help="Include uppercase letters (A-Z) in the password")
        use_lower = st.checkbox("Lowercase", True, help="Include lowercase letters (a-z) in the password")
        use_digits = st.checkbox("Digits", True, help="Include numbers (0-9) in the password")
        use_symbols = st.checkbox("Symbols", True, help="Include special characters (!@#$%) in the password")
        gen = GeneratorFactory.create("random",
                                     length=length,
                                     use_upper=use_upper,
                                     use_lower=use_lower,
                                     use_digits=use_digits,
                                     use_symbols=use_symbols,
                                    )
    elif kind == "pin":
        length = st.slider("PIN length", 4, 16, 8)
        gen = GeneratorFactory.create("pin", length=length)
    else:  # passphrase
        words = st.slider("Number of words", 2, 8, 4)
        sep = st.text_input("Separator", "-")
        lang = st.selectbox("Languages", Mnemonic.list_languages())
        gen = GeneratorFactory.create("passphrase", words=words, separator=sep, language=lang )

    st.markdown("---")
    st.subheader("Batch")
    batch = st.number_input("Generate Count (batch)", min_value=1, max_value=1000, value=1, step=1)
    st.toggle("Show as masked (only in UI)", value=False, key="masked")
    if st.button("Generate"):
        with st.spinner("Generating passwords..."):
            results = [gen.generate() for _ in range(batch)]
            st.session_state["latest_results"] = results
            st.success(f"Generated {len(results)} item(s)")
        

    if "latest_results" in st.session_state:
        results = st.session_state["latest_results"]
        st.write("### Results")
        masked = st.session_state.get("masked", False)
        cols = st.columns(2)
        for i, r in enumerate(results):
            with cols[i % 2]:
                st.code(f"{i}. {r}")


        # for i, r in enumerate(results, 1):
        #     display = "*" * len(r) if masked else r 
        #     st.code(f"{i}. {display}")


        # download options
        buf = io.StringIO()
        writer = csv.writer(buf)
        writer.writerow(["index", "value", "generated_at"])
        now = datetime.utcnow().isoformat() + "Z"
        for i, r in enumerate(results, 1):
            writer.writerow([i, r, now])
        file_name = f"passwords_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.csv"
        st.download_button("Download CSV", data=buf.getvalue(), file_name=file_name, mime="text/csv", key=f"download_{datetime.utcnow().timestamp()}")


with col2:
    st.subheader("ℹ️ About Keymancer")
    
    with st.expander("Learn more about Keymancer"):
        st.markdown("""
        **Keymancer** is a **CLI & Web-based** password and passphrase generator.  
        It helps you create secure, unique, and memorable credentials with ease.

        🛡️ **Key Features:**
        - Generate **random passwords**, **PIN codes**, and **passphrases**  
        - Multi-language support for passphrases (English, French, Japanese, etc.)  
        - Batch generation & **CSV export** for easy management  
        - Open-source & **privacy-first** design  

        📂 **Resource:**  
        - [GitHub Repository](https://github.com/amirhosseinmirzaei9/Keymancer)  
        """)

    st.markdown("---")

    st.subheader("💡 Tip of the Day")
    tip = st.success(get_tip())
    print(tip)
    if st.button("💡 Another Tip"):
        print(tip)

