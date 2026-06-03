# Decision Report

- generated_at: 2026-06-03T16:15:04.782436+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5558**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.10% / filled 20/20。**
- 全期間 MARKET基準: n=5558, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.16% | **+1.16%** |
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.00% | **+0.75%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.63% | **+0.57%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.84% | **+0.46%** |
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +0.71% | **+0.43%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1004件 (Win 239 / Loss 312 / Flat 453) / skip 1115件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-03T16:14:58.865407+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=66184.3
- Funnel: target 771 → liquid 147 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.7 >= 65=1, 4h RSI 70.8 >= 65=1, 4h RSI 72.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +15.01% | $1,667,573.30 |
| BP/USDT:USDT | +7.49% | $1,250,579.43 |
| EPIC/USDT:USDT | +6.82% | $3,295,712.43 |
| LAB/USDT:USDT | +5.50% | $281,157,415.23 |
| MAGMA/USDT:USDT | +2.56% | $2,742,643.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +2.59% | +2.37% |
| USELESS/USDT:USDT | below_1h_threshold | +1.84% | +1.62% |
| BILL/USDT:USDT | below_1h_threshold | +1.84% | +1.62% |
| EDGE/USDT:USDT | below_1h_threshold | +1.49% | +1.27% |
| STG/USDT:USDT | below_1h_threshold | +1.25% | +1.03% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
