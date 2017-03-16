"""Exemple de gestionnaire d'évènements."""

from watchdog.events import FileSystemEventHandler


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
