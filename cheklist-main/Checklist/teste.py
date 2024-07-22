import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

# Exemplo de dicionário

def enviar_emaail(dados,usuario,pdf_buffer):


    df = pd.DataFrame(dados)

    # Converte o DataFrame em uma tabela HTML
    tabela_html = df.to_html(index=False)

    # Configurações do email
    sender_email = "juanpablozonho@gmail.com"
    receiver_email = "juanpablozonho@gmail.com"
    password = "pkfc drmv pghk dvuc"

    # Cria a mensagem do email
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Tabela de Dados"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Cria a parte HTML do email
    html = f"""
    <html>
    <body>
        <p>Usuário: {usuario}<br>
        Aqui está a tabela de dados:<br>
        </p>
        {tabela_html}
    </body>
    </html>
    """

    # Anexa a parte HTML ao email
    part = MIMEText(html, "html")
    msg.attach(part)
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(pdf_buffer.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="relatorio.pdf"')
    msg.attach(part)
    # Envia o email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
def enviar_emaail2(dados,usuario,pdf_buffer):


    df = pd.DataFrame(dados)

    # Converte o DataFrame em uma tabela HTML
    tabela_html = df.to_html(index=False)

    # Configurações do email
    sender_email = "juanpablozonho@gmail.com"
    receiver_email = "Jonatan.lima@thule.com"
    password = "pkfc drmv pghk dvuc"

    # Cria a mensagem do email
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Tabela de Dados"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Cria a parte HTML do email
    html = f"""
    <html>
    <body>
        <p>Usuário: {usuario}<br>
        Aqui está a tabela de dados:<br>
        </p>
        {tabela_html}
    </body>
    </html>
    """

    # Anexa a parte HTML ao email
    part = MIMEText(html, "html")
    msg.attach(part)
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(pdf_buffer.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="relatorio.pdf"')
    msg.attach(part)
    # Envia o email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())



