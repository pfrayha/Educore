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

class IClassManager(ABC):
    @abstractmethod
    def get_class_form(id=None):
        pass

    @abstractmethod
    def submit_class_form(id=None):
        pass

    @abstractmethod
    def get_classes():
        pass

    @abstractmethod
    def delete_class(id):
        pass

    @abstractmethod
    def populate_class(id):
        pass

class IGradeManager(ABC):
    @abstractmethod
    def get_grade_form(id=None):
        pass

    @abstractmethod
    def submit_grade_form(id=None):
        pass

    @abstractmethod
    def delete_grade(id):
        pass

class IPresenceManager(ABC):
    @abstractmethod
    def get_presence_form(id=None):
        pass

    @abstractmethod
    def submit_presence_form(id=None):
        pass

class IActivityManager(ABC):
    @abstractmethod
    def get_activity_form(id=None):
        pass

    @abstractmethod
    def submit_activity_form(id=None):
        pass

    @abstractmethod
    def get_activities():
        pass

    @abstractmethod
    def delete_activity(id):
        pass