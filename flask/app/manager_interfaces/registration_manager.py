from abc import ABC, abstractmethod

class IRegistrationManager(ABC):
    @abstractmethod
    def get_registration_form():
        pass

    @abstractmethod
    def submit_registration_form(json_data):
        pass
    