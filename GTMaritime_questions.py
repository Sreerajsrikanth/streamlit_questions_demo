import streamlit as st
import random
from datetime import datetime, timedelta

# Initialize session state variables
if 'current_streak' not in st.session_state:
    st.session_state.current_streak = 0
if 'questions_answered' not in st.session_state:
    st.session_state.questions_answered = 0
if 'current_questions' not in st.session_state:
    st.session_state.current_questions = []
if 'used_questions' not in st.session_state:
    st.session_state.used_questions = set()
if 'completion_history' not in st.session_state:
    # Mock 30 days of history data
    st.session_state.completion_history = {
        (datetime.now().date() - timedelta(days=x)): random.choice([True, True, True, False]) 
        for x in range(30, 0, -1)
    }
if 'longest_streak' not in st.session_state:
    st.session_state.longest_streak = 7 # Mock longest streak

# Helper function to calculate current and best streaks
def calculate_streaks():
    current_streak = st.session_state.current_streak
    best_streak = st.session_state.longest_streak
    return current_streak, best_streak

# Function to display streak calendar
def display_streak_calendar():
    st.markdown("### Your Safety Streak Calendar")
    
    # Create 5 columns for the last 5 weeks
    cols = st.columns(5)
    today = datetime.now().date()
    
    # Calculate color intensities based on streak
    for week in range(5):
        with cols[4-week]:  # Display most recent week on the right
            for day in range(7):
                date = today - timedelta(days=(week*7 + day))
                completed = st.session_state.completion_history.get(date, False)
                
                # Create colored box based on completion
                if completed:
                    box_color = "🟩"  # Green box for completed
                else:
                    box_color = "⬜"  # White box for not completed
                
                st.write(box_color)


