from pyswizzle.pyswizzle import BytesSwizzle,BytesDeswizzle

def nsw_deswizzle(data: bytearray | bytes,im_size: (int,int),block_size: (int,int),bytes_per_block: int,swizzle_mode: int) -> bytes:
    deswizzle = BytesDeswizzle('nsw',data, im_size, block_size, bytes_per_block, swizzle_mode)
    return deswizzle.deswizzle()

def nsw_swizzle(data: bytearray | bytes,im_size: (int,int),block_size: (int,int),bytes_per_block: int,swizzle_mode: int) -> bytes:
    swizzle = BytesSwizzle('nsw',data, im_size, block_size, bytes_per_block, swizzle_mode)
    return swizzle.swizzle()

def ps4_deswizzle(data: bytearray | bytes,im_size: (int,int),block_size: (int,int),bytes_per_block: int) -> bytes:
    deswizzle = BytesDeswizzle('ps4',data, im_size, block_size, bytes_per_block)
    return deswizzle.deswizzle()

def ps4_swizzle(data: bytearray | bytes,im_size: (int,int),block_size: (int,int),bytes_per_block: int) -> bytes:
    swizzle = BytesSwizzle('ps4',data, im_size, block_size, bytes_per_block)
    return swizzle.swizzle()