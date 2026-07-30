from __future__ import annotations

import unittest

from tools.live_preflight import (
    _count_open_positions,
    _finite_nonnegative_float,
    _usdt_balance,
    _validate_position_mode,
)


class NumericValidationTest(unittest.TestCase):
    def test_accepts_finite_nonnegative_numbers_and_numeric_strings(self) -> None:
        self.assertEqual(
            _finite_nonnegative_float(0, field="value"),
            0.0,
        )
        self.assertEqual(
            _finite_nonnegative_float("12.5", field="value"),
            12.5,
        )

    def test_rejects_nonfinite_negative_missing_and_bool_values(self) -> None:
        invalid_values = (
            float("nan"),
            float("inf"),
            float("-inf"),
            -0.01,
            None,
            True,
            False,
            "not-a-number",
        )
        for value in invalid_values:
            with self.subTest(value=value):
                with self.assertRaisesRegex(RuntimeError, "finite non-negative"):
                    _finite_nonnegative_float(value, field="value")


class BalanceValidationTest(unittest.TestCase):
    def test_returns_validated_free_and_total_balance(self) -> None:
        self.assertEqual(
            _usdt_balance({"USDT": {"free": "5.25", "total": 10}}),
            (5.25, 10.0),
        )

    def test_rejects_nonfinite_or_negative_free_and_total(self) -> None:
        invalid_values = (
            float("nan"),
            float("inf"),
            float("-inf"),
            -1,
        )
        for field in ("free", "total"):
            for value in invalid_values:
                with self.subTest(field=field, value=value):
                    usdt = {"free": 5.0, "total": 10.0}
                    usdt[field] = value
                    with self.assertRaisesRegex(RuntimeError, field):
                        _usdt_balance({"USDT": usdt})

    def test_rejects_missing_or_malformed_balance_objects(self) -> None:
        invalid_balances = (
            None,
            [],
            {},
            {"USDT": None},
            {"USDT": {}},
            {"USDT": {"free": 1.0}},
            {"USDT": {"total": 1.0}},
        )
        for balance in invalid_balances:
            with self.subTest(balance=balance):
                with self.assertRaises(RuntimeError):
                    _usdt_balance(balance)


class PositionModeValidationTest(unittest.TestCase):
    def test_accepts_exact_bool_matching_expected_mode(self) -> None:
        self.assertTrue(
            _validate_position_mode({"hedged": True}, "hedged")
        )
        self.assertFalse(
            _validate_position_mode({"hedged": False}, "one_way")
        )

    def test_rejects_truthy_or_falsy_non_bool_hedged_values(self) -> None:
        for value in ("true", "false", 1, 0, None, [], {}):
            with self.subTest(value=value):
                with self.assertRaisesRegex(RuntimeError, "strict bool"):
                    _validate_position_mode({"hedged": value}, "hedged")

    def test_rejects_mode_mismatch_and_invalid_mode_config(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "mode mismatch"):
            _validate_position_mode({"hedged": False}, "hedged")
        with self.assertRaisesRegex(RuntimeError, "mode mismatch"):
            _validate_position_mode({"hedged": True}, "one_way")
        with self.assertRaisesRegex(RuntimeError, "LIVE_POSITION_MODE"):
            _validate_position_mode({"hedged": True}, "invalid")


class PositionValidationTest(unittest.TestCase):
    def test_counts_only_finite_positive_contracts(self) -> None:
        positions = [
            {"contracts": 0},
            {"contracts": "0.0"},
            {"contracts": 1},
            {"contracts": "2.5"},
        ]
        self.assertEqual(_count_open_positions(positions), 2)

    def test_rejects_nonfinite_or_negative_contracts(self) -> None:
        invalid_values = (
            float("nan"),
            float("inf"),
            float("-inf"),
            -1,
        )
        for value in invalid_values:
            with self.subTest(value=value):
                with self.assertRaisesRegex(RuntimeError, "contracts"):
                    _count_open_positions([{"contracts": value}])

    def test_rejects_missing_or_malformed_position_data(self) -> None:
        invalid_positions = (
            None,
            {},
            [None],
            ["position"],
            [{}],
            [{"contracts": None}],
        )
        for positions in invalid_positions:
            with self.subTest(positions=positions):
                with self.assertRaises(RuntimeError):
                    _count_open_positions(positions)


if __name__ == "__main__":
    unittest.main()