# Sample questions from different categories
# Complete question bank from the document
QUESTIONS = {
    'PPE & Equipment Safety': [
        {'text': 'Was all required PPE available for your tasks today?', 'type': 'yes_no'},
        {'text': 'Did you face any issues with your safety equipment?', 'type': 'yes_no_comment'},
        {'text': 'Are your work boots in good condition?', 'type': 'yes_no'},
        {'text': 'How many times did you need to replace/adjust PPE during shift?', 'type': 'numeric'},
        {'text': 'Did you check your PPE before starting work?', 'type': 'yes_no'},
        {'text': 'Is your hard hat free from cracks or damage?', 'type': 'yes_no'},
        {'text': 'Were ear protection devices available when needed?', 'type': 'yes_no'},
        {'text': 'Did you observe anyone working without proper PPE?', 'type': 'yes_no_comment'},
        {'text': 'Rate the condition of your safety equipment', 'type': 'scale'},
        {'text': 'Were gloves appropriate for your assigned tasks?', 'type': 'yes_no'},
        {'text': 'Is your respiratory protection equipment working properly?', 'type': 'yes_no'},
        {'text': 'Rate your comfort level with PPE today', 'type': 'scale'}
    ],
    'Workplace Safety': [
        {'text': 'Did you notice any new hazards in your work area?', 'type': 'yes_no_comment'},
        {'text': 'Were all safety signs clearly visible?', 'type': 'yes_no'},
        {'text': 'Rate the lighting conditions in your work area', 'type': 'scale'},
        {'text': 'How many hazards did you identify today?', 'type': 'numeric'},
        {'text': 'Did you observe any slip/trip hazards today?', 'type': 'yes_no_comment'},
        {'text': 'Were emergency exits clear of obstacles?', 'type': 'yes_no'},
        {'text': 'Did you notice any unsafe electrical connections?', 'type': 'yes_no_comment'},
        {'text': 'Were firefighting equipment easily accessible?', 'type': 'yes_no'},
        {'text': 'How many spills required cleaning today?', 'type': 'numeric'},
        {'text': 'Were tools properly stored after use?', 'type': 'yes_no'},
        {'text': 'Did you observe proper lifting techniques being used?', 'type': 'yes_no'},
        {'text': 'Rate the ventilation in your work area', 'type': 'scale'},
        {'text': 'Was your workspace free from unnecessary obstacles?', 'type': 'yes_no'},
        {'text': 'Rate the overall cleanliness of your work area', 'type': 'scale'}
    ],
    'Safety Procedures & Communication': [
        {'text': 'Were safety permits properly filled before work?', 'type': 'yes_no'},
        {'text': 'Rate your understanding of today\'s safety briefing', 'type': 'scale'},
        {'text': 'Were emergency procedures clearly communicated?', 'type': 'yes_no'},
        {'text': 'How many safety concerns did you report today?', 'type': 'numeric'},
        {'text': 'Were toolbox talks conducted before critical tasks?', 'type': 'yes_no'},
        {'text': 'Did you feel rushed while performing any task?', 'type': 'yes_no'},
        {'text': 'Was the chain of command clear for safety issues?', 'type': 'yes_no'},
        {'text': 'How many safety meetings did you attend?', 'type': 'numeric'},
        {'text': 'Were safety instructions clear for your tasks?', 'type': 'yes_no'},
        {'text': 'Did you receive feedback on any safety suggestions?', 'type': 'yes_no'},
        {'text': 'Rate the effectiveness of shift handover communication', 'type': 'scale'},
        {'text': 'Did you understand all safety announcements?', 'type': 'yes_no'},
        {'text': 'How many near-misses were reported in your area?', 'type': 'numeric'},
        {'text': 'Did you feel comfortable raising safety concerns?', 'type': 'yes_no'}
    ],
    'Work Practices': [
        {'text': 'Did you follow all safety procedures today?', 'type': 'yes_no'},
        {'text': 'Were you able to complete tasks without shortcuts?', 'type': 'yes_no'},
        {'text': 'Did you have proper tools for all tasks?', 'type': 'yes_no'},
        {'text': 'Rate your energy level during your shift', 'type': 'scale'},
        {'text': 'How many hours into your shift are you now?', 'type': 'numeric'},
        {'text': 'Were you given adequate breaks?', 'type': 'yes_no'},
        {'text': 'Did you feel overworked at any point?', 'type': 'yes_no'},
        {'text': 'Were manual handling tasks done safely?', 'type': 'yes_no'},
        {'text': 'Did you check equipment before use?', 'type': 'yes_no'},
        {'text': 'Was adequate supervision available?', 'type': 'yes_no'},
        {'text': 'Did you face pressure to skip safety steps?', 'type': 'yes_no'},
        {'text': 'Were standard operating procedures followed?', 'type': 'yes_no'},
        {'text': 'How many hours was your shift today?', 'type': 'numeric'},
        {'text': 'Were safety checklists completed properly?', 'type': 'yes_no'}
    ],
    'Emergency Preparedness': [
        {'text': 'Do you know your muster station location?', 'type': 'yes_no'},
        {'text': 'Can you locate the nearest fire extinguisher?', 'type': 'yes_no'},
        {'text': 'Are emergency contact numbers visible?', 'type': 'yes_no'},
        {'text': 'Do you know the emergency evacuation route?', 'type': 'yes_no'},
        {'text': 'Rate your confidence in emergency procedures', 'type': 'scale'},
        {'text': 'Is emergency equipment properly maintained?', 'type': 'yes_no'},
        {'text': 'Do you know how to raise different alarms?', 'type': 'yes_no'},
        {'text': 'Rate your readiness for emergency response', 'type': 'scale'},
        {'text': 'Do you know your role during emergencies?', 'type': 'yes_no'}
    ],
    'Health & Wellness': [
        {'text': 'How many hours of continuous rest did you get?', 'type': 'numeric'},
        {'text': 'Rate your stress level today', 'type': 'scale'},
        {'text': 'Did you feel physically well during your shift?', 'type': 'yes_no'},
        {'text': 'How many liters of water did you drink?', 'type': 'numeric'},
        {'text': 'Rate the quality of meals today', 'type': 'scale'},
        {'text': 'Did you experience excessive fatigue?', 'type': 'yes_no'},
        {'text': 'Were you able to take scheduled breaks?', 'type': 'yes_no'},
        {'text': 'Did you experience any health concerns?', 'type': 'yes_no'},
        {'text': 'How many hours since your last meal?', 'type': 'numeric'}
    ],
    'Environmental Conditions': [
        {'text': 'Was noise level acceptable in your area?', 'type': 'yes_no'},
        {'text': 'Did you notice any unusual smells?', 'type': 'yes_no_comment'},
        {'text': 'What\'s the temperature in your work area?', 'type': 'numeric'},
        {'text': 'Did you observe any environmental spills?', 'type': 'yes_no'},
        {'text': 'Rate the air quality in your work area', 'type': 'scale'},
        {'text': 'Did you notice excessive vibration?', 'type': 'yes_no'},
        {'text': 'Were weather conditions affecting safety?', 'type': 'yes_no'},
        {'text': 'Was there adequate natural ventilation?', 'type': 'yes_no'},
        {'text': 'Did you observe proper waste disposal?', 'type': 'yes_no'}
    ],
    'Hygiene & Sanitation': [
        {'text': 'Were restrooms clean and functional?', 'type': 'yes_no'},
        {'text': 'Was the mess room properly maintained?', 'type': 'yes_no'},
        {'text': 'Were hand washing facilities available?', 'type': 'yes_no'},
        {'text': 'How many hours since drinking water was tested?', 'type': 'numeric'},
        {'text': 'Were food storage areas clean?', 'type': 'yes_no'},
        {'text': 'Was garbage properly segregated?', 'type': 'yes_no'},
        {'text': 'Were living quarters properly maintained?', 'type': 'yes_no'},
        {'text': 'Was pest control effective?', 'type': 'yes_no'},
        {'text': 'Rate the overall hygiene standards today', 'type': 'scale'}
    ]
}
def get_new_questions():
    """Get 3 random questions from different categories"""
    if len(st.session_state.used_questions) >= 90:  # All questions used
        st.session_state.used_questions.clear()
    
    categories = list(QUESTIONS.keys())
    selected_questions = []
    
    for category in random.sample(categories, 3):
        available_questions = [q for q in QUESTIONS[category] 
                             if (category, q['text']) not in st.session_state.used_questions]
        if available_questions:
            question = random.choice(available_questions)
            selected_questions.append((category, question))
            st.session_state.used_questions.add((category, question['text']))
    
    return selected_questions

