import re

def detect_context(response_text, payload):
    if payload in response_text:
        if "<script>" in response_text:
            return "js"
        if '="' in response_text:
            return "attr"
        return "html"
    return None
