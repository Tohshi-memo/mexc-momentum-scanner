# Decision Report

- generated_at: 2026-05-23T11:03:58.999323+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4771**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.11% / filled 20/20。**
- 全期間 MARKET基準: n=4771, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+2.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.11% | **+2.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.11% | **+2.11%** |
| ASK | 20/20 | 100.0% | +2.09% | **+2.09%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.31% | **+1.11%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| MARKET_LONG | 20/20 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -0.04% | **-0.03%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | -0.15% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.91** / 初期 $100.00 (+20.91%)
- 確定: 616件 (Win 150 / Loss 195 / Flat 271) / skip 716件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $120.91

## 4. Latest Market Context

- 更新: 2026-05-23T11:03:56.598999+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=74707.3
- Funnel: target 764 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +140.98% | $77,824,465.47 |
| BEAT/USDT:USDT | +24.66% | $67,557,828.24 |
| IN/USDT:USDT | +20.64% | $2,048,704.37 |
| GMTTOKEN/USDT:USDT | +17.53% | $2,695,522.56 |
| BILL/USDT:USDT | +12.84% | $16,402,101.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.78% | +4.74% |
| GMTTOKEN/USDT:USDT | below_1h_threshold | +0.98% | +0.94% |
| MYX/USDT:USDT | below_1h_threshold | +0.85% | +0.82% |
| H/USDT:USDT | below_1h_threshold | +0.64% | +0.61% |
| BILL/USDT:USDT | below_1h_threshold | +0.62% | +0.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
