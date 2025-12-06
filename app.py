import streamlit as st
import jdatetime

def main():
    st.set_page_config(page_title="تبدیل تاریخ شمسی به میلادی", page_icon="📆")

    st.title("📆 تبدیل تاریخ شمسی به میلادی")
    st.write("سال، ماه و روز شمسی رو وارد کن تا تاریخ میلادی رو بهت بدم.")

    year = st.number_input("سال", min_value=1300, max_value=1500, step=1)
    month = st.number_input("ماه", min_value=1, max_value=12, step=1)
    day = st.number_input("روز", min_value=1, max_value=31, step=1)

    if st.button("تبدیل کن"):
        try:
            d = jdatetime.date(int(year), int(month), int(day)).togregorian()
            st.success(f"تاریخ میلادی: {d}")
        except Exception as e:
            st.error("تاریخ وارد شده معتبر نیست.")

if __name__ == "__main__":
    main()
