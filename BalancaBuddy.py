import streamlit as st

def main():
    st.title("Event Input App")

    # Event Name
    event_name = st.text_input("Event Name")

    # Type
    event_types = ["Work", "Fitness", "Family", "Social", "Study", "Meditation"]
    event_type = st.radio("Type", event_types)

    # Submit button
    if st.button("Submit"):
        if event_name and event_type:
            st.success(f"Event Submitted:\nEvent: {event_name}\nType: {event_type}")
        else:
            st.error("Please fill in all fields")

if __name__ == "__main__":
    main()

print("Streamlit app is running.")
