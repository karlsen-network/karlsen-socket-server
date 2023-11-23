# encoding: utf-8

from server import karlsend_client


async def get_network():
    """
    Get some global karlsen network information
    """
    resp = await karlsend_client.request("getBlockDagInfoRequest")
    return resp["getBlockDagInfoResponse"]
