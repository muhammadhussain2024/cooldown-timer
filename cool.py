import streamlit as st
import time

st.title("⏳ Countdown Timer")


st.sidebar.title("⏲️ Set Timer")
minutes = st.sidebar.number_input("Minutes", min_value=0, max_value=60, value=0)
seconds = st.sidebar.number_input("Seconds", min_value=0, max_value=60, value=0)


if st.button("▶️ Start Countdown"):
    total_time = int(minutes * 60 + seconds)

    if total_time == 0:
        st.warning("Please set a time greater than 0.")
    else:
        countdown_placeholder = st.empty()

        for remaining in range(total_time, -1, -1):
            mins, secs = divmod(remaining, 60)
            timer_display = f"{mins:02d}:{secs:02d}"
            countdown_placeholder.header(f"⏰ {timer_display}")
            time.sleep(1)

        st.balloons()
        st.success("🎉 Time's up!")
