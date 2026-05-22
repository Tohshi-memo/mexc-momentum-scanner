# Decision Report

- generated_at: 2026-05-22T16:09:03.896247+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4716**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=4716, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.60% | **+0.51%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.81% | **+0.45%** |
| ASK | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.01% | **+0.40%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +0.89% | **+0.22%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.18% | **+0.13%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.12% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.06** / 初期 $100.00 (+21.06%)
- 確定: 565件 (Win 144 / Loss 187 / Flat 234) / skip 712件
- 成長率目線: 平均log +0.000338 / 幾何平均 +0.034% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VVV/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $121.06

## 4. Latest Market Context

- 更新: 2026-05-22T16:09:01.631463+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=76753.6
- Funnel: target 768 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +4.26% | $5,423,286.77 |
| USELESS/USDT:USDT | +1.91% | $1,196,496.42 |
| GRASS/USDT:USDT | +1.81% | $8,453,152.57 |
| BEAT/USDT:USDT | +1.72% | $29,050,022.51 |
| PENDLE/USDT:USDT | +1.09% | $2,886,268.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BUILDONBOB/USDT:USDT | below_1h_threshold | +4.37% | +4.38% |
| USELESS/USDT:USDT | below_1h_threshold | +1.92% | +1.92% |
| GRASS/USDT:USDT | below_1h_threshold | +1.81% | +1.82% |
| BEAT/USDT:USDT | below_1h_threshold | +1.72% | +1.72% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.27% | +1.28% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
