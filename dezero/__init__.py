# =============================================================================
# step23.py부터 step32.py까지는 simple_core를 이용해야 합니다.
# is_simple_core = True  # True
# 고차 미분에 대응하기 위해 다음과 같이 설정
is_simple_core = False
# =============================================================================

if is_simple_core:
    from dezero.core_simple import Variable
    from dezero.core_simple import Function
    from dezero.core_simple import using_config
    from dezero.core_simple import no_grad
    from dezero.core_simple import as_array
    from dezero.core_simple import as_variable
    from dezero.core_simple import setup_variable

else:

    # 제 2-3고지
    from dezero.core import Variable
    from dezero.core import Function
    from dezero.core import using_config
    from dezero.core import no_grad
    from dezero.core import as_array
    from dezero.core import as_variable
    from dezero.core import setup_variable

    # from dezero.layers import Layer
    # from dezero.models import Model
    # from dezero.datasets import Dataset
    # from dezero.dataloaders import DataLoader
    # from dezero.dataloaders import SeqDataLoader

setup_variable()
__version__ = '0.0.13'
