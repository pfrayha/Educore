from abc import ABC, abstractmethod

class IReportManager(ABC):
    @abstractmethod
    def generate_report(student_id):
        pass
    