#!/usr/bin/env python
from travel_agent.travel_crew import TravelCrew
import streamlit as st
import datetime as dt

st.set_page_config(layout="wide", page_title="Nomad Travel Helper", page_icon=":airplane:")

st.subheader('Flight Details')

col1, col2 = st.columns(2)

with col1:
    origin = st.text_input('Origin', 'Buenos Aires')
    date = st.date_input('Departure Date', min_value=dt.date.today())

with col2:
    destination = st.text_input('Destination', 'Tokyo, Japan')
    passport = st.selectbox(
        'Which passport will you be using?',
        ['USA', 'Argentina', 'Australia', 'Germany', 'France', 'Japan', 'Other']
    )

# Accommodation, Activities, and Health Preferences using expander to avoid clutter
with st.expander("Accommodation Preferences", expanded=True):
    accommodation_preferences = st.multiselect(
        'Select your accommodation preferences',
        [
            "Reliable high-speed internet", "Desk or dedicated workspace", "Central location",
            "Quiet environment", "Flexible lease terms", "Co-living options", "Proximity to co-working spaces",
            "Public transport access", "Fully furnished", "Laundry facilities", "Kitchen facilities",
            "Safety and security features", "Nearby leisure activities", "Cultural attractions",
            "Pet-friendly accommodations", "Budget-friendly options", "Short-term rental availability",
            "Community events and activities", "Support services for foreigners", "Environmentally sustainable practices"
        ]
    )

with st.expander("Activities and Health Preferences"):
    activities_list = st.multiselect(
        'Select Preferred Activities',
        ["Surf", "Photography", "Networking Events", "Local Meetups", "Tech Conferences",
         "Sports", "Cultural tours", "Hiking", "Outdoor sports", "Yoga and wellness",
         "Scuba diving", "Mountain biking", "Skiing or snowboarding", "Live music events",
         "Food and culinary experiences", "Street art exploration", "Language exchange meetups",
         "Volunteering with local communities", "Rock climbing", "Kayaking or canoeing",
         "Safari tours", "Historical site visits"],
        default=['Surf']
    )
    health_preferences = st.multiselect(
        'Select your Health Preferences',
        ["Access to gyms and fitness centers", "Availability of yoga and meditation classes",
         "Proximity to walking and biking trails", "Availability of outdoor exercise areas",
         "Swimming facilities", "Vegan diet options", "Vegetarian diet options", "Keto diet options",
         "Paleo diet options", "Gluten-free options", "Organic food availability", "Farm-to-table dining experiences",
         "Healthy snack options", "Juice and smoothie bars", "Nutritional counseling services",
         "Mindfulness and wellness workshops", "Spa and massage services", "Therapeutic environments",
         "Sleep quality enhancements", "Stress management programs"]
    )

with st.expander("Work Environment Preferences"):
    work_environment_preferences = st.multiselect(
        'Select Work Environment Preferences',
        ["Quiet areas", "Library", "Cafe", "Co-working spaces", "Outdoor work areas", "Private offices",
         "Hotel lounges", "University campuses", "Tech hubs", "Beachfront locations", "Mountain retreats",
         "Creative spaces", "Artistic communities", "Community centers", "Rooftop terraces", "Garden settings",
         "Floating offices (boats)", "Historic buildings"],
        default=['Quiet areas', 'Co-working spaces']
    )

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

def on_button_click():
    # Update the session state to indicate the button has been clicked
    st.session_state.button_clicked = True


if st.button('Submit', disabled=st.session_state.button_clicked):
    on_button_click()
    with st.spinner('Processing your preferences... Please wait.'):
        travel_inputs = {
            'nationality': passport,
            'from_date': date,
            'origin': origin,
            'destination': destination,
            'activities': activities_list,
            'work_environment_preferences': work_environment_preferences,
            'health_preferences': health_preferences,
            'accomodation_preferences': accommodation_preferences
        }

        daily_nomad_inputs = {
            'from_date': date,
            'destination': destination,
            'activities': activities_list,
            'work_environment_preferences': work_environment_preferences,
            'health_preferences': health_preferences,
            'accomodation_preferences': accommodation_preferences
        }

        travel_crew = TravelCrew()

        travel_result = travel_crew.travel_crew().kickoff(inputs=travel_inputs)
        daily_nomad_result = travel_crew.daily_nomad_travel_crew().kickoff(inputs=daily_nomad_inputs)

        st.success('Done')
        st.text(travel_result)
        st.text(daily_nomad_result)

