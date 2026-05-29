<p align="center">
  <img src="./assets/banner.svg" alt="Jhonatan Viana — Infraestrutura · Automação · Sistemas resilientes" width="100%"/>
</p>

<p align="center">
  <a href="https://jhou.tech"><img alt="jhou.tech" src="https://img.shields.io/badge/-jhou.tech-0c1018?style=flat-square&logo=cloudflare&logoColor=bae6fd&labelColor=07090f"/></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/jhonatanviana/"><img alt="LinkedIn" src="https://img.shields.io/badge/-linkedin-0c1018?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0yMC40NSAyMC40NWgtMy41NlYxNC45YzAtMS4zMi0uMDMtMy4wMi0xLjg0LTMuMDItMS44NCAwLTIuMTMgMS40NC0yLjEzIDIuOTN2NS42NUg5LjM2VjloMy40MnYxLjU2aC4wNWEzLjc1IDMuNzUgMCAwMTMuMzctMS44NWMzLjYgMCA0LjI3IDIuMzcgNC4yNyA1LjQ2ek01LjM0IDcuNDNhMi4wNiAyLjA2IDAgMTEwLTQuMTIgMi4wNiAyLjA2IDAgMDEwIDQuMTJ6bTEuNzggMTMuMDJIMy41NlY5aDMuNTZ6TTIyLjIyIDBIMS43N0MuOCAwIDAgLjc3IDAgMS43M3YyMC41NEMwIDIzLjIzLjggMjQgMS43NyAyNGgyMC40NWMuOTggMCAxLjc4LS43NyAxLjc4LTEuNzNWMS43M0MyNCAuNzcgMjMuMiAwIDIyLjIyIDB6Ii8%2BPC9zdmc%2B&logoColor=bae6fd&labelColor=07090f"/></a>
  &nbsp;
  <a href="mailto:jhou@jhou.tech"><img alt="Email" src="https://img.shields.io/badge/-jhou%40jhou.tech-0c1018?style=flat-square&logo=maildotru&logoColor=bae6fd&labelColor=07090f"/></a>
  &nbsp;
  <a href="https://www.instagram.com/jhonatan_viana/"><img alt="Instagram" src="https://img.shields.io/badge/-instagram-0c1018?style=flat-square&logo=instagram&logoColor=bae6fd&labelColor=07090f"/></a>
</p>

<br/>

<table>
<tr><td>

```bash
$ ls -la ~/

drwxr-xr-x   sobre/         # quem é
drwxr-xr-x   laboratorio/   # o que construí
drwxr-xr-x   stack/         # ferramentas
-rw-r--r--   now.log        # no que estou agora
```

</td></tr>
</table>

<br/>

<h3 id="sobre">&nbsp;<code>~/sobre</code></h3>

Especialista em Soluções de TI na **Pense Rede** (Cariacica, ES). Trabalho no ponto em que infraestrutura encontra produto — desde a operação que sustenta o sistema até a decisão técnica que define o roadmap.

Meu jeito de aprender é construindo: monto, quebro, reconstruo, documento. Cada projeto vira um laboratório.

<br/>

<h3 id="laboratorio">&nbsp;<code>~/laboratorio</code></h3>

<table>
  <tr>
    <td width="220" valign="top">
      <h3>&nbsp;🟢 &nbsp;Jhou TBC</h3>
      <sub>&nbsp;<a href="https://play.jhou.tech">play.jhou.tech</a></sub>
      <br/><br/>
      <sub>&nbsp;<b>LIVE SINCE</b><br/>&nbsp;May 2026</sub>
      <br/><br/>
      <sub>&nbsp;<b>OPERAÇÃO</b><br/>&nbsp;Solo · bare-metal</sub>
      <br/><br/>
      <sub>&nbsp;<b>STATUS</b><br/>&nbsp;Produção pública</sub>
    </td>
    <td valign="top">
      <p>
        Servidor privado de <b>WoW The Burning Crusade 2.4.3</b> em produção pública.
        Realm completo construído e mantido sozinho — do core em C++ ao painel web,
        passando por DB, observabilidade e exposição segura.
      </p>
      <p>
        <b>Stack &nbsp;·&nbsp;</b>
        <code>Ubuntu&nbsp;24.04</code> &nbsp;
        <code>cMaNGOS-TBC (C++)</code> &nbsp;
        <code>MariaDB</code> &nbsp;
        <code>Flask&nbsp;+&nbsp;gunicorn</code> &nbsp;
        <code>nginx</code> &nbsp;
        <code>Cloudflare&nbsp;Tunnel</code> &nbsp;
        <code>netdata</code>
      </p>
      <p>
        <b>Engenharia &nbsp;·&nbsp;</b>
        patches custom no core &nbsp;·&nbsp;
        SQL versionado &nbsp;·&nbsp;
        backups off-site automatizados &nbsp;·&nbsp;
        hardening anti-DDoS (UFW&nbsp;+&nbsp;sysctl) &nbsp;·&nbsp;
        runbook próprio &nbsp;·&nbsp;
        changelog bilíngue (PT/EN)
      </p>
      <p>
        <sub><i>Single-server private WoW TBC realm — live since May 2026. Solo ops: bare-metal Linux, C++ core, custom patches, hardened public exposure.</i></sub>
      </p>
    </td>
  </tr>
