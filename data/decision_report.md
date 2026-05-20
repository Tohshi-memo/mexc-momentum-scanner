# Decision Report

- generated_at: 2026-05-20T16:21:31.571595+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4554**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.52% / filled 20/20。**
- 全期間 MARKET基準: n=4554, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.02% | **+0.97%** |
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.68% | **+0.51%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.52% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.12% | **+0.50%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.05% | **+0.04%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.09% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.96** / 初期 $100.00 (+24.96%)
- 確定: 516件 (Win 136 / Loss 175 / Flat 205) / skip 599件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $124.96

## 4. Latest Market Context

- 更新: 2026-05-20T16:21:29.023857+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=77197.6
- Funnel: target 763 → liquid 129 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +8.18% | $37,513,274.11 |
| EDEN/USDT:USDT | +3.04% | $25,817,930.29 |
| NAORIS/USDT:USDT | +3.01% | $1,065,580.92 |
| LYN/USDT:USDT | +2.99% | $1,068,043.40 |
| PLAY/USDT:USDT | +2.89% | $16,621,500.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +3.15% | +3.44% |
| NAORIS/USDT:USDT | below_1h_threshold | +3.01% | +3.30% |
| LYN/USDT:USDT | below_1h_threshold | +3.00% | +3.29% |
| PLAY/USDT:USDT | below_1h_threshold | +2.95% | +3.24% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.80% | +2.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
