from plumbum import local


def get() -> str:
    return local["hostname"]().strip()


def set(hostname: str) -> None:
    try:
        local["hostname"](hostname)
        local["sysrc"]("hostname=" + hostname)
    except Exception as e:
        raise RuntimeError(f"Failed to set hostname: {e}") from e
