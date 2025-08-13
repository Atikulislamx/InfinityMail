import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# Hacker-style banner
banner_text = Text()
banner_text.append(r"""
 _   _            _                __  __       _ _     
| | | | __ _  ___| | _____ _ __   |  \/  | __ _(_) |___ 
| |_| |/ _` |/ __| |/ / _ \ '__|  | |\/| |/ _` | | / __|
|  _  | (_| | (__|   <  __/ |     | |  | | (_| | | \__ \
|_| |_|\__,_|\___|_|\_\___|_|     |_|  |_|\__,_|_|_|___/
""", style="bold red")

console.print(Panel(banner_text, subtitle="HackerMail CLI v1.0", expand=False))

# CLI input
sender_name = console.input("[bold cyan]Sender Name:[/bold cyan] ")
sender_email = console.input("[bold cyan]Sender Email:[/bold cyan] ")
sender_password = console.input("[bold cyan]App Password:[/bold cyan] ")
receiver_email = console.input("[bold green]Receiver Email:[/bold green] ")
subject = console.input("[bold yellow]Email Subject:[/bold yellow] ")

console.print("[bold magenta]Enter HTML Body (type END on a new line to finish):[/bold magenta]")

lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)
body = "\n".join(lines)

# Create message
msg = MIMEMultipart()
msg['From'] = f"{sender_name} <{sender_email}>"
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'html'))

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()
    console.print(f"[bold green]Email sent successfully to {receiver_email}![/bold green]")
except Exception as e:
    console.print(f"[bold red]Failed to send email:[/bold red] {str(e)}")
