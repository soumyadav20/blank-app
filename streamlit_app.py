import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="MBA Time Manager", layout="wide")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Task creation form
st.title("🎓 MBA Time Manager")
with st.form("task_form"):
    st.subheader("➕ Add a New Task")
    title = st.text_input("Task Title")
    description = st.text_area("Task Description")
    estimated_time = st.number_input("Estimated Time (in minutes)", min_value=1)
    submitted = st.form_submit_button("Add Task")
    if submitted and title:
        st.session_state.tasks.append({
            "title": title,
            "description": description,
            "estimated_time": estimated_time,
            "created_at": datetime.now(),
            "status": "Pending",
            "actual_time": None,
            "completed_at": None
        })
        st.success(f"Task '{title}' added!")

# Display tasks
st.subheader("📋 Your Tasks")
for i, task in enumerate(st.session_state.tasks):
    with st.expander(f"{task['title']} ({task['status']})"):
        st.write(f"📝 Description: {task['description']}")
        st.write(f"⏳ Estimated Time: {task['estimated_time']} minutes")
        if task['status'] == "Completed":
            st.write(f"✅ Completed At: {task['completed_at'].strftime('%Y-%m-%d %H:%M')}")
            st.write(f"🕒 Actual Time: {task['actual_time']} minutes")
        else:
            if st.button(f"Mark as Done", key=f"done_{i}"):
                actual_time = st.number_input("Actual Time Spent (minutes)", key=f"actual_{i}", min_value=1)
                if actual_time:
                    st.session_state.tasks[i]['status'] = "Completed"
                    st.session_state.tasks[i]['actual_time'] = actual_time
                    st.session_state.tasks[i]['completed_at'] = datetime.now()
                    st.experimental_rerun()
