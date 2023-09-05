#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(s, n):
    """Create a copy of the string without the character at position n."""
    if 0 <= n < len(s):
        return s[:n] + s[n+1:]
    else:
        # Handle the case when n is out of range
        return s
