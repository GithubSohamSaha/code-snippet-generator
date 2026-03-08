import streamlit as st
import uuid

from llm.llm_client import generate_code
from services.prompt_builder import build_prompt
from storage.chat_store import load_chats, save_chats

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Code Snippet Generator",
    layout="wide"
)

# --------------------------------------------------
# LOAD CHATS
# --------------------------------------------------
raw_chats = load_chats()
chats = {}

for cid, convo in raw_chats.items():
    if isinstance(convo, list):
        title = convo[0]["user"][:35] if convo else "New Chat"
        chats[cid] = {
            "title": title,
            "messages": convo
        }
    else:
        chats[cid] = convo

save_chats(chats)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "chat_id" not in st.session_state:
    if chats:
        st.session_state.chat_id = next(iter(chats))
    else:
        new_id = str(uuid.uuid4())
        chats[new_id] = {"title": "New Chat", "messages": []}
        save_chats(chats)
        st.session_state.chat_id = new_id

chat_id = st.session_state.chat_id

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("💬 Conversations")

# Create new conversation
if st.sidebar.button("➕ New Conversation", key="new_chat"):
    new_id = str(uuid.uuid4())
    chats[new_id] = {"title": "New Chat", "messages": []}
    save_chats(chats)
    st.session_state.chat_id = new_id
    st.rerun()

# Conversation list
for cid, convo in chats.items():
    if st.sidebar.button(convo["title"], key=f"chat_{cid}"):
        st.session_state.chat_id = cid
        st.rerun()

# Delete conversation
st.sidebar.markdown("---")
st.sidebar.subheader("🗑 Delete Conversation")

titles = {cid: convo["title"] for cid, convo in chats.items()}

selected_chat = st.sidebar.selectbox(
    "Select conversation",
    options=list(titles.values())
)

if st.sidebar.button("Delete Selected Chat"):

    delete_id = None
    for cid, title in titles.items():
        if title == selected_chat:
            delete_id = cid
            break

    if delete_id:
        del chats[delete_id]
        save_chats(chats)

        if chats:
            st.session_state.chat_id = next(iter(chats))
        else:
            new_id = str(uuid.uuid4())
            chats[new_id] = {"title": "New Chat", "messages": []}
            save_chats(chats)
            st.session_state.chat_id = new_id

        st.rerun()

# --------------------------------------------------
# MAIN UI
# --------------------------------------------------
st.title("🧠 Code Snippet Generator Agent")

language = st.selectbox(
    "Select Programming Language",
    ["Python", "Java", "C++", "JavaScript", "SQL"]
)

# --------------------------------------------------
# CHAT DISPLAY
# --------------------------------------------------
st.markdown("---")

chat_container = st.container()

with chat_container:
    for msg in chats[chat_id]["messages"]:
        st.markdown("**🧑 You:**")
        st.write(msg["user"])

        st.markdown("**🤖 Assistant:**")

        # ---------------- RESPONSE RENDER ----------------
        bot_text = msg["bot"]

        # Case 1: Proper markdown code block
        if "```" in bot_text:

            parts = bot_text.split("```")

            for part in parts:

                part = part.strip()

                if part.startswith(("python", "cpp", "java", "c", "javascript", "sql")):
                    code = part.split("\n", 1)[1] if "\n" in part else part
                    st.code(code)

                elif part:
                    st.write(part)

        # Case 2: Model forgot code block
        elif "def " in bot_text or "class " in bot_text:

            lines = bot_text.split("\n")

            code_lines = []
            explanation_lines = []

            for line in lines:
                if line.strip().startswith(("def ", "class ", "import ", "for ", "while ", "if ")):
                    code_lines.append(line)
                else:
                    explanation_lines.append(line)

            if code_lines:
                st.code("\n".join(code_lines))

            if explanation_lines:
                st.write("\n".join(explanation_lines))

        # Case 3: normal text
        else:
            st.write(bot_text)

# --------------------------------------------------
# INPUT AREA (BOTTOM)
# --------------------------------------------------
user_input = st.text_area(
    "Ask for a code snippet:",
    placeholder="Example: Write a program to print hello 100 times"
)

if st.button("Generate Code", key="generate_btn") and user_input.strip():

    with st.spinner("🧠 Generating code... Please wait"):
        prompt = build_prompt(user_input, language)
        response = generate_code(prompt)

    if chats[chat_id]["title"] == "New Chat":
        chats[chat_id]["title"] = user_input[:35]

    chats[chat_id]["messages"].append({
        "user": user_input,
        "bot": response
    })

    save_chats(chats)
    st.rerun()