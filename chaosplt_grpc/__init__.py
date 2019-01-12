from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager

import grpc
from grpc import Channel, Server

__all__ = ["remote_channel", "create_grpc_server", "start_grpc_server",
           "stop_grpc_server"]
__version__ = '0.1.1'


@contextmanager
def remote_channel(addr: str) -> Channel:
    """
    Open a channel to the remote gRPC server at the given ̀`addr`.

    The channel is closed automatically when the context manager exits.
    """
    try:
        channel = grpc.insecure_channel(addr)
        yield channel
    except Exception as x:
        raise
    else:
        channel.close()


def create_grpc_server(addr: str, pool_size: int = 10,
                       cert_chain: bytes = None, priv_key: bytes = None,
                       root_certificates: bytes = None) -> Server:
    """
    Instanciate a gRPC server bound to the given ̀`addr`.

    If you provide `cert_chain` and `priv_key`, the server will expect secure
    communication from clients.

    If `root_certificates` is set, clients will authentication will be
    validated. This is optional.
    """
    server = grpc.server(ThreadPoolExecutor(max_workers=pool_size))
    if not cert_chain and not priv_key:
        server.add_insecure_port(addr)
    else:
        creds = grpc.ssl_server_credentials(
            ((priv_key, cert_chain),), root_certificates,
            require_client_auth=root_certificates is not None)
        server.add_secure_port(addr, server_credentials=creds)
    return server


def start_grpc_server(server: Server):
    """
    Start the given gRPC `server`.

    This does not block so, if you don't have a mainloop, this will simply
    finish immediatly with the thread/process.
    """
    server.start()


def stop_grpc_server(server: Server, timeout: int = 1):
    """
    Stop the given gRPC `server`.

    Allow a grace period set by the provided `timeout` (in seconds). Block
    until that timeout is reached.
    """
    terminated_event = server.stop(grace=timeout)
    terminated_event.wait(timeout=timeout + 0.2)
