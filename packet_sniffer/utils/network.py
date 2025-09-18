def is_port_well_known(port: int) -> bool:
    """
    Checks whether the given port is in the well-known range 0 - 1023
    """
    return 0 <= port <= 1023
