import streamlit as st

from rag import generate_answer, process_urls

st.title('Real Estate Data Assistant')
url1 = st.sidebar.text_input('URL 1')
url2 = st.sidebar.text_input('URL 2')
url3 = st.sidebar.text_input('URL 3')
placeholder = st.empty()

submit_button = st.sidebar.button('Retrieve details')

if submit_button:
    urls = [url for url in (url1, url2,url3) if url != '']
    if len(urls) == 0:
        placeholder.text('Please provide atleast one valid URL')
    else:
        for status in process_urls(urls):
            placeholder.text(status)

query = placeholder.text_input('Enter here')
if query:
    try:
        answer, sources = generate_answer(query)
        st.header("Answer: ")
        st.write(answer)

        if sources:
            st.subheader("Sources:")
            for source in sources.split("\n"):
                st.write(source)
    except RuntimeError as e:
        placeholder.text("Please provide the url's first")