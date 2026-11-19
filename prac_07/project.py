"""
Project class module for Project Management Program.
Estimated time: 50 minutes
Actual time:
"""
import datetime


class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name: str, start_date: datetime.date, priority: int,
                 cost_estimate: float, completion_percentage: int):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a formatted string representation of a Project."""
        date_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {date_str}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare projects based on priority (lower number means higher priority)."""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if the project is 100% complete."""
        return self.completion_percentage == 100
