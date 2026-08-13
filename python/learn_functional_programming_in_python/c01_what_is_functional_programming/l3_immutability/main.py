#!/usr/bin/env python3


def add_prefix(document: str, documents: tuple[str, ...]) -> tuple[str, ...]:
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    documents.append(new_doc)
    return documents
