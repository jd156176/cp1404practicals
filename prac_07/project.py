class Project:
    """Represent project details as an object"""

    def __init__(self, name="", start_date=None, priority=0, cost_estimate =0.0, completion_percentage=0):
        self.name = name
        self.start_date = start_date #expects a date.time object
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return (f"[{self.name}] Start Date:{self.start_date} Priority:{self.priority} Cost Estimate:{self.cost_estimate}"
                f"Completion Percentage:{self.completion_percentage}")

    def __repr__(self):
        return str(self)

    def to_file_line(self):
        """Formate the project details as a tab-separated string for file output."""
        return f"{self.name}\t{self.start_date}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"

    def is_complete(self):
        """Identify objects that have a 100 percent completion"""
        return self.completion_percentage >= 100

    def __lt__(self, other):
        return self.start_date < other.start_date