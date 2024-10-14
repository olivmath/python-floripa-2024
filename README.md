# Introduction to Blockchain with Python

- A simple sample of how to works a vyper lang with ape frameworks

## Quickstart Guide

### 1. Setup environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

**Install Ape Worx**

```bash
pip3 install eth-ape
pip3 install ape-vyper
```

**Install local blockchain**

```bash
# We will use `anvil` from foundry framework
curl -L https://foundry.paradigm.xyz | bash
```

### 3. Compile Smartcontracts

```bash
ape compile
```

### 4. Running Local Blockchain (Anvil Network)

```bash
# open new terminal windown
anvil
```

### 5. Create your Test Wallet

> [!CAUTION]
> tip dont use this with mainnet assets

```bash
# past this test private key: 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
ape accounts import my_wallet
```

### 5. Deploy Smartcontracts (on Anvil Network)

```bash
ape run deploy --network ethereum:anvil:node
```

### 6. Interacte with Smartcontract

```python
# for interacte with smartcontract you need open console
ape console --network ethereum:anvil:node

# ape console is Python REPL
from ape import project, accounts

owner = accounts.load("my_wallet")

# import the smartcontract has deployed
flipper = project.Flipper.at("0x5FbDB2315678afecb367f032d93F642f64180aa3")

# read data from blockchain
flipper.get()

# write data into blockchain
flipper.flip(sender=owner)

# read data from blockchain again
flipper.get()
```
