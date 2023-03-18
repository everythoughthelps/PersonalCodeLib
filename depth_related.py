import matplotlib as mpl
import matplotlib.cm as cm
import numpy as np
class DepthMap():
    def __int__(self):

    def color_depth(self, depth):
        normalizer = mpl.colors.Normalize(vmin=depth.min(), vmax=depth.max())
        mapper = cm.ScalarMappable(norm=normalizer, cmap='rainbow')
        # choices of cmap: rainbow, magma,
        colored_depth = (mapper.to_rgba(depth)[:, :, :3] * 255.0).astype(np.uint8)
        return colored_depth


    def normalize_depth(self, depth)
        vmax = np.percentile(depth, 95)
        normalizer = mpl.colors.Normalize(vmin=depth.min(), vmax=vmax)
        normalized_depth = normalizer(depth)
        return normalized_depth
