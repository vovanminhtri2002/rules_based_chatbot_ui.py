import streamlit as st
from datetime import datetime

# Thiết lập cấu hình trang
st.set_page_config(page_title="ChatGPT Clone", layout="wide")

# Tiêu đề ứng dụng
st.title("🧠 ChatGPT UI Clone with Streamlit")

# Hàm xử lý phản hồi của chatbot
def respond_to_user(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hi":
        return (
            "Xin chào quý khách! Tôi có thể giúp gì cho quý khách?\n"
            "['Tư vấn mua hàng', 'Tra cứu bảo hành', 'Hỗ trợ kỹ thuật']"
        )
    elif user_input == "hello":
        return (
            "Xin chào, bạn cần tôi giúp gì không?\n"
            "['Tư vấn mua hàng', 'Tra cứu bảo hành', 'Hỗ trợ kỹ thuật']"
        )
    elif user_input == "tư vấn mua hàng":
        return ["Điện thoại", "Laptop", "Máy tính bảng"]
    elif user_input == "điện thoại":
        return "Quý khách muốn mua điện thoại nào ạ?"
    elif user_input == "laptop":
        return "Quý khách muốn mua laptop nào ạ?"
    elif user_input == "máy tính bảng":
        return "Quý khách muốn mua tablet nào ạ?"
    elif user_input == "tra cứu bảo hành":
        return ["Tra cứu bằng số điện thoại", "Tra cứu bằng IMEI"]
    elif user_input == "tra cứu bằng số điện thoại":
        return "Quý khách vui lòng nhập số điện thoại để tra cứu bảo hành"
    elif user_input == "tra cứu bằng imei":
        return "Quý khách vui lòng nhập IMEI để tra cứu bảo hành"
    elif user_input == "hỗ trợ kỹ thuật":
        return ["Lỗi phần cứng", "Lỗi phần mềm"]
    elif user_input == "lỗi phần cứng":
        return "Quý khách vui lòng mô tả lỗi phần cứng để được hỗ trợ"
    elif user_input == "lỗi phần mềm":
        return "Quý khách vui lòng mô tả lỗi phần mềm để được hỗ trợ"
    else:
        return "Xin lỗi! Tôi không hiểu yêu cầu của bạn. Bạn có thể nói rõ hơn không?"

# Khởi tạo session state để lưu lịch sử chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Hiển thị lịch sử chat
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        if isinstance(message["content"], list):
            st.markdown(", ".join(message["content"]))
        else:
            st.markdown(message["content"])

# Nhận đầu vào từ người dùng
prompt = st.chat_input("Nhập tin nhắn của bạn...")

if prompt:
    # Lưu tin nhắn người dùng vào lịch sử
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Hiển thị tin nhắn người dùng
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gọi hàm respond_to_user để lấy phản hồi
    response = respond_to_user(prompt)

    # Hiển thị phản hồi của chatbot
    with st.chat_message("assistant"):
        if isinstance(response, list):
            st.markdown(", ".join(response))
        else:
            st.markdown(response)

    # Lưu phản hồi vào lịch sử chat
    st.session_state.chat_history.append({"role": "assistant", "content": response})