from abc import ABC, abstractmethod

class IPeopleManager(ABC):
    """
    
    People manager interface 
            
    Methods
    -------
    get_registration_form(model,id)
        Collects registration form for the specified model and id

    submit_registration_form(model,id)
        Submits registration form for the specified model and id

    list_people(model)
        Returns list of people that match the model parameter

    delete_person(model, id)
        Deletes person that matches specified model and id
    """

    @abstractmethod
    def get_registration_form(model, id=None):
        """
        Gets the registration form for a new or existing person
                
        Parameters
        -------
        model : str
            Specifies DB model, or other qualifier, to identify person group

        id : int
            DB primary key of person desired. Should be None in case of new person

        Returns
        -------
        form : str
            Rendered html template for the new or exiting person form
        """
        pass

    @abstractmethod
    def submit_registration_form(model, id=None):
        """
        Submits the registration form for a new or existing person. This includes
        validation of submitted data
                
        Parameters
        -------
        model : str
            Specifies DB model, or other qualifier, to identify person group

        id : int
            DB primary key of person desired. Should be None in case of new person

        Returns
        -------
        res : Response object
            If successful redirects accordingly and if failed, redirects to form page
            specifying errors
        """
        pass

    @abstractmethod
    def list_people(model):
        """
        Collects every person that matches model and displays them
                
        Parameters
        -------
        model : str
            Specifies DB model, or other qualifier, to identify person group

        Returns
        -------
        res : str
            Rendered html template showing people that match model
        """
        pass

    @abstractmethod
    def delete_person(model, id):
        """
        Deletes person that matches model and id. If no match is found, 
        returns error
                
        Parameters
        -------
        model : str
            Specifies DB model, or other qualifier, to identify person group
        
        id : int
            DB primary key of person desired

        Returns
        -------
        res : Response object
            If successful redirects accordingly and if failed, redirects to previous page
            specifying errors
        """
        pass
    
class IReportManager(ABC):
    """
    
    Report manager interface 
            
    Methods
    -------
    generate_report(report_type,**kwargs)
        Collects registration form for the specified model and id
    """

    @abstractmethod
    def generate_report(report_type, **kwargs):
        """
        Generates the specified report_type with customizable arguments.
        Returns error if report_type specified is not implemented
                
        Parameters
        -------
        report_type : str
            Report type that must be generated

        kwargs : dict
            Dictionary of customizable arguments for personalization of
            reports generated

        Returns
        -------
        report : str | Response object
            Rendered html template for the new report generated or sends file
            to be downloaded by user's browser
        """
        pass

class IClassManager(ABC):
    """
    
    Class manager interface 
            
    Methods
    -------
    get_class_form(id)
        Collects class registration form for the specified id

    submit_class_form(id)
        Submits class registration form for the specified id

    list_classes()
        Returns view for list of classes

    delete_class(id)
        Deletes class that matches specified id

    populate_class(id)
        Selects students that will be a part of the class
    """

    @abstractmethod
    def get_class_form(id=None):
        """
        Gets the registration form for a new or existing class
                
        Parameters
        -------

        id : int
            DB primary key of class desired. Should be None in case of new class

        Returns
        -------
        form : str
            Rendered html template for the new or exiting class form
        """
        pass

    @abstractmethod
    def submit_class_form(id=None):
        """
        Submits the registration form for a new or existing class. This includes
        validation of submitted data
                
        Parameters
        -------

        id : int
            DB primary key of class desired. Should be None in case of new class

        Returns
        -------
        res : Response object
            If successful redirects accordingly and if failed, redirects to form page
            specifying errors
        """
        pass

    @abstractmethod
    def list_classes():
        """
        Collects every class and displays them

        Returns
        -------
        res : str
            Rendered html template showing classes
        """
        pass

    @abstractmethod
    def delete_class(id):
        """
        Deletes class that matches id. If no match is found, 
        returns error
                
        Parameters
        -------
        
        id : int
            DB primary key of class desired

        Returns
        -------
        res : Response object
            If successful redirects accordingly and if failed, redirects to previous page
            specifying errors
        """
        pass

    @abstractmethod
    def populate_class(id):
        """
        Uses developer-defined allocation algorithm to populate a class
        with students.
                
        Parameters
        -------
        
        id : int
            DB primary key of class desired

        Returns
        -------
        res : Response object
            If successful redirects accordingly and if failed, redirects to previous page
            specifying errors
        """
        pass

