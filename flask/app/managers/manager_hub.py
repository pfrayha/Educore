class ManagerHub():
    class __ManagerHub():
        def __init__(self, registration_manager):
            self.registration_manager = registration_manager

    _hub_instance = None
    
    @staticmethod
    def configure_hub_instance(registration_manager):
        ManagerHub._hub_instance = ManagerHub.__ManagerHub(registration_manager)

    @staticmethod
    def get_hub_instance():
        return ManagerHub._hub_instance