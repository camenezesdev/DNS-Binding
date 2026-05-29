## DNS Rebinding Laboratory & Proof of Concept (PoC)

[!["Language: PT-BR/EN"](https://img.shields.io/badge/Language-PT--BR%20%2F%20EN-blue.svg)](#)
[!["License: MIT"](https://img.shields.io/badge/License-MIT-green.svg)](#)

Este repositório contém a documentação completa e os scripts operacionais utilizados para validar um ataque de **DNS Rebinding** num ambiente de laboratório controlado. O objetivo desta PoC é demonstrar como a manipulação dinâmica de zonas DNS e tempos de vida (TTL) curtos pode ser explorada para contornar a *Same-Origin Policy* (SOP) e os mecanismos de *Private Network Access* (PNA) de navegadores modernos.

This repository contains the full documentation and operational scripts used to validate a **DNS Rebinding** attack in a controlled sandbox environment. The goal of this PoC is to demonstrate how dynamic DNS zone manipulation and short TTL records can be exploited to bypass the *Same-Origin Policy* (SOP) and *Private Network Access* (PNA) mechanisms in modern browsers.

---

## Estrutura do Repositório / Repository Structure

* `dns_server.py`: Servidor DNS customizado (UDP/53) com lógica de gatilho alternado (DNS Blindado). / Custom stateful DNS Server with split-horizon behavior.
* `alvo.py`: API interna emulada (Python HTTP) que expõe dados locais confidenciais. / Internal Python HTTP API exposing sensitive local data.
* `index.html`: Payload malicioso assíncrono utilizado para ler e exfiltrar a flag. / Asynchronous malicious web payload used to read and exfiltrate the key.
* `Write-Up_PT.md`: Relatório técnico e documentação detalhada passo a passo em Português.
* `Write-Up_EN.md`: Full step-by-step technical write-up and diagnostics in English.

---

## Como Executar o Laboratório / Quick Start Guide

> **Aviso:** Este laboratório foi desenvolvido estritamente para fins educacionais e de auditoria de segurança (Blue Team/Hardening). 
> **Warning:** This environment was developed strictly for educational and defensive security auditing purposes.

Para instruções detalhadas de configuração de interfaces, mitigação de ruído de rede corporativa e alinhamento de portas simétricas, consulte os ficheiros de Write-Up dedicados.

For detailed instructions on interface metrics configuration, system noise mitigation, and symmetric port alignment, please refer to the dedicated Write-Up files.

---

## Megabytez CyberSec Labs

Este projeto faz parte do meu ecossistema de segurança e portefólio profissional. Para consultar o meu currículo, visite o meu domínio oficial:

This project is part of my secure ecosystem and professional portfolio. To check my CV, please visit my official domain:

🔗 **[megabytez.pt](https://megabytez.pt)**

---
Developed by **Carlos Alexandre Menezes** | Version 1.4 | Confidentiality: Academic & Professional Use.
