import streamlit as st
import pandas as pd
import time

#Side bar components:
def side_bar():
    with st.sidebar:
        st.header('***LIFE PEEKING***')
        Options = [
            "Home",
            "Tasks",
            "Diary",
            "About"
        ]
        Side_button = st.radio('', Options)
        return Side_button
    
side_panel = side_bar()

#home
def Home():
    st.header('***WELCOME TO YOUR ORGANIZER***', text_alignment='center', divider='rainbow', width="stretch")
    

    # 1. Text input (optional quick note)
    note = st.text_input("Quick Note")
    if note:
        st.info(f"You wrote: {note}")

    # 2. Image
    st.subheader("Motivation")
    st.image("https://th.bing.com/th/id/OIP.CoOxsp4qtrGVWPwFVXICfQHaEK?w=271&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3", caption="Stay productive!")

    tasks = st.number_input('Tasks: ', value=0, key="tasks_input")
    water = st.number_input('Water: ', value=3, key="water_input")
    hours = st.number_input('Tasks: ', value=0, key="hours_input")
     # 3. Metrics in columns
    col1, col2, col3 = st.columns(3)
    col1.metric("Tasks Completed", 5 + tasks, f'+{tasks} today')
    col2.metric("Water Intake", f'{water}', f"+{water}")
    col3.metric("Study Hours", f"{hours} hrs", f"{hours}")

    # 4. Progress bar
    st.subheader("Weekly Goal Progress")
    st.progress(70)

    # Bar chart (example data)
    st.subheader("Tasks Done Per Day")
    data = pd.DataFrame({
        "Tasks": [1, 2, 3, 2, 4, 1, 3]
    }, index=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
    st.bar_chart(data)

    # 6. Button
    if st.button("Refresh Dashboard"):
        st.success("Dashboard updated!")
   
def Tasks():

    # Add new task
    task_name = st.text_input("Task Name")
    deadline = st.date_input("Deadline")
    category = st.selectbox("Category", ["Work", "Study", "Personal"])
    priority = st.radio("Priority", ["High", "Medium", "Low"])
    effort = st.slider("Effort (1-10)", 1, 10, 5)


    if st.button("Add Task"):
        st.success(f"Task '{task_name}' added under {category} with {priority} priority!")

    # Example task list
    data = pd.DataFrame({
        "Task": ["Finish report", "Study math", "Clean room"],
        "Category": ["Work", "Study", "Personal"],
        "Deadline": ["2026-03-12", "2026-03-13", "2026-03-14"],
        "Priority": ["High", "Medium", "Low"],
        "Status": ["Pending", "Completed", "Pending"]
    })
    st.subheader("Task List")
    st.dataframe(data)

    # Metrics and progress
    st.metric("Tasks Remaining", 2)
    st.progress(40)


#About
def About():
    st.header('***ABOUT THIS WEB APP***', text_alignment='center', divider='rainbow', width="stretch")
    st.write('''
    The purpose of this web app is to record you everyday activity, tasks, and story, 
    this is you personal productivity tool,a digital diary where you can access and 
    record your activities anywhere.
    ''')

    st.write('''
    this web app offers a tasks manager whereas you can write your activities, when it is the due date,
    and what items you need, and many more in the future
    ''')

    st.write('''
    And for future update, this app will offer a digital diary, where you can record your daily life, what happened, how satisfied you were, and how did it impact in your life,
    and the best part will be!: that only you the user can see, unless you publish it
    ''')

    st.image("data:image/jpeg;base64,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", width="stretch")


#choicer
if side_panel == "Home":
    Home()
elif side_panel == "About":
    About()
elif side_panel == "Tasks":
    Tasks()
else:
    st.warning('this is underconstruction')
    with st.spinner("TIme until update", show_time=True):
        time.sleep(9999999)
    st.success("Done!")