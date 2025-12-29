class DocumentNotBorrowedException(Exception):
    """To raise when attempting to return a document that has not yet been borrowed."""
    pass