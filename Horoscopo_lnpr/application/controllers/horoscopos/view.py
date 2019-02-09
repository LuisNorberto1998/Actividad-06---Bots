import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, id_signo):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_signo) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_signo):
    '''

    def GET(self, id_signo):
        id_signo = config.check_secure_val(str(id_signo)) # HMAC id_signo validate
        result = config.model.get_horoscopos(id_signo) # search for the id_signo data
        return config.render.view(result) # render view.html with id_signo data
