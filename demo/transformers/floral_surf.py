from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Execute Transformer Action: ActionType.AVERAGE

    Docs: https://docs.mage.ai/guides/transformer-blocks#aggregation-actions
    """
    action = build_transformer_action(
    df,
    action_type=ActionType.AVERAGE,
    action_code='vendor_id != null',
    arguments=['fare_amount', 'tip_amount'],
    axis=Axis.COLUMN,
    options={'groupby_columns': ['vendor_id','pickup_datetime']},
    outputs=[
        {'uuid': 'avg_rev_per_brand', 'column_type': 'number_with_decimals'},
        {'uuid': 'avg_cost_per_brand', 'column_type': 'number_with_decimals'},
    ],
)


    return BaseAction(action).execute(df)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
