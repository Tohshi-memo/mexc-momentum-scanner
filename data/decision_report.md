# Decision Report

- generated_at: 2026-05-30T13:39:50.374089+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5127**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.33% / filled 20/20。**
- 全期間 MARKET基準: n=5127, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.33% | **+1.20%** |
| ASK | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_BB3S | 5/17 | 29.4% | +1.81% | **+0.53%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.44% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.04% | **+1.22%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.73% | **+0.51%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.43% | **+0.32%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.35% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.25** / 初期 $100.00 (+25.25%)
- 確定: 782件 (Win 183 / Loss 238 / Flat 361) / skip 906件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.91%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $125.25

## 4. Latest Market Context

- 更新: 2026-05-30T13:39:47.736841+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=73659.4
- Funnel: target 773 → liquid 129 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.5 >= 65=1, 4h RSI 72.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +65.14% | $3,104,903.97 |
| LAB/USDT:USDT | +36.36% | $135,712,484.04 |
| NFP/USDT:USDT | +29.94% | $3,512,647.51 |
| STG/USDT:USDT | +25.97% | $1,791,268.89 |
| H/USDT:USDT | +25.92% | $6,211,412.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.31% | +4.31% |
| STG/USDT:USDT | below_1h_threshold | +3.66% | +3.67% |
| LAB/USDT:USDT | below_1h_threshold | +2.18% | +2.19% |
| OL/USDT:USDT | below_1h_threshold | +2.14% | +2.14% |
| UAI/USDT:USDT | below_1h_threshold | +2.06% | +2.07% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
