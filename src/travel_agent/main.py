#!/usr/bin/env python
from travel_agent.travel_crew import TravelCrew
import streamlit as st

st.title('Digital Nomad Travel and Daily Routine Helper')


    # User input fields
st.subheader('Flight Details')
origin = st.text_input('Origin', 'Buenos Aires')
destination = st.text_input('Destination', 'Tokyo, Japan')
date = st.date_input('Departure Date')
st.subheader('Passport Information')
passport = st.selectbox(
        'Which passport will you be using?',
        ['USA', 'Argentina', 'Australia', 'Germany', 'France', 'Japan', 'Other']
    )
st.subheader('Accomodation Preferences')
accomodation_preferences = st.multiselect(
    'Select your accomdation preferences',
    [
    "Reliable high-speed internet",
    "Desk or dedicated workspace",
    "Central location",
    "Quiet environment",
    "Flexible lease terms",
    "Co-living options",
    "Proximity to co-working spaces",
    "Public transport access",
    "Fully furnished",
    "Laundry facilities",
    "Kitchen facilities",
    "Safety and security features",
    "Nearby leisure activities",
    "Cultural attractions",
    "Pet-friendly accommodations",
    "Budget-friendly options",
    "Short-term rental availability",
    "Community events and activities",
    "Support services for foreigners",
    "Environmentally sustainable practices"
]
)
st.subheader('Activities Preferences')
activities_list = st.multiselect(
        'Select Preferred Activities',
        ["Surf",
        "Photography",
        "Networking Events",
        "Local Meetups",
        "Tech Conferences",
        "Sports",
        "Cultural tours",
        "Hiking",
        "Outdoor sports",
        "Yoga and wellness",
        "Scuba diving",
        "Mountain biking",
        "Skiing or snowboarding",
        "Live music events",
        "Food and culinary experiences",
        "Street art exploration",
        "Language exchange meetups",
        "Volunteering with local communities",
        "Rock climbing",
        "Kayaking or canoeing",
        "Safari tours",
        "Historical site visits"],
        default=['Surf']
    )

st.subheader('Health Preferences')
health_preferences = st.multiselect(
    'Select your Health Preferences',
    [
    "Access to gyms and fitness centers",
    "Availability of yoga and meditation classes",
    "Proximity to walking and biking trails",
    "Availability of outdoor exercise areas",
    "Swimming facilities",
    "Vegan diet options",
    "Vegetarian diet options",
    "Keto diet options",
    "Paleo diet options",
    "Gluten-free options",
    "Organic food availability",
    "Farm-to-table dining experiences",
    "Healthy snack options",
    "Juice and smoothie bars",
    "Nutritional counseling services",
    "Mindfulness and wellness workshops",
    "Spa and massage services",
    "Therapeutic environments",
    "Sleep quality enhancements",
    "Stress management programs"
]
)

st.subheader('Work Environment Preferences')
    # Work environment preferences
work_environment_preferences = st.multiselect(
        'Work Environment Preferences',
        ["Quiet areas",
        "Library",
        "Cafe",
        "Co-working spaces",
        "Outdoor work areas",
        "Private offices",
        "Hotel lounges",
        "University campuses",
        "Tech hubs",
        "Beachfront locations",
        "Mountain retreats",
        "Creative spaces",
        "Artistic communities",
        "Community centers",
        "Rooftop terraces",
        "Garden settings",
        "Floating offices (boats)",
        "Historic buildings"],
        default=['Quiet areas', 'Co-working spaces']
    )


if st.button('Submit Preferences'):
    travel_inputs = {
        'nationality': passport,
        'from_date':date,
        'origin': origin,
        'destination': destination,
        'activities': activities_list,
        'work_environment_preferences': work_environment_preferences,
        'health_preferences': health_preferences,
        'accomodation_preferences': accomodation_preferences
    }

    daily_nomad_inputs = {
        'from_date': date,
        'destination': destination,
        'activities': activities_list,
        'work_environment_preferences': work_environment_preferences,
        'health_preferences': health_preferences,
        'accomodation_preferences': accomodation_preferences
    }

    travel_crew = TravelCrew()

    travel_result = travel_crew.travel_crew().kickoff(inputs=travel_inputs)
    daily_nomad_result = travel_crew.daily_nomad_travel_crew().kickoff(inputs = daily_nomad_inputs)

    with st.spinner('Proccessing'):
         st.success('Done')
         print(travel_result)
         print(daily_nomad_result)

         st.text(travel_result)
         st.text(daily_nomad_result)


