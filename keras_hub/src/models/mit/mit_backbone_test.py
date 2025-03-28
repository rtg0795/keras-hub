import numpy as np
import pytest

from keras_hub.src.models.mit.mit_backbone import MiTBackbone
from keras_hub.src.tests.test_case import TestCase


class MiTBackboneTest(TestCase):
    def setUp(self):
        self.init_kwargs = {
            "layerwise_depths": [2, 2],
            "image_shape": (32, 32, 3),
            "hidden_dims": [4, 8],
            "num_layers": 2,
            "layerwise_num_heads": [1, 2],
            "layerwise_sr_ratios": [8, 4],
            "max_drop_path_rate": 0.1,
            "layerwise_patch_sizes": [7, 3],
            "layerwise_strides": [4, 2],
        }
        self.input_size = 32
        self.input_data = np.ones(
            (2, self.input_size, self.input_size, 3), dtype="float32"
        )

    def test_backbone_basics(self):
        self.run_vision_backbone_test(
            cls=MiTBackbone,
            init_kwargs=self.init_kwargs,
            input_data=self.input_data,
            expected_output_shape=(2, 4, 4, 8),
            expected_pyramid_output_keys=["P1", "P2"],
            expected_pyramid_image_sizes=[(8, 8), (4, 4)],
            run_quantization_check=False,
            run_mixed_precision_check=False,
            run_data_format_check=False,
        )

    @pytest.mark.large
    def test_saved_model(self):
        self.run_model_saving_test(
            cls=MiTBackbone,
            init_kwargs=self.init_kwargs,
            input_data=self.input_data,
        )
