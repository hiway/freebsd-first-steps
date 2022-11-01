from plumbum import local


def get() -> str:
    return local["hostname"]().strip()


def set(hostname: str) -> None:
    try:
        local["hostname"](hostname)
        local["sysrc"]("hostname=" + hostname)
    except Exception as e:
        if "Operation not permitted" in str(e):
            raise RuntimeError(
                "Failed to set hostname. Please run this interactive guide as root."
            ) from e
        raise RuntimeError(f"Failed to set hostname: {e}") from e
