def parse_args(arr):
    result = {}
    i = 0

    while i < len(arr):
        key = arr[i].replace("--", "")
        value = arr[i + 1]
        result[key] = value
        i += 2

    return result