class DocumentAlreadyBorrowedException(Exception):
    """To raise when attempting to borrow a document that is already borrowed (not available)."""
    pass