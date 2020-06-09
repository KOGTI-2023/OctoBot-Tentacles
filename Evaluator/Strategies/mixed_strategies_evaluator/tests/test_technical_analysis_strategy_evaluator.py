#  Drakkar-Software OctoBot-Tentacles
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
import pytest

from tests.functional_tests.strategy_evaluators_tests.abstract_strategy_test import AbstractStrategyTest
from tentacles.Evaluator.Strategies import TechnicalAnalysisStrategyEvaluator
from tentacles.Trading.Mode import DailyTradingMode


# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


@pytest.fixture()
def strategy_tester():
    strategy_tester_instance = TechnicalAnalysisStrategyEvaluatorTest()
    strategy_tester_instance.initialize(TechnicalAnalysisStrategyEvaluator, DailyTradingMode)
    return strategy_tester_instance


class TechnicalAnalysisStrategyEvaluatorTest(AbstractStrategyTest):
    """
    About using this test framework:
    To be called by pytest, tests have to be called manually since the cythonized version of AbstractStrategyTest
    creates an __init__() which prevents the default pytest tests collect process
    """

    async def test_default_run(self):
        # market: -12.052505966587105
        await self.run_test_default_run(-2.717)

    async def test_slow_downtrend(self):
        # market: -12.052505966587105
        # market: -15.195702225633141
        # market: -29.12366137549725
        # market: -32.110091743119256
        await self.run_test_slow_downtrend(-2.717, -4.584, -9.798, -12.499)

    async def test_sharp_downtrend(self):
        # market: -26.07183938094741
        # market: -32.1654501216545
        await self.run_test_sharp_downtrend(-19.514, -13.323)

    async def test_flat_markets(self):
        # market: -10.560669456066947
        # market: -3.401191658391241
        # market: -5.7854560064282765
        # market: -8.067940552016978
        await self.run_test_flat_markets(-0.811, 0.733, -7.592, 8.305)

    async def test_slow_uptrend(self):
        # market: 17.203948364436457
        # market: 16.19613670133728
        await self.run_test_slow_uptrend(3.895, 16.903)

    async def test_sharp_uptrend(self):
        # market: 30.881852230166828
        # market: 12.28597871355852
        await self.run_test_sharp_uptrend(11.995, 0.035)

    async def test_up_then_down(self):
        # market: -6.040105108015155
        await self.run_test_up_then_down(0.161)


async def test_default_run(strategy_tester):
    await strategy_tester.test_default_run()


async def test_slow_downtrend(strategy_tester):
    await strategy_tester.test_slow_downtrend()


async def test_sharp_downtrend(strategy_tester):
    await strategy_tester.test_sharp_downtrend()


async def test_flat_markets(strategy_tester):
    await strategy_tester.test_flat_markets()


async def test_slow_uptrend(strategy_tester):
    await strategy_tester.test_slow_uptrend()


async def test_sharp_uptrend(strategy_tester):
    await strategy_tester.test_sharp_uptrend()


async def test_up_then_down(strategy_tester):
    await strategy_tester.test_up_then_down()
