def create_search_string(v: str) -> str:
    return f'%{"%%".join(v.split())}%'
