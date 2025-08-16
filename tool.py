import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import random

console = Console()

# List of banners with corresponding subtitles
banners_with_subtitles = [
    {
        "banner": r"""
███████╗███╗   ██╗███████╗███████╗███╗   ██╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝████╗  ██║██╔════╝██╔════╝████╗  ██║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
█████╗  ██╔██╗ ██║█████╗  █████╗  ██╔██╗ ██║███████║   ██║   ██║██║   ██║██╔██╗ ██║
██╔══╝  ██║╚██╗██║██╔══╝  ██╔══╝  ██║╚██╗██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
███████╗██║ ╚████║███████╗███████╗██║ ╚████║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
""",
        "subtitle": "By Atikul Islam Rabbi | Cyber Infinity"
    },
    {
        "banner": r"""
░█▀▀▀ ░█▀▀▀█ ░█▀▀█ ░█▀▀█ ░█▀▀▀█ ▀▀█▀▀ ░█▀▀█ 
░█▀▀▀ ░█──░█ ░█▀▀▄ ░█─── ░█──░█ ─░█── ░█▄▄▀ 
░█▄▄▄ ░█▄▄▄█ ░█▄▄█ ░█▄▄█ ░█▄▄▄█ ─░█── ░█─░█
""",
        "subtitle": "Developed by Atikul Islam Rabbi"
    },
    {
        "banner": r"""
╔═╗╔═╗╦  ╦╔═╗╔═╗╔═╗
║  ║ ║║  ║╠═╝║ ║║ ╦
╚═╝╚═╝╩═╝╩╩  ╚═╝╚═╝
""",
        "subtitle": "Cyber Infinity Presents: GhostMail"
    },
    {
        "banner": r"""
█████╗ ██╗      ██████╗ ██╗   ██╗███████╗
██╔══██╗██║     ██╔═══██╗██║   ██║██╔════╝
███████║██║     ██║   ██║██║   ██║█████╗  
██╔══██║██║     ██║   ██║╚██╗ ██╔╝██╔══╝  
██║  ██║███████╗╚██████╔╝ ╚████╔╝ ███████╗
╚═╝  ╚═╝╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝
""",
        "subtitle": "Encrypted Mailer | Atikul Islam Rabbi"
    },
    {
        "banner": r"""
██╗  ██╗ █████╗ ██████╗ ██╗███╗   ██╗ ██████╗ 
██║  ██║██╔══██╗██╔══██╗██║████╗  ██║██╔═══██╗
███████║███████║██████╔╝██║██╔██╗ ██║██║   ██║
██╔══██║██╔══██║██╔═══╝ ██║██║╚██╗██║██║   ██║
██║  ██║██║  ██║██║     ██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝
""",
        "subtitle": "Phantom Mail by Cyber Infinity"
    }
]

# Function to apply glitch effect
def glitch_banner(banner_text, glitch_prob=0.08):
    glitch_chars = ['░','▒','▓','█','≈','≡','•','∎','☣','☠','✦','✪','✶','⨀']
    glitched_lines = []
    for line in banner_text.splitlines():
        new_line = ""
        for char in line:
            if char != " " and random.random() < glitch_prob:
                new_line += random.choice(glitch_chars)
            else:
                new_line += char
        glitched_lines.append(new_line)
    return "\n".join(glitched_lines)

# Select a random banner
selected = random.choice(banners_with_subtitles)
glitched_banner_text = Text(glitch_banner(selected["banner"]), style="bold red")
subtitle_text = Text(selected["subtitle"], style="bold bright_cyan")

# Display banner panel
console.print(Panel(glitched_banner_text, subtitle=subtitle_text, expand=False, border_style="bright_magenta"))

# -------------------
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

# Create MIME message
msg = MIMEMultipart()
msg['From'] = f"{sender_name} <{sender_email}>"
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'html'))

# Send email via Gmail SMTP
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()
    console.print(f"[bold green]Email sent successfully to {receiver_email}![/bold green]")
    console.print("[bold cyan]Note:[/bold cyan] Inbox may override sender name depending on email client settings.")
except Exception as e:
    console.print(f"[bold red]Failed to send email:[/bold red] {str(e)}")
