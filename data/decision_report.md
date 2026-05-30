# Decision Report

- generated_at: 2026-05-30T12:54:42.295654+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5126**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.75% / filled 20/20。**
- 全期間 MARKET基準: n=5126, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.65% | **+1.40%** |
| ASK | 20/20 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_BB3S | 5/17 | 29.4% | +1.81% | **+0.53%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.63% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.26% | **+1.02%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.65% | **+0.49%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.39% | **+0.26%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.24% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.25** / 初期 $100.00 (+25.25%)
- 確定: 781件 (Win 183 / Loss 238 / Flat 360) / skip 906件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.91%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $125.25

## 4. Latest Market Context

- 更新: 2026-05-30T12:54:39.666623+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=73624.3
- Funnel: target 773 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +42.52% | $2,190,326.39 |
| LAB/USDT:USDT | +33.01% | $128,683,250.96 |
| NFP/USDT:USDT | +29.63% | $3,377,295.57 |
| STG/USDT:USDT | +23.84% | $1,498,582.96 |
| VTHO/USDT:USDT | +18.98% | $1,786,164.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FET/USDT:USDT | below_1h_threshold | +3.58% | +3.50% |
| GUA/USDT:USDT | below_1h_threshold | +3.36% | +3.28% |
| QNTSTOCK/USDT:USDT | below_1h_threshold | +3.00% | +2.92% |
| LAB/USDT:USDT | below_1h_threshold | +2.63% | +2.55% |
| BEAT/USDT:USDT | below_1h_threshold | +2.47% | +2.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
