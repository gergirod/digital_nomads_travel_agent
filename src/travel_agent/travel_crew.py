from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_community.agent_toolkits.amadeus.toolkit import AmadeusToolkit
from langchain_community.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv

load_dotenv()
amadeusTools = AmadeusToolkit()
search = GoogleSerperAPIWrapper()

@CrewBase
class TravelCrew:
    agents_config = 'config/travel_agents.yaml'
    tasks_config = 'config/travel_tasks.yaml'
    
    @agent
    def inmigration_agent(self) -> Agent:
		
        
        return Agent(
            config=self.agents_config['inmigration_agent'],
            tool=[search],
            verbose=True
        )

    @agent
    def flights_research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['flights_research_agent'],
            tool=[amadeusTools, search],
            verbose=True,
        )

    @agent
    def travel_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['travel_agent'],
            verbose=True,
        )    

    @task
    def inmigration_task(self) -> Task:
        return Task(
            config=self.tasks_config['inmigration_task'],
            agent=self.inmigration_agent()
        )


    @task
    def flight_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['flight_search_task'],
            agent=self.flights_research_agent()
        )

    @task
    def travel_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config['travel_agent_task'],
            agent=self.travel_agent()
        )

    @crew
    def travel_crew(self) -> Crew:
        return Crew(
            agents=[self.inmigration_agent(), self.flights_research_agent(), self.travel_agent()],
            tasks=[self.inmigration_task(), self.flight_search_task(), self.travel_agent_task()],
        	process=Process.sequential,
            verbose=2,
        )
    
    @agent
    def accommodation_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['accommodation_specialist'],
            tool=[search],
            verbose=True
        )
    
    @task
    def accommodation_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['accommodation_search_task'],
            agent=self.accommodation_specialist(),
        )
    
    @agent
    def nomad_health_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['nomad_health_agent'],
            tool=[search],
            verbose=True
        )

    
    @task
    def health_wellness_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['health_wellness_plan_task'],
            agent=self.nomad_health_agent(),
        )
    

    @agent
    def accomodation_and_daily_planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['accomodation_and_daily_planner_agent'],
            verbose=True
        )

    
    @task
    def daily_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config['daily_agent_task'],
            agent=self.accomodation_and_daily_planner_agent(),
        )

    @crew
    def daily_nomad_travel_crew(self) -> Crew:
        """Creates the DigitalNomadTravelCrew."""
        return Crew(
            agents= [self.accommodation_specialist(), self.nomad_health_agent(), self.accomodation_and_daily_planner_agent()],
            tasks=[self.accommodation_search_task(), self.health_wellness_plan_task(), self.daily_agent_task()],
        	process=Process.sequential,
            verbose=2,
        )

