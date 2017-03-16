from watchdog.events import FileSystemEventHandler

class AuditHandler(FileSystemEventHandler):

    def on_modified(self, event):
        print("Le fichier %s a été modifié" % event.src_path)
    def on_created(self,event):
        print("Le fichier %s a été créé" % event.src_path)
    def on_deleted(self,event):
        print("Le fichier %s a été supprimé" % event.src_path)
