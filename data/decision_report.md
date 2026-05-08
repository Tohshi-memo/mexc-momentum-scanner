# Decision Report

- generated_at: 2026-05-08T04:27:38.208717+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3733**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.26% / filled 20/20。**
- 全期間 MARKET基準: n=3733, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+2.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.26% | **+2.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.26% | **+2.26%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.65% | **+2.25%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.28% | **+1.71%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +3.06% | **+1.22%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.02% | **+1.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.06% | **+0.53%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.75% | **+0.41%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.40% | **+0.35%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.17% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$98.83** / 初期 $100.00 (-1.17%)
- 確定トレード: 24件 (TP 6 / SL 16 / EXP 2)
- 最新: PENGUIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 190件 (Win 48 / Loss 64 / Flat 78) / skip 104件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T04:27:35.228584+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=79629.2
- Funnel: target 771 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +34.66% | $2,443,034.72 |
| LAB/USDT:USDT | +21.05% | $212,228,367.25 |
| DYDX/USDT:USDT | +20.99% | $12,584,392.69 |
| NOT/USDT:USDT | +19.69% | $10,939,101.90 |
| TST/USDT:USDT | +19.52% | $6,346,235.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.86% | +3.75% |
| JTO/USDT:USDT | below_1h_threshold | +3.08% | +2.96% |
| VVV/USDT:USDT | below_1h_threshold | +3.07% | +2.96% |
| PLAY/USDT:USDT | below_1h_threshold | +3.06% | +2.94% |
| DYDX/USDT:USDT | below_1h_threshold | +2.91% | +2.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