class IGradeManager(ABC):
    """
    
    Grade manager interface 
            
    Methods
    -------
    get_grade_form(id)
        Collects grade registration form for the specified id

    submit_grade_form(id)
        Submits grade registration form for the specified id

    delete_grade(id)
        Deletes grade that matches specified id

    """

    @abstractmethod
    def get_grade_form(id=None):
        """
        Gets the registration form for a new or existing grade
                
        Parameters
        -------

        id : int
            DB primary key of grade desired. Should be None in case of new grade

        Returns
        -------
        form : str
            Rendered html template for the new or exiting grade form
        """
        pass

    @abstractmethod
    def submit_grade_form(id=None):
        """
        Submits the registration form for a new or existing grade. This includes
        validation of submitted data
                
        Parameters
        -------

        id : int
            DB primary key of grade desired. Should be None in case of new grade

        Returns
        -------
        res : Response object
            If successful redirects accordingly and if failed, redirects to form page
            specifying errors
        """
        pass

    @abstractmethod
    def delete_grade(id):
        """
        Deletes grade that matches id. If no match is found, 
        returns error
                
        Parameters
        -------
        
        id : int
            DB primary key of grade desired

        Returns
        -------
        res : Response object
            If successful redirects accordingly and if failed, redirects to previous page
            specifying errors
        """
        pass

class IPresenceManager(ABC):
    """
    
    Presence manager interface 
            
    Methods
    -------
    get_presence_form(id)
        Collects activity registration form for the specified id

    submit_presence_form(id)
        Submits activity registration form for the specified id
    """
    @abstractmethod
    def get_presence_form(id=None):
        """
        Gets the registration form for a new or existing presence data
                
        Parameters
        -------

        id : int
            DB primary key of presence data desired. Should be None in case of new presence registration

        Returns
        -------
        form : str
            Rendered html template for the new or exiting presence registration form
        """
        pass

    @abstractmethod
    def submit_presence_form(id=None):
        """
        Submits the registration form for a new or existing presence data. This includes
        validation of submitted data
                
        Parameters
        -------

        id : int
            DB primary key of presence data desired. Should be None in case of new presence 
            registration

        Returns
        -------
        res : Response object
            If successful redirects accordingly and if failed, redirects to form page
            specifying errors
        """
        pass

class IActivityManager(ABC):
    """
    
    Activity manager interface 
            
    Methods
    -------
    get_activity_form(id)
        Collects activity registration form for the specified id

    submit_activity_form(id)
        Submits activity registration form for the specified id

    list_activities()
        Returns view for list of activities

    delete_activity(id)
        Deletes activity that matches specified id
    """
    
    @abstractmethod
    def get_activity_form(id=None):
        """
        Gets the registration form for a new or existing activity
                
        Parameters
        -------

        id : int
            DB primary key of activity desired. Should be None in case of new activity

        Returns
        -------
        form : str
            Rendered html template for the new or exiting activity form
        """
        pass

    @abstractmethod
    def submit_activity_form(id=None):
        """
        Submits the registration form for a new or existing activity. This includes
        validation of submitted data
                
        Parameters
        -------

        id : int
            DB primary key of activity desired. Should be None in case of new activity

        Returns
        -------
        res : Response object
            If successful redirects accordingly and if failed, redirects to form page
            specifying errors
        """
        pass

    @abstractmethod
    def list_activities():
        """
        Collects every activity and displays them

        Returns
        -------
        res : str
            Rendered html template showing activities
        """
        pass

    @abstractmethod
    def delete_activity(id):
        """
        Deletes activity that matches id. If no match is found, 
        returns error
                
        Parameters
        -------
        
        id : int
            DB primary key of activity desired

        Returns
        -------
        res : Response object
            If successful redirects accordingly and if failed, redirects to previous page
            specifying errors
        """
        pass