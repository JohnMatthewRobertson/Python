'''
    from the application folder load __init__.py
    and import the fuction create_application_instance
'''
from application import create_application_instance

# creates an instance of the flask application
application_instance = create_application_instance()
