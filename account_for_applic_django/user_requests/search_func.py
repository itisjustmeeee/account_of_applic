def unicode_contains(value, search):
    if value is None or search is None:
        return 0

    return int(
        str(search).casefold() in str(value).casefold()
    )
