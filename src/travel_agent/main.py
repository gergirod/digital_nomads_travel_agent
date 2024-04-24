#!/usr/bin/env python
from travel_agent.crew import DigitalNomadTravelCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'date': 'may 2024',
        'origin': 'Buenos Aires',
        'destination': 'Bali',
        'activities': ['surfing', 'yoga'],
        'preferences': {'coffee_shops': True, 'gyms': True, 'internet':True}
    }

    result = DigitalNomadTravelCrew().crew().kickoff(inputs=inputs)
    print(result)