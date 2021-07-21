import pkg_resources

from .interfaces.gen_classifier_conf_sal import GenerateClassifierConfidenceSaliency  # noqa: F401
from .interfaces.perturb_image import PerturbImage  # noqa: F401
from .interfaces.vis_sal_similarity import ImageSimilaritySaliencyMapGenerator  # noqa: F401
from .interfaces.vis_sal_image_classifier_blackbox import GenerateImageClassifierBlackboxSaliency  # noqa: F401


# It is known that this will fail if SMQTK-Core is not "installed" in the
# current environment. Additional support is pending defined use-case-driven
# requirements.
__version__ = pkg_resources.get_distribution(__name__).version
