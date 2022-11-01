from plumbum import local


def _search_timezone(query: str) -> list[str]:
    return local["grep"]("-i", query, "/usr/share/zoneinfo/zone.tab").strip().splitlines()


def search(query) -> list[str]:
    return [line.split("\t")[2] for line in _search_timezone(query)]


def get_system_timezone() -> str:
    return local["date"]("+%Z").strip()


def set_system_timezone(timezone: str) -> None:
    """
    cp /usr/share/zoneinfo/Asia/Kolkata /etc/localtime
    adjkerntz -a
    """
    try:
        local["cp"](f"/usr/share/zoneinfo/{timezone}", "/etc/localtime")
        local["adjkerntz"]("-a")
    except Exception as e:
        if "Operation not permitted" in str(e):
            raise RuntimeError(
                "Failed to set timezone. Please run this interactive guide as root."
            ) from e
        raise RuntimeError(f"Failed to set timezone: {e}") from e
