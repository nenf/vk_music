# -*- coding: utf-8 -*-


def utf(text):
    return text.encode("utf-8")


def uformat(text):
    return utf(text[:40].rstrip())
