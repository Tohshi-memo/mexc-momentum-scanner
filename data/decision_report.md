# Decision Report

- generated_at: 2026-06-17T21:01:37.178706+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6967**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=6967, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.40% | **+0.40%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_BB3S | 7/15 | 46.7% | +0.68% | **+0.32%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.42% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +4.81% | **+2.89%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.21% | **+0.97%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.22% | **+0.79%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.89% | **+0.67%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.71** / 初期 $100.00 (+98.71%)
- 確定: 1818件 (Win 496 / Loss 573 / Flat 749) / skip 1710件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $198.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$102.92** / 初期 $100.00 (+2.92%)
- 確定: 240件 (Win 63 / Loss 59 / Flat 118) / skip 138件
- 成長率目線: 平均log +0.000120 / 幾何平均 +0.012% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0591 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $102.92

## 5. Latest Market Context

- 更新: 2026-06-17T21:01:31.977572+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64413.6
- Funnel: target 790 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +77.86% | $1,133,776.00 |
| SYN/USDT:USDT | +64.01% | $2,708,840.29 |
| RE/USDT:USDT | +16.18% | $1,714,406.72 |
| MITO/USDT:USDT | +8.64% | $1,490,150.33 |
| TAC/USDT:USDT | +7.19% | $2,392,145.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +1.42% | +1.41% |
| ALLO/USDT:USDT | below_1h_threshold | +0.78% | +0.77% |
| BSB/USDT:USDT | below_1h_threshold | +0.46% | +0.45% |
| PLAY/USDT:USDT | below_1h_threshold | +0.45% | +0.44% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.34% | +0.33% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
