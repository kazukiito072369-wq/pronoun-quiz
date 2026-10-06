import streamlit as st
import random

questions = {
    "私は": "I",
    "私の": "my",
    "私を": "me",
    "私のもの": "mine",

    "あなたは": "you",
    "あなたの": "your",
    "あなたを": "you",
    "あなたのもの": "yours",

    "彼は": "he",
    "彼の": "his",
    "彼を": "him",
    "彼のもの": "his",

    "彼女は": "she",
    "彼女の": "her",
    "彼女を": "her",
    "彼女のもの": "hers",

    "それは": "it",
    "それの": "its",
    "それを": "it",

    "私たちは": "we",
    "私たちの": "our",
    "私たちを": "us",
    "私たちのもの": "ours",

    "あなたたちは": "you",
    "あなたたちの": "your",
    "あなたたちを": "you",
    "あなたたちのもの": "yours",

    "彼らは": "they",
    "彼らの": "their",
    "彼らを": "them",
    "彼らのもの": "theirs"
}

st.title("英語 人称代名詞クイズ")

if "questions" not in st.session_state:
    st.session_state.questions = random.sample(list(questions.keys()), 10)
    st.session_state.number = 0
    st.session_state.results = []
    st.session_state.finished = False
    st.session_state.show_results = False

if st.session_state.finished:

    st.success("10問終了！")

    score = 0

    for result in st.session_state.results:
        if result["answer"] == result["correct"]:
            score += 1

    st.write("あなたの得点は", score, "/ 10")

    if st.button("今回の結果を見る"):
        st.session_state.show_results = True
        st.rerun()

    if st.session_state.show_results:

        st.write("### 今回の問題と結果")

        for i, result in enumerate(st.session_state.results):
            st.write("第", i + 1, "問")
            st.write("問題:", result["question"])
            st.write("あなたの答え:", result["answer"])
            st.write("正解:", result["correct"])

            if result["answer"] == result["correct"]:
                st.success("○ 正解")
            else:
                st.error("× 不正解")

    if st.button("もう一度挑戦"):
        st.session_state.questions = random.sample(list(questions.keys()), 10)
        st.session_state.number = 0
        st.session_state.results = []
        st.session_state.finished = False
        st.session_state.show_results = False
        st.rerun()

else:

    question = st.session_state.questions[st.session_state.number]

    st.write("第", st.session_state.number + 1, "問")
    st.write("「" + question + "」は英語で？")

    answer = st.text_input(
        "答えを入力してください",
        key="answer"+ str(st.session_state.number)
    )

    if st.button("回答"):

        if answer == questions[question]:
            st.success("正解！")
        else:
            st.error("不正解。正解は " + questions[question])

        st.session_state.results.append({
            "question": question,
            "answer": answer,
            "correct": questions[question]
        })

        if st.session_state.number < 9:
            st.session_state.number += 1
            st.rerun()
        else:
            st.session_state.finished = True
            st.rerun()