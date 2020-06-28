class ManagerHub():
    class __ManagerHub():
        def __init__(self, people_manager=None, report_manager=None):
            self.people_manager = people_manager
            self.report_manager = report_manager

    _hub_instance = None
    
    @staticmethod
    def configure_hub_instance(people_manager, report_manager):
        ManagerHub._hub_instance = ManagerHub.__ManagerHub(people_manager, report_manager)

    @staticmethod
    def get_hub_instance():
        return ManagerHub._hub_instance