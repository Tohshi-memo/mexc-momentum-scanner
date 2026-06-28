# Decision Report

- generated_at: 2026-06-28T05:30:21.835689+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7730**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=7730, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +5.04% | **+0.76%** |
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |
| ASK | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_5PCT | 6/20 | 30.0% | -0.70% | **-0.21%** |
| LIMIT_6PCT | 4/20 | 20.0% | -1.06% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.34% | **+0.34%** |
| ASK_LONG | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.15% | **-0.02%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$240.71** / 初期 $100.00 (+140.71%)
- 確定: 2238件 (Win 675 / Loss 748 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: O/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $240.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 686件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T05:30:14.948688+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.49% price=59810.1
- Funnel: target 806 → liquid 122 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACT/USDT:USDT | +20.09% | $1,114,491.24 |
| BAS/USDT:USDT | +18.91% | $3,411,090.22 |
| LAB/USDT:USDT | +14.22% | $39,064,350.45 |
| S/USDT:USDT | +13.92% | $5,078,264.48 |
| VELVET/USDT:USDT | +11.62% | $270,799,962.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +1.86% | +2.36% |
| RAVE/USDT:USDT | below_1h_threshold | +1.85% | +2.34% |
| BAS/USDT:USDT | below_1h_threshold | +1.69% | +2.19% |
| S/USDT:USDT | below_1h_threshold | +1.17% | +1.66% |
| O/USDT:USDT | below_1h_threshold | +1.11% | +1.60% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
