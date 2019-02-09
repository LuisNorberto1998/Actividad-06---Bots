import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_signo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_signo) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_signo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_signo) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_signo, **k):

    @staticmethod
    def POST_EDIT(id_signo, **k):
        
    '''

    def GET(self, id_signo, **k):
        message = None # Error message
        id_signo = config.check_secure_val(str(id_signo)) # HMAC id_signo validate
        result = config.model.get_horoscopos(int(id_signo)) # search for the id_signo
        result.id_signo = config.make_secure_val(str(result.id_signo)) # apply HMAC for id_signo
        return config.render.edit(result, message) # render horoscopos edit.html

    def POST(self, id_signo, **k):
        form = config.web.input()  # get form data
        form['id_signo'] = config.check_secure_val(str(form['id_signo'])) # HMAC id_signo validate
        # edit user with new data
        result = config.model.edit_horoscopos(
            form['id_signo'],form['nombre_signo'],form['descripcion_signo'],form['ruta_img_signo'],
        )
        if result == None: # Error on udpate data
            id_signo = config.check_secure_val(str(id_signo)) # validate HMAC id_signo
            result = config.model.get_horoscopos(int(id_signo)) # search for id_signo data
            result.id_signo = config.make_secure_val(str(result.id_signo)) # apply HMAC to id_signo
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/horoscopos') # render horoscopos index.html
