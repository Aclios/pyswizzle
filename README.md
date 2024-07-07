A python library which allow to swizzle and deswizzle some video games textures. Supported platforms: Nintendo Switch and PS4

# Usage

## Nintendo Switch:

<code>from pyswizzle import nsw_deswizzle, nsw_swizzle</code>

Deswizzle bytes:

<code>deswizzled_bytes = nsw_deswizzle(bytes, im_size, block_size, bytes_per_block, swizzle_mode)</code>

Swizzle bytes:

<code>swizzled_bytes = nsw_swizzle(bytes, im_size, block_size, bytes_per_block, swizzle_mode)</code>

## PS4:

<code>from pyswizzle import ps4_deswizzle, ps4_swizzle</code>

Deswizzle bytes:

<code>deswizzled_bytes = ps4_deswizzle(bytes, im_size, block_size, bytes_per_block)</code>

Swizzle bytes:

<code>swizzled_bytes = ps4_deswizzle(bytes, im_size, block_size, bytes_per_block)</code>

# Parameters

bytes: a bytes-like object, representing image data

im_size: a tuple (im_width,im_height) representing the dimensions of the image.

block_size: a tuple (bloc_width,bloc_height) representing the dimensions of the compression blocks of the image encoding.
For example, BC7 and BC1 are encoded with blocks of 4x4 pixels, so you should input (4,4), while ASTC6x6 are encoded with blocks of 6x6 pixels, so you should input (6,6).
For format that are not block compressed like RGBA8888, you should input (1,1).

bytes_per_block: the number of bytes used to encode one block. For BC7, it's equal to 16; for BC1: 8; for ASTC6x6: 16; for RGBA8888: 4, etc.

swizzle_mode: the swizzle mode, for Nintendo Switch.

# Notes

Not all images can be swizzled or deswizzled, they might require some padding. 

For Nintendo Switch, the image width must be a multiple of *64 x block_width / bytes_per_block* pixels, <br>and the image_height a multiple of *8 x block_height x (2\*\*swizzle_mode)* pixels.

For PS4, the image width must be a multiple of *8 x block_width* pixels, <br>and the image_height a multiple of *8 x block_height* pixels.
