import streamlit as st
import cohere
import config
import io

co = cohere.Client(config.COHERE_API_KEY)

def ai(prompt, tokens=800):
    try:
        r = co.chat(
            model="c4ai-aya-expanse-8b",
            message=prompt,
            temperature=0.3,
            max_tokens=tokens
        )
        return r.text.strip()
    except Exception as e:
        return f"Error: {e}"

def get_answer(question):
    prompt = f"Answer this question clearly and completely: {question}"
    return ai(prompt)

def export_chat(history):
    text = ""
    for i, item in enumerate(history, 1):
        text += f"You: {item['question']}\n"
        text += f"AI: {item['answer']}\n\n"
    return io.BytesIO(text.encode("utf-8"))

if "history" not in st.session_state:
    st.session_state.history = []

st.set_page_config(page_title="AI Assistant", layout="centered")

st.title("🤖 AI Assistant")
st.write("Ask me anything!")

col1, col2 = st.columns(2)
with col1:
    if st.button("New Chat"):
        st.session_state.history = []
        st.rerun()

with col2:
    if st.session_state.history:
        st.download_button(
            "Save Chat",
            data=export_chat(st.session_state.history),
            file_name="chat_history.txt",
            mime="text/plain"
        )

question = st.text_input("Type your question here:")

if st.button("Send"):
    if question.strip():
        with st.spinner("Thinking..."):
            answer = get_answer(question)
        
        st.session_state.history.append({
            "question": question,
            "answer": answer
        })
    else:
        st.warning("Please enter a question")

st.markdown("### Chat History")

for item in reversed(st.session_state.history):
    with st.container():
        st.markdown(f"**You:** {item['question']}")
        st.markdown(f"**AI:** {item['answer']}")
        st.markdown("---")