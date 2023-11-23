# encoding: utf-8

from server import karlsend_client


async def get_blockdag():
    """
    Get some global Karlsen BlockDAG information
    """
    resp = await karlsend_client.request("getBlockDagInfoRequest")
    return resp["getBlockDagInfoResponse"]