</table>

<details>
  <summary>&nbsp;<sub><b>📐 &nbsp; SERVICE MAP COMPLETO &nbsp; ·  &nbsp; abrir</b></sub></summary>
  <br/>
  <table>
    <thead>
      <tr>
        <th align="left"><sub>CAMADA</sub></th>
        <th align="left"><sub>COMPONENTE</sub></th>
        <th align="left"><sub>FUNÇÃO</sub></th>
      </tr>
    </thead>
    <tbody>
      <tr><td><sub><b>EDGE</b></sub></td><td><code>Cloudflare&nbsp;Tunnel</code></td><td><sub>publicação HTTPS sem porta exposta</sub></td></tr>
      <tr><td><sub><b>EDGE</b></sub></td><td><code>nginx</code></td><td><sub>roteamento play / jhou / monitor</sub></td></tr>
      <tr><td><sub><b>APP</b></sub></td><td><code>Flask&nbsp;+&nbsp;gunicorn (1w/8t)</code></td><td><sub>painel do jogador, registro double-opt-in, votos, LGPD</sub></td></tr>
      <tr><td><sub><b>APP</b></sub></td><td><code>cMaNGOS-TBC&nbsp;(C++)</code></td><td><sub>core do jogo · patch consolidado próprio</sub></td></tr>
      <tr><td><sub><b>DADOS</b></sub></td><td><code>MariaDB&nbsp;10.11</code></td><td><sub>realmd · characters · mangos · logs</sub></td></tr>
      <tr><td><sub><b>OBS</b></sub></td><td><code>netdata</code></td><td><sub>cpu / mem / disco / rede em tempo real</sub></td></tr>
      <tr><td><sub><b>SEC</b></sub></td><td><code>UFW&nbsp;+&nbsp;sysctl&nbsp;+&nbsp;fail2ban</code></td><td><sub>connlimit · SYN flood guard · brute-force</sub></td></tr>
      <tr><td><sub><b>BACKUP</b></sub></td><td><code>backup-db.sh&nbsp;+&nbsp;repo privado</code></td><td><sub>dump diário rotativo · off-site automático</sub></td></tr>
      <tr><td><sub><b>BOOT</b></sub></td><td><code>systemd&nbsp;+&nbsp;tmux&nbsp;+&nbsp;screen</code></td><td><sub>serviços managed · jogo em screen dentro do tmux</sub></td></tr>
      <tr><td><sub><b>DEPLOY</b></sub></td><td><code>git&nbsp;+&nbsp;Makefiles&nbsp;+&nbsp;scripts</code></td><td><sub>SQL numerada · patches versionados · runbook próprio</sub></td></tr>
    </tbody>
  </table>
  <p><sub>&nbsp;Tudo opera em bare-metal num único notebook Dell (Intel i5-4200U · 7.7 GB RAM · Ubuntu 24.04 LTS).</sub></p>
</details>

<br/>

<h3 id="stack">&nbsp;<code>~/stack</code></h3>

