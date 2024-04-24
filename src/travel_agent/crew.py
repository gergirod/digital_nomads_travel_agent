from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_community.agent_toolkits.amadeus.toolkit import AmadeusToolkit
from langchain_community.utilities import GoogleSerperAPIWrapper

amadeusTools = AmadeusToolkit()
search = GoogleSerperAPIWrapper()


@CrewBase
class DigitalNomadTravelCrew:
    """Crew setup for a digital nomad travel agency."""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def travel_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['travel_agent'],
            tool=[amadeusTools, search],
            verbose=True
        )

    @agent
    def accommodation_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['accommodation_specialist'],
            tool=[search],
            verbose=True,
        
        )
    
    @agent
    def routine_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['routine_planner'],
            verbose=True
        )

    @agent
    def activity_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['activity_coordinator'],
            tool=[search],
            verbose=True
        )


    @task
    def flight_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['flight_search_task'],
            agent=self.travel_agent()
        )

    @task
    def accommodation_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['accommodation_search_task'],
            agent=self.accommodation_specialist()
        )

    @task
    def activity_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['activity_planning_task'],
            agent=self.activity_coordinator()
        )

    @task
    def routine_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['routine_planning_task'],
            agent=self.routine_planner()
        )
    
    @task
    def compile_travel_itinerary_task(self) -> Task:
        return Task(
            config=self.tasks_config['compile_travel_itinerary_task'],
            agent=self.activity_coordinator(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the DigitalNomadTravelCrew."""
        return Crew(
            agents= self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2
        )

