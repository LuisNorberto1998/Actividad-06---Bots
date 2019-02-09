import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_signo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_signo) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_signo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_signo) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_signo, **k):

    @staticmethod
    def POST_DELETE(id_signo, **k):
    '''

    def GET(self, id_signo, **k):
        message = None # Error message
        id_signo = config.check_secure_val(str(id_signo)) # HMAC id_signo validate
        result = config.model.get_horoscopos(int(id_signo)) # search  id_signo
        result.id_signo = config.make_secure_val(str(result.id_signo)) # apply HMAC for id_signo
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_signo, **k):
        form = config.web.input() # get form data
        form['id_signo'] = config.check_secure_val(str(form['id_signo'])) # HMAC id_signo validate
        result = config.model.delete_horoscopos(form['id_signo']) # get horoscopos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_signo = config.check_secure_val(str(id_signo))  # HMAC user validate
            id_signo = config.check_secure_val(str(id_signo))  # HMAC user validate
            result = config.model.get_horoscopos(int(id_signo)) # get id_signo data
            result.id_signo = config.make_secure_val(str(result.id_signo)) # apply HMAC to id_signo
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/horoscopos') # render horoscopos delete.html 