<table>
  <tr>
    <td align="right" valign="middle" width="170"><sub><b>OPERAÇÃO &amp; INFRA</b></sub></td>
    <td>
      <img alt="Linux" src="https://img.shields.io/badge/-Linux-0c1018?style=flat-square&logo=linux&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="Ubuntu Server" src="https://img.shields.io/badge/-Ubuntu_Server-0c1018?style=flat-square&logo=ubuntu&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="nginx" src="https://img.shields.io/badge/-nginx-0c1018?style=flat-square&logo=nginx&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="systemd" src="https://img.shields.io/badge/-systemd-0c1018?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xOS40IDEzYTcuNSA3LjUgMCAwMDAtMmwyLTEuNi0yLTMuNS0yLjQgMWE3LjQgNy40IDAgMDAtMS43LTFMMTUgMy41aC00bC0uMyAyLjRhNy40IDcuNCAwIDAwLTEuNyAxbC0yLjQtMS0yIDMuNUw0LjYgMTFhNy41IDcuNSAwIDAwMCAybC0yIDEuNiAyIDMuNSAyLjQtMWMuNS40IDEuMS44IDEuNyAxbC4zIDIuNGg0bC4zLTIuNGE3LjQgNy40IDAgMDAxLjctMWwyLjQgMSAyLTMuNXpNMTIgMTUuNWEzLjUgMy41IDAgMTEwLTcgMy41IDMuNSAwIDAxMCA3eiIvPjwvc3ZnPg%3D%3D&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="tmux" src="https://img.shields.io/badge/-tmux-0c1018?style=flat-square&logo=tmux&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="Cloudflare" src="https://img.shields.io/badge/-Cloudflare-0c1018?style=flat-square&logo=cloudflare&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="Netdata" src="https://img.shields.io/badge/-Netdata-0c1018?style=flat-square&logo=netdata&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="fail2ban" src="https://img.shields.io/badge/-fail2ban-0c1018?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyLjQiLz48bGluZSB4MT0iNS42IiB5MT0iNS42IiB4Mj0iMTguNCIgeTI9IjE4LjQiIHN0cm9rZT0id2hpdGUiIHN0cm9rZS13aWR0aD0iMi40IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz48L3N2Zz4%3D&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="UFW" src="https://img.shields.io/badge/-UFW-0c1018?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0yIDRoNnY0SDJ6TTkgNGg2djRIOXpNMTYgNGg2djRoLTZ6TTIgOWgzdjRIMnpNNiA5aDZ2NEg2ek0xMyA5aDZ2NGgtNnpNMjAgOWgydjRoLTJ6TTIgMTRoNnY0SDJ6TTkgMTRoNnY0SDl6TTE2IDE0aDZ2NGgtNnpNMiAxOWgzdjNIMnpNNiAxOWg2djNINnpNMTMgMTloNnYzaC02ek0yMCAxOWgydjNoLTJ6Ii8%2BPC9zdmc%2B&logoColor=bae6fd&labelColor=07090f"/>
    </td>
  </tr>
  <tr>
    <td align="right" valign="middle"><sub><b>BACKEND &amp; DADOS</b></sub></td>
    <td>
      <img alt="Python" src="https://img.shields.io/badge/-Python-0c1018?style=flat-square&logo=python&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="Flask" src="https://img.shields.io/badge/-Flask-0c1018?style=flat-square&logo=flask&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="gunicorn" src="https://img.shields.io/badge/-gunicorn-0c1018?style=flat-square&logo=gunicorn&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="MariaDB" src="https://img.shields.io/badge/-MariaDB-0c1018?style=flat-square&logo=mariadb&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="C++" src="https://img.shields.io/badge/-C%2B%2B-0c1018?style=flat-square&logo=cplusplus&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="Bash" src="https://img.shields.io/badge/-Bash-0c1018?style=flat-square&logo=gnubash&logoColor=bae6fd&labelColor=07090f"/>
    </td>
  </tr>
  <tr>
    <td align="right" valign="middle"><sub><b>WEB</b></sub></td>
    <td>
      <img alt="HTML5" src="https://img.shields.io/badge/-HTML5-0c1018?style=flat-square&logo=html5&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="CSS3" src="https://img.shields.io/badge/-CSS3-0c1018?style=flat-square&logo=css&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="JavaScript" src="https://img.shields.io/badge/-JavaScript-0c1018?style=flat-square&logo=javascript&logoColor=bae6fd&labelColor=07090f"/>
    </td>
  </tr>
  <tr>
    <td align="right" valign="middle"><sub><b>WORKFLOW</b></sub></td>
    <td>
      <img alt="Git" src="https://img.shields.io/badge/-Git-0c1018?style=flat-square&logo=git&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="GitHub" src="https://img.shields.io/badge/-GitHub-0c1018?style=flat-square&logo=github&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="Docker" src="https://img.shields.io/badge/-Docker-0c1018?style=flat-square&logo=docker&logoColor=bae6fd&labelColor=07090f"/>
      <img alt="GNU Make" src="https://img.shields.io/badge/-GNU_Make-0c1018?style=flat-square&logo=gnu&logoColor=bae6fd&labelColor=07090f"/>
    </td>
  </tr>
</table>

<p align="center">
  <img alt="Top languages — code distribution: jhou tbc + public repos" src="./assets/top-langs.svg" width="60%"/>
</p>

<br/>

<h3 id="now">&nbsp;<code>~/now</code></h3>

<table>
<tr><td>

```log
$ tail -1 ~/now.log
[2026-05-29]  refatorando JS inline dos templates do painel para arquivos externos
              e removendo 'unsafe-inline' do script-src no CSP. próximo na fila:
              CSRF per-user (destrava multi-worker no gunicorn).
```

</td></tr>
</table>

<br/>

<p align="center">
  <sub><code>~$ uptime &nbsp;—&nbsp; sistemas em pé desde que aprendi a derrubá-los com cuidado.</code></sub>
</p>

<p align="center">
  <sub><code>// jhou.tech &nbsp;·&nbsp; cariacica → internet &nbsp;·&nbsp; v.2026.05</code></sub>
</p>
