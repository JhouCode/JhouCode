#!/usr/bin/env python3
"""
Lembrete de frescor do bloco ~/now do README do perfil (JhouCode/JhouCode).

Lê a data [YYYY-MM-DD] do bloco ~/now no README. Se passar de THRESHOLD_DAYS
(default 21), manda um email de cutucada via SMTP Zoho (creds em .env_wow).
Idempotente e silencioso enquanto fresco — só fala quando vence.

Uso:
  ./check-now-freshness.py            # checa e, se vencido, envia email
  ./check-now-freshness.py --dry-run  # só reporta, nunca envia
  THRESHOLD_DAYS=14 ./check-now-freshness.py

Pensado pra rodar em cron semanal (ver instalacao no fim deste arquivo).
"""
import os, re, sys, smtplib, datetime
from email.mime.text import MIMEText

SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
README       = os.path.join(SCRIPT_DIR, '..', 'README.md')
ENV_FILE     = '/home/mangos/.env_wow'
DEST         = 'jhonatan.pgd@gmail.com'
THRESHOLD    = int(os.environ.get('THRESHOLD_DAYS', '21'))
DRY_RUN      = '--dry-run' in sys.argv


def load_env(path):
    env = {}
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                k, v = line.split('=', 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    except FileNotFoundError:
        pass
    return env


def now_date_from_readme(path):
    """Pega a 1a data [YYYY-MM-DD] depois do header ~/now."""
    with open(path, encoding='utf-8') as f:
        txt = f.read()
    anchor = txt.find('~/now')
    scope = txt[anchor:] if anchor != -1 else txt
    m = re.search(r'\[(20\d\d-\d\d-\d\d)\]', scope)
    if not m:
        return None, None
    raw = m.group(1)
    return raw, datetime.date.fromisoformat(raw)


def send_email(env, days, raw, snippet):
    host = env.get('EMAIL_HOST', 'smtp.zoho.com')
    port = int(env.get('EMAIL_PORT', '587'))
    user = env.get('EMAIL_USER')
    pwd  = env.get('EMAIL_PASS')
    sender = (env.get('EMAIL_FROM') or f'Jhou <{user}>').strip('"').strip("'")
    if not (user and pwd):
        print('ERRO: credenciais SMTP ausentes em .env_wow', file=sys.stderr)
        return 1

    body = f"""\
Teu bloco ~/now do perfil GitHub (github.com/JhouCode) está com {days} dias.

Última entrada [{raw}]:
  {snippet}

Um "now" velho passa a impressão inversa (abandono). Atualiza a linha em:
  /home/mangos/github/JhouCode/README.md  (seção ~/now)
e dá um: git -C /home/mangos/github/JhouCode commit -am "now: ..." && git push

— lembrete automático (limite: {THRESHOLD} dias)
"""
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = f'🕓 ~/now do perfil está com {days} dias — atualiza?'
    msg['From'] = sender
    msg['To'] = DEST
    with smtplib.SMTP(host, port, timeout=20) as s:
        s.starttls()
        s.login(user, pwd)
        s.sendmail(user, [DEST], msg.as_string())
    return 0


def main():
    raw, d = now_date_from_readme(README)
    if d is None:
        print('AVISO: não achei data [YYYY-MM-DD] no bloco ~/now', file=sys.stderr)
        return 0
    days = (datetime.date.today() - d).days
    snippet = ''
    with open(README, encoding='utf-8') as f:
        for line in f:
            if raw in line:
                snippet = line.strip()
                break

    if days <= THRESHOLD:
        print(f'OK: ~/now com {days} dias (limite {THRESHOLD}). Nada a fazer.')
        return 0

    print(f'VENCIDO: ~/now com {days} dias (limite {THRESHOLD}).')
    if DRY_RUN:
        print('[dry-run] email NÃO enviado.')
        return 0
    rc = send_email(load_env(ENV_FILE), days, raw, snippet)
    print('Email enviado.' if rc == 0 else 'Falha ao enviar email.')
    return rc


if __name__ == '__main__':
    sys.exit(main())

# Instalação do cron (segunda, 09:00):
#   ( crontab -l 2>/dev/null; echo '0 9 * * 1 /usr/bin/python3 /home/mangos/github/JhouCode/scripts/check-now-freshness.py >> /home/mangos/github/JhouCode/scripts/now-freshness.log 2>&1' ) | crontab -
