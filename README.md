# Mobile DevOps & Ledger Suite

A lightweight Python-based client ledger and profit calculator automation pipeline, containerized with Docker and built directly on Android via Termux.

## Features

- **Deal Calculator (`calculator.py`)**: Computes gross/net margins and exports deals to `deals.csv`.
- **Client Ledger (`ledger.py`)**: Tracks account balances, exports formatted history to `ledger_history.txt`, and generates copy-paste WhatsApp reminder cards.
- **Docker Ready (`Dockerfile`)**: Standardized container configuration for deployment across cloud environments.

## Quick Start (Termux)

Run the client ledger script locally:
```bash
python ledger.py
