
import sys
import shutil
from pathlib import Path

# Project Root
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import streamlit as st

from upload_manager import UploadManager
from frontend.api_client import APIClient

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Self-Healing RAG",
    page_icon="🤖",
    layout="wide"
)

# ==================================================
# COMPONENTS
# ==================================================

upload_manager = UploadManager()
api_client = APIClient()

# ==================================================
# SESSION STATE
# ==================================================

if "indexed_files" not in st.session_state:
    st.session_state.indexed_files = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("🤖 Self-Healing RAG")

    st.caption(
        "Upload documents and chat with them"
    )

    st.divider()

    uploaded_files = st.file_uploader(
        "📂 Upload Documents",
        accept_multiple_files=True
    )

    if uploaded_files:

        for uploaded_file in uploaded_files:

            if uploaded_file.name not in st.session_state.indexed_files:

                try:

                    file_path = upload_manager.save_file(
                        uploaded_file
                    )

                    api_client.upload_file(
                        file_path
                    )

                    st.session_state.indexed_files.append(
                        uploaded_file.name
                    )

                    st.success(
                        f"Indexed: {uploaded_file.name}"
                    )

                except Exception as e:

                    st.error(
                        f"Failed: {uploaded_file.name}"
                    )

                    st.exception(e)

    st.divider()

    st.subheader("📄 Indexed Documents")

    if st.session_state.indexed_files:

        for file_name in st.session_state.indexed_files:

            st.write(
                f"✅ {file_name}"
            )

    else:

        st.info(
            "No documents uploaded"
        )

    st.divider()

    if st.button(
        "🗑 Clear Chat"
    ):

        st.session_state.chat_history = []

        st.rerun()

    if st.button(
        "♻ Reset Session"
    ):

        st.session_state.chat_history = []

        st.session_state.indexed_files = []

        upload_dir = Path(
            "data/uploads"
        )

        chroma_dir = Path(
            "chroma_db"
        )

        try:

            if upload_dir.exists():

                shutil.rmtree(
                    upload_dir
                )

            upload_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            if chroma_dir.exists():

                shutil.rmtree(
                    chroma_dir
                )

        except Exception:
            pass

        st.success(
            "Session Reset"
        )

        st.rerun()

# ==================================================
# MAIN AREA
# ==================================================

st.title(
    "🤖 Self-Healing RAG Assistant"
)

st.caption(
    "Chat with your uploaded documents"
)

# ==================================================
# CHAT HISTORY
# ==================================================

for chat in st.session_state.chat_history:

    with st.chat_message(
        "user"
    ):

        st.write(
            chat["user"]
        )

    with st.chat_message(
        "assistant"
    ):

        st.write(
            chat["assistant"]
        )

# ==================================================
# CHAT INPUT
# ==================================================

query = st.chat_input(
    "Ask anything about your documents..."
)

if query:

    with st.chat_message(
        "user"
    ):

        st.write(
            query
        )

    try:

        with st.spinner(
            "Thinking..."
        ):

            result = api_client.chat(
                query
            )

        answer = result.get(
            "answer",
            "No answer returned."
        )

        st.session_state.chat_history.append(

            {
                "user": query,
                "assistant": answer,
                "debug": result
            }

        )

        with st.chat_message(
            "assistant"
        ):

            st.write(
                answer
            )

    except Exception as e:

        st.error(
            "Error generating answer."
        )

        st.exception(e)

