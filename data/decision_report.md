# Decision Report

- generated_at: 2026-06-12T15:44:58.461911+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6519**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.40% / filled 20/20。**
- 全期間 MARKET基準: n=6519, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.08% | **+0.70%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| ASK | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.55% | **+1.27%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.34% | **+0.60%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.72% | **+0.32%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.10% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$95.64** / 初期 $100.00 (-4.36%)
- 確定トレード: 19件 (TP 3 / SL 15 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.64
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.17** / 初期 $100.00 (+67.17%)
- 確定: 1392件 (Win 384 / Loss 452 / Flat 556) / skip 1688件
- 成長率目線: 平均log +0.000369 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $167.17

## 4. Latest Market Context

- 更新: 2026-06-12T15:44:55.391254+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=63875.5
- Funnel: target 774 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +95.32% | $62,931,883.49 |
| NAORIS/USDT:USDT | +43.77% | $6,824,039.49 |
| SKYAI/USDT:USDT | +39.38% | $17,900,392.82 |
| XPL/USDT:USDT | +37.66% | $16,081,980.22 |
| AIN/USDT:USDT | +36.83% | $1,458,626.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.20% | +3.35% |
| ENJ/USDT:USDT | below_1h_threshold | +3.03% | +3.18% |
| H/USDT:USDT | below_1h_threshold | +2.86% | +3.01% |
| ALLO/USDT:USDT | below_1h_threshold | +2.44% | +2.59% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.38% | +2.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
