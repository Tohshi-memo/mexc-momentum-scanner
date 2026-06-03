# Decision Report

- generated_at: 2026-06-03T15:18:36.026355+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5555**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.64% / filled 20/20。**
- 全期間 MARKET基準: n=5555, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.64% | **+0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.67% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.31% | **+1.05%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.99% | **+0.74%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +0.71% | **+0.53%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.47% | **+0.42%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.83% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1004件 (Win 239 / Loss 312 / Flat 453) / skip 1112件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-03T15:18:33.644663+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.69% price=66382.1
- Funnel: target 771 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +38.28% | $2,106,751.75 |
| ENA/USDT:USDT | +36.14% | $69,311,541.17 |
| CLO/USDT:USDT | +35.66% | $5,270,543.01 |
| BP/USDT:USDT | +33.47% | $1,213,703.14 |
| LIT/USDT:USDT | +31.81% | $11,263,419.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BP/USDT:USDT | below_1h_threshold | +4.93% | +5.62% |
| XPL/USDT:USDT | below_1h_threshold | +4.59% | +5.28% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.94% | +4.63% |
| JTO/USDT:USDT | below_1h_threshold | +1.77% | +2.46% |
| LIT/USDT:USDT | below_1h_threshold | +1.18% | +1.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
