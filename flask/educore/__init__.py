from flask import Flask
from .manager_hub import ManagerHub

def configure_educore(app, people_manager=None, report_manager=None, class_manager=None, grade_manager=None, presence_manager=None, activity_manager=None):
    """
        This method is responsible for passing the adequate implementations of the
        listed interfaces to the ManagerHub class. It also registers the routes that
        are going to be answered by the framework

        Parameters
        ----------
        app : Application Object
            This is the application object created when using Flask's constructor
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

        Returns
        ----------
        app : Application Object
            Same application object passed as a parameter with the framework routes
            added to it.
    """

    ManagerHub.configure_hub_instance(people_manager, report_manager)

    from .people import people as people_blueprint
    app.register_blueprint(people_blueprint)

    from .report import report as report_blueprint
    app.register_blueprint(report_blueprint)

    return app