from abc import ABC, abstractmethod

class IRegistrationManager(ABC):
    @abstractmethod
    def get_registration_form(model):
        pass

    @abstractmethod
    def submit_registration_form(model, json_data):
        pass

class IReportManager(ABC):
    @abstractmethod
    def generate_report(student_id):
        pass