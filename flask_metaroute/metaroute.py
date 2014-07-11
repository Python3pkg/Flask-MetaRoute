from flask_metaroute.func import attach_controllers
import importlib
    
class MetaRoute(object):
    
    def __init__(self, app = None, ctrl_pkg = None):
        self.app = app
        if app:
            self.init_app(self.app, ctrl_pkg)

    def init_app(self, app, ctrl_pkg = None):
        pkg = ctrl_pkg or app.config['METAROUTE_CONTROLLERS_PKG']
        if isinstance(pkg, str):
            pkg = importlib.import_module(pkg)
            
        
        attach_controllers(app, pkg)
