.. _email-tutorial:

``email``
=========

Par Karim Gehrig [#KG]_

Introduction
------------

Les mails sont la base de communication et d'alert à ce jour,

les mail se découpe en deux partie, ``envoie`` et ``réception``

Nous allons voir des exemple de code simple, et divers astuce afin de comprendre
le principe de base.


SMTP
====
Pour l'envoie de mail (DOCSMTP_)
l'envoir est plus courrent que la réception pour un script.

Par exemple si on veur etre averti d'un acces sur un serveur ou encore une alert
d'un fichier log ou autres.

Voici un exemple de code utilisant la gestion de l'HTML dans les messages

.. note:: C'est bien si on utilise de l'html de également mettre le texte en plain text, afin de support pour
les programme qui ne gérerai pas ou ont le html de désactivé.



On commence par importer ``import smtplib``

.. code:: python3 
    :number-lines:

    import smtplib
    import os
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    me = "<ADRESSE MAIL EXPEITEUR>"
    you = "<ADRESSE MAIL DESTINATAIRE>"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "<SUJET>"
    msg['From'] = "<NAME> <"+me+">"
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "<VOTRE TEXT>"
    html = """\
    <html>
    <head></head>
    <body>
        <VOTRE CODE HTML>
    </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.

    msg.attach(part1)
    msg.attach(part2)

    # Send the message via SMTP server.
    s = smtplib.SMTP()
    s.connect('<SERVEUR SMTP>:<PORT>')
    s.login(me,'<MOT DE PASSE SERVEUR SMTP>')
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, you, msg.as_string())
    s.quit()



Changer ce qu'il y a dans les ``<>`` avec vos informations

Ce code simple permet d'envoyer un mail avec uun serveur relai SMTP en mode html et plain/text


IMAP
====
Pour la réception de mail (DOCIMAP_)


.. code:: python3 
    :number-lines:

    import imaplib
    M = imaplib.IMAP4("<SERVEUR SMTP>")
    M.login("<login>", "<MOT DE PASSE>")
    M.select()
    typ, data = M.search(None, 'ALL')

    data_idx=data[0].split()

    num=data_idx[-1];

    typ, data = M.fetch(num, '(RFC822)')
    #print('Message %s\n%s\n' % (num, data[0][1]))
    print (data[0][1].decode("utf-8"))
    M.close()
    M.logout()
    

Changer ce qu'il y a dans les ``<>`` avec vos informations

Ce code simple récupère le dernier mail sur le serveur et affiche la source
du message décodé en UTF8


Conclusion
----------

.. [#KG] <karim.gehrig@he-arc.ch>

.. _DOCIMAP: https://docs.python.org/3/library/imaplib.html
.. _DOCSMTP: https://docs.python.org/3/library/smtplib.html
