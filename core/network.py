import socket


def get_local_addresses():
    addresses = set()

    hostname = socket.gethostname()

    for address in socket.getaddrinfo(hostname, None):
        ip = address[4][0]
        addresses.add(ip)

    return addresses