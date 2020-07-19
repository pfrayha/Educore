from abc import ABC, abstractmethod

class IPeopleManager(ABC):
    @abstractmethod
    def get_registration_form(model, id=None):
        pass

    @abstractmethod
    def submit_registration_form(model, id=None):
        pass

    @abstractmethod
    def list_people(model):
        pass

    @abstractmethod
    def delete_person(model, id):
        pass
    
class IReportManager(ABC):
    @abstractmethod
    def generate_report(report_type, **kwargs):
        pass