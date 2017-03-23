"""Classes d'exemple d'utilisation pour watchdog."""

from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler


class AuditHandler(FileSystemEventHandler):
    """Gestion d'audit."""

    def on_modified(self, event):
        """Un fichier a été modifié."""
        print("Le fichier %s a été modifié" % event.src_path)

    def on_created(self, event):
        """Un fichier a été créé."""
        print("Le fichier %s a été créé" % event.src_path)

    def on_deleted(self, event):
        """Un fichier a été supprimé."""
        print("Le fichier %s a été supprimé" % event.src_path)

class AuditHandlerMusic(PatternMatchingEventHandler):

    def on_modified(self, event):
        print("Le fichier %s a été modifié" % event.src_path)
    def on_created(self,event):
        print("Le fichier %s a été créé" % event.src_path)
    def on_deleted(self,event):
        print("Le fichier %s a été supprimé" % event.src_path)
