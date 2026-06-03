# Decision Report

- generated_at: 2026-06-03T17:54:09.378862+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5568**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.70% / filled 20/20。**
- 全期間 MARKET基準: n=5568, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| ASK | 20/20 | 100.0% | +0.80% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.69% | **+0.55%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.66% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +4.00% | **+1.71%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +3.49% | **+0.87%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.51% | **+0.46%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.66% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$97.09** / 初期 $100.00 (-2.91%)
- 確定トレード: 92件 (TP 27 / SL 62 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.09
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1004件 (Win 239 / Loss 312 / Flat 453) / skip 1125件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-03T17:54:06.741069+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=65793.5
- Funnel: target 768 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +40.42% | $6,501,739.31 |
| BP/USDT:USDT | +11.64% | $1,411,155.00 |
| EDEN/USDT:USDT | +6.91% | $1,451,718.70 |
| HEI/USDT:USDT | +6.11% | $1,023,732.63 |
| MAGMA/USDT:USDT | +5.29% | $3,283,693.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +4.82% | +5.19% |
| APR/USDT:USDT | below_1h_threshold | +3.44% | +3.81% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.92% | +2.28% |
| EDGE/USDT:USDT | below_1h_threshold | +1.80% | +2.17% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.76% | +2.12% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
