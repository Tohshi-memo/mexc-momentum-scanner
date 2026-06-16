# Decision Report

- generated_at: 2026-06-16T17:03:22.431174+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6873**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=6873, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.37% | **+0.37%** |
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.96% | **+0.19%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.19% | **+0.06%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +3.85% | **+3.30%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.97% | **+0.72%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.81% | **+0.61%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.54% | **+0.46%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.28% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.05** / 初期 $100.00 (+84.05%)
- 確定: 1746件 (Win 459 / Loss 548 / Flat 739) / skip 1688件
- 成長率目線: 平均log +0.000349 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $184.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 128件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0037 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T16:53:42.312579+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=65709.6
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +7.71% | $22,070,183.78 |
| STG/USDT:USDT | +7.29% | $3,153,086.37 |
| ESPORTS/USDT:USDT | +5.16% | $1,604,928.80 |
| BSB/USDT:USDT | +5.10% | $39,255,658.18 |
| H/USDT:USDT | +4.38% | $65,168,828.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.77% | +4.97% |
| WDCSTOCK/USDT:USDT | below_1h_threshold | +3.33% | +3.53% |
| BILL/USDT:USDT | below_1h_threshold | +3.18% | +3.38% |
| BR/USDT:USDT | below_1h_threshold | +2.82% | +3.02% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +2.73% | +2.93% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
