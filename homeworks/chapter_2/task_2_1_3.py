def debug_control(*args, **kwargs):
    return len(args)+len(kwargs)

debug_control("Hello!", 1000, 7)
