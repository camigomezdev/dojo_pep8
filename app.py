""" Main file for CodeBreaker"""
# __doc__ (Main file for little game CodeBreaker where you must guess
# the secret number)

from app.controllers.default import DefaultController

if __name__ == '__main__':
    app = DefaultController()
    app.create_app()
    app.show_credits(True)
