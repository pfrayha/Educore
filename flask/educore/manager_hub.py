class ManagerHub():
    """
        Singleton static wrapper class used to encapsulate the central instance
        
        Attributes
        ----------
        _hub_instance : _ManagerHub
            Single reference to _ManagerHub used externally to access managers
        
        Methods
        ---------
        get_hub_instance():
            Getter for internal instance
        
        configure_hub_instance(people_manager, report_manager, class_manager, grade_manager, presence_manager, activity_manager):
            Function used for configuration of internal instance
    """
    
    class __ManagerHub():
        """
            ManagerHub inner class responsable for being a single central point that holds
            the references to all the manager implementations
            
            Attributes
            ----------
            people_manager : IPeopleManager
                Static class reference to a class that implements the methods defined
                by the interface IPeopleManager
            report_manager : IReportManager
                Static class reference to a class that implements the methods defined
                by the interface IReportManager
            class_manager : IClassManager
                Static class reference to a class that implements the methods defined
                by the interface IClassManager
            grade_manager : IGradeManager
                Static class reference to a class that implements the methods defined
                by the interface IGradeManager
            presence_manager : IPresenceManager
                Static class reference to a class that implements the methods defined
                by the interface IPresenceManager
            activity_manager : IActivityManager
                Static class reference to a class that implements the methods defined
                by the interface IActivityManager
                
        """
        def __init__(self, people_manager=None, report_manager=None, class_manager=None, grade_manager=None, presence_manager=None, activity_manager=None):
            self.people_manager = people_manager
            self.report_manager = report_manager
            self.class_manager = class_manager
            self.grade_manager = grade_manager
            self.presence_manager = presence_manager
            self.activity_manager = activity_manager

    _hub_instance = None
    
    @staticmethod
    def configure_hub_instance(people_manager=None, report_manager=None, class_manager=None, grade_manager=None, presence_manager=None, activity_manager=None):
        ManagerHub._hub_instance = ManagerHub.__ManagerHub(people_manager, report_manager, class_manager, grade_manager, presence_manager, activity_manager)

    @staticmethod
    def get_hub_instance():
        return ManagerHub._hub_instance