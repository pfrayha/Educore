from abc import ABC, abstractmethod

class IPeopleManager(ABC):
    @abstractmethod
    def get_registration_form(model, id=None):
        pass

    @abstractmethod
    def submit_registration_form(model, id=None):
        pass

class IReportManager(ABC):
    @abstractmethod
    def generate_report(student_id):
        pass