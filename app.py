import streamlit as st
st.title("Sample App 2: A little more complex web app")

st.write("##### 動作モード1: 文字数カウント")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで文字数をカウントできます。")
st.write("##### 動作モード2: BMI値の計算")
st.write("身長と体重を入力することで、肥満度を表す体型指数のBMI値を算出できます。")

selected_mode = st.radio(
    "動作モードを選択してください。",
    ["文字数カウント", "BMI値の計算"]
)

st.divider()

if selected_mode == "文字数カウント":
    input_message = st.text_input(label="文字数のカウント対象となるテキストを入力してください。")
    text_count = len(input_message)
elif selected_mode == "BMI値の計算":
    height = st.number_input(label="身長(cm)を入力してください。", min_value=0)
    weight = st.number_input(label="体重(kg)を入力してください。", min_value=0)
    if height > 0:
        bmi = weight / ((height / 100) ** 2)
        bmi = round(bmi, 2)
    else:
        bmi = 0

if st.button("実行"):
    st.divider()
    if selected_mode == "文字数カウント":
        st.write(f"文字数: **{text_count}**")
    elif selected_mode == "BMI値の計算":
            st.write(f"BMI値: **{bmi}**")