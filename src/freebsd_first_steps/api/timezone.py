from plumbum import local
from plumbum import ProcessExecutionError


def _search_timezone(query: str) -> list[str]:
    try:
        return local["grep"]("-i", query, "/usr/share/zoneinfo/zone.tab").strip().splitlines()
    except ProcessExecutionError as e:
        if e.retcode == 1:
            return []
        raise

def search(query) -> list[str]:
    results = []
    for line in _search_timezone(query):
        if line.startswith("#"):
            continue
        results.append(line.split("\t")[2])
    return results

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
        elif "are identical (not copied)." in str(e):
            raise RuntimeError("Timezone is already set to " + timezone) from e
        raise RuntimeError(f"Failed to set timezone: {e}") from e
