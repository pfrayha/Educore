Educore v0.0.1
=======

This framework works utilizing the _Flask_ environment to offer a streamlined approach to developing management systems.

The framework itself is implemented inside _flask/educore_ and the _flask/app_ folder hosts the code for the prototype example. The _flask/migrations_ folder works with the _manage.py_ module to handle database modelling and migrations used for the prototype.

Given this initial stage of development, _Educore_ is yet to be made available through _pip_ to be used externally.

---

Configuration
------

The configuration of the framework requires two main phases. The first is the implementation of the manager interfaces that will be used by the developer to construct the necessary code hot spots. All manager interfaces are documented fully in the file _flask/educore/manager\_interfaces.py_. To import any manager interface to be implemented, you must use the statement 

    from educore.manager_interfaces import IPeopleManager, IReportManager

The second step for configuration of the framework happens during the inicialization phase of the application itself. At some point during the creation of app, the developer must run the function _configure\_educore_ which is imported using the statement

    from educore import configure_educore

After importing the function, every implementation of the manager interfaces must also be imported and passed, alongside the app variable itself, to the _configure\_educore_ function. It is important to note that the app variable passed is **NOT** modified and the return value of the function **MUST** overwrite the app variable.

After both these steps have been executed, the framework is now configured.

---

Reserved route names
-----------

The following route prefixes **CANNOT** be used by the developer without risking naming collisions.
* /people/*
* /reports/*
* /classes/*
* /grades/*
* /presences/*
* /activities/*

Routes with these prefixes are reserved to be served by the framework. Any other route prefixes are fine to use.