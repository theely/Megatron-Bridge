# Apertus 1.5 needs a transformers that defines Apertus1p5ForConditionalGeneration (the
# swiss-ai/transformers fork, for now). Without it the bridge is not registered, so importing
# megatron.bridge.models keeps working for every other model.
try:
    from transformers import Apertus1p5ForConditionalGeneration  # noqa: F401
except ImportError:
    APERTUS1P5_AVAILABLE = False
else:
    APERTUS1P5_AVAILABLE = True

if APERTUS1P5_AVAILABLE:
    from megatron.bridge.models.apertus1p5.apertus1p5_bridge import Apertus1p5Bridge

    __all__ = ["APERTUS1P5_AVAILABLE", "Apertus1p5Bridge"]
else:
    __all__ = ["APERTUS1P5_AVAILABLE"]
