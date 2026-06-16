# Decision Report

- generated_at: 2026-06-16T20:21:52.286701+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6884**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.87% / filled 20/20。**
- 全期間 MARKET基準: n=6884, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.93% | **+0.84%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.31% | **+0.46%** |
| ASK | 20/20 | 100.0% | +0.35% | **+0.35%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.41% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.17% | **+0.12%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | -0.07% | **-0.05%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | -0.15% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$183.35** / 初期 $100.00 (+83.35%)
- 確定: 1757件 (Win 463 / Loss 553 / Flat 741) / skip 1688件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $183.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.68** / 初期 $100.00 (-2.32%)
- 確定: 159件 (Win 29 / Loss 31 / Flat 99) / skip 136件
- 成長率目線: 平均log -0.000148 / 幾何平均 -0.015% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0237 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $97.68

## 5. Latest Market Context

- 更新: 2026-06-16T20:21:47.129721+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=65789.9
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +17.11% | $27,689,423.95 |
| BLESS/USDT:USDT | +13.47% | $1,463,946.17 |
| PLAY/USDT:USDT | +13.15% | $1,487,195.41 |
| SENT/USDT:USDT | +10.86% | $1,112,827.08 |
| ESPORTS/USDT:USDT | +8.47% | $1,648,805.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENA/USDT:USDT | below_1h_threshold | +3.11% | +2.90% |
| WLD/USDT:USDT | below_1h_threshold | +2.73% | +2.52% |
| FLOKI/USDT:USDT | below_1h_threshold | +2.69% | +2.48% |
| VVV/USDT:USDT | below_1h_threshold | +2.33% | +2.12% |
| VELVET/USDT:USDT | below_1h_threshold | +2.19% | +1.98% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
