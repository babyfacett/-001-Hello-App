import streamlit as st


def main():
    """Simple Hello app demonstrating basic Streamlit components."""
    st.title("Hello アプリ")
    st.write("これはシンプルな Hello アプリです。名前を入力して挨拶してみましょう。")

    # Text input for the user's name
    name = st.text_input("あなたの名前を入力してください")

    # Button that triggers the greeting
    if st.button("挨拶する"):
        if name:
            st.success(f"こんにちは、{name}さん！")
        else:
            st.warning("名前を入力してください。")


if __name__ == "__main__":
    main()