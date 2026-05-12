# Decision Report

- generated_at: 2026-05-12T05:02:53.020391+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4095**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4095, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.58% | **-0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.04% | **+0.61%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.31% | **+0.26%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.09% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.01% | **+2.11%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.23% | **+2.01%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.12% | **+1.72%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.78% | **+1.52%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.90% | **+0.90%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$110.63** / 初期 $100.00 (+10.63%)
- 確定: 231件 (Win 60 / Loss 81 / Flat 90) / skip 425件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $110.63

## 4. Latest Market Context

- 更新: 2026-05-12T05:02:49.634220+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=81209.8
- Funnel: target 762 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +54.25% | $2,630,857.35 |
| SKYAI/USDT:USDT | +38.32% | $41,910,009.10 |
| SAGA/USDT:USDT | +30.07% | $7,992,564.69 |
| GUA/USDT:USDT | +24.95% | $1,495,047.88 |
| USELESS/USDT:USDT | +23.07% | $4,830,206.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +1.94% | +1.92% |
| SAGA/USDT:USDT | below_1h_threshold | +1.49% | +1.47% |
| JELLYJELLY/USDT:USDT | below_1h_threshold | +1.17% | +1.15% |
| BILL/USDT:USDT | below_1h_threshold | +1.14% | +1.13% |
| COLLECT/USDT:USDT | below_1h_threshold | +0.94% | +0.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