def display_question(category, question):
    """Display a single question based on its type"""
    st.subheader(category)
    
    if question['type'] == 'yes_no':
        return st.radio(question['text'], ['Yes', 'No'], key=question['text'])
    
    elif question['type'] == 'yes_no_comment':
        response = st.radio(question['text'], ['Yes', 'No'], key=question['text'])
        if response == 'Yes':
            st.text_input('Please provide details:', key=f"comment_{question['text']}")
        return response
    
    elif question['type'] == 'scale':
        return st.slider(question['text'], 1, 5, 3, key=question['text'])
    
    elif question['type'] == 'numeric':
        return st.number_input(question['text'], min_value=0, max_value=24, key=question['text'])

def main():
    st.title("ShipArc Safety Questions Demo")
    
    # Display streak and progress
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Current Streak", f"{st.session_state.current_streak} days")
    with col2:
        st.metric("Questions Answered", st.session_state.questions_answered)
    
    # Get or generate current questions
    if not st.session_state.current_questions:
        st.session_state.current_questions = get_new_questions()
    
    # Display current questions
    with st.form("safety_questions"):
        for category, question in st.session_state.current_questions:
            display_question(category, question)
        
        submitted = st.form_submit_button("Submit Responses")
    
    # Handle form submission outside the form
    if submitted:
        st.session_state.current_streak += 1
        st.session_state.questions_answered += 3
        st.success("Responses submitted successfully!")
        st.balloons()
        
        # Clear current questions to prepare for next day
        st.session_state.current_questions = []

    # Separate "Simulate Next Day" functionality
    if st.session_state.current_questions:
        st.write("Please submit your responses before simulating the next day.")
    else:
        if st.button("Simulate Next Day"):
            st.session_state.current_questions = get_new_questions()
            st.experimental_rerun()


def main():
    st.title("ShipArc Safety Questions Demo")
    
    # Display streak information
    col1, col2, col3 = st.columns(3)
    current_streak, best_streak = calculate_streaks()
    
    with col1:
        st.metric("Current Streak", f"{current_streak} days", 
                 delta=f"+1" if current_streak > 0 else None)
    with col2:
        st.metric("Best Streak", f"{best_streak} days")
    with col3:
        st.metric("Total Questions", st.session_state.questions_answered)
    
    # Display streak calendar
    display_streak_calendar()
    
    # Display streak milestone messages
    if current_streak >= 5:
        st.success(f"🌟 Amazing! You've maintained your safety streak for {current_streak} days!")
    elif current_streak >= 3:
        st.info(f"👏 Well done! You're building a strong safety habit - {current_streak} days and counting!")
    
    # Add a small separation before questions
    st.markdown("---")
    
    # Get or generate current questions
    if not st.session_state.current_questions:
        st.session_state.current_questions = get_new_questions()
    
    # Display current questions
    with st.form("safety_questions"):
        for category, question in st.session_state.current_questions:
            display_question(category, question)
        
        submitted = st.form_submit_button("Submit Responses")
    
    # Handle form submission outside the form
    if submitted:
        st.session_state.current_streak += 1
        st.session_state.questions_answered += 3
        
        # Update completion history
        today = datetime.now().date()
        st.session_state.completion_history[today] = True
        
        # Update longest streak if current streak is higher
        if st.session_state.current_streak > st.session_state.longest_streak:
            st.session_state.longest_streak = st.session_state.current_streak
        
        st.success("Responses submitted successfully!")
        st.balloons()
        
        # Clear current questions to prepare for next day
        st.session_state.current_questions = []
    
    # Show "Next Day" button outside the form
    if not st.session_state.current_questions:
        if st.button("Simulate Next Day"):
            st.experimental_rerun()

if __name__ == "__main__":
    main()