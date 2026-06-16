# Decision Report

- generated_at: 2026-06-16T20:14:56.140679+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6883**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=6883, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.31% | **+0.46%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.51% | **+0.44%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.41% | **+0.27%** |
| ASK | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.17% | **+0.12%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.01% | **+0.01%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | -0.13% | **-0.13%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.27** / 初期 $100.00 (+84.27%)
- 確定: 1756件 (Win 463 / Loss 552 / Flat 741) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $184.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.02** / 初期 $100.00 (-1.98%)
- 確定: 158件 (Win 29 / Loss 30 / Flat 99) / skip 136件
- 成長率目線: 平均log -0.000126 / 幾何平均 -0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0427 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $98.02

## 5. Latest Market Context

- 更新: 2026-06-16T20:14:51.035624+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=65737.1
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +15.50% | $27,493,406.93 |
| PLAY/USDT:USDT | +13.00% | $1,434,323.85 |
| BLESS/USDT:USDT | +12.87% | $1,372,411.22 |
| H/USDT:USDT | +11.71% | $57,694,983.14 |
| SENT/USDT:USDT | +9.07% | $1,105,880.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +2.99% | +2.86% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.89% | +1.76% |
| VVV/USDT:USDT | below_1h_threshold | +1.85% | +1.72% |
| XPL/USDT:USDT | below_1h_threshold | +1.67% | +1.54% |
| ENA/USDT:USDT | below_1h_threshold | +1.48% | +1.35% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
