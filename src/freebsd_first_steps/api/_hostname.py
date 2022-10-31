from plumbum import local


def hostname() -> str:
    return local["hostname"]().strip()


def set_hostname(hostname: str) -> None:
    try:
        local["hostname"](hostname)
        local["sysrc"]("hostname=" + hostname)
    except Exception as e:
        raise RuntimeError(f"Failed to set hostname: {e}") from e
