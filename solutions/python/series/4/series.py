def slices(series, length):
    if not series:
        raise ValueError("series cannot be empty")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    
    slicing = len(series) - length + 1
    
    return [
        series[start:start+length]
        for start in range(slicing)
    ]
