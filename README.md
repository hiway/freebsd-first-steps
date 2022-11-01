# freebsd-first-steps

A guided tutorial and web-ui to set up your first FreeBSD server.

## What is this?

This is a guided tutorial and web-ui to set up your first FreeBSD server. It is
intended to be used by people who are new to FreeBSD and want to get a server
up and running quickly.

## How do I use it?

### Never used FreeBSD?

If you have never used FreeBSD before, you should start with installing
`freebsd-first-steps` on your local machine.
Then using the cli, you can install `freebsd-first-steps` on a remote FreeBSD server.

### Already familiar with FreeBSD?

If you are already familiar with FreeBSD, you can install `freebsd-first-steps`
on a remote FreeBSD server and use the web-ui to set up your server.

## How do I install?

```bash
git clone https://github.com/hiway/freebsd-first-steps.git
cd freebsd-first-steps

python3 -m pip install poetry
poetry install
```

## How do I use it?

### Serve the web-ui

```bash
freebsd-first-steps serve
```

### Install via SSH on remote FreeBSD server

```bash
freebsd-first-steps ssh-install --identity ~/.ssh/id_rsa user@hostname
```
