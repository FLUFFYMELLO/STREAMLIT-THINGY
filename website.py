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