# Decision Report

- generated_at: 2026-06-07T02:11:26.392180+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5919**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=5919, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| ASK | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.79% | **+0.75%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.77% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +3.90% | **+2.78%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.79% | **+0.67%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.13% | **+0.53%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.71% | **+0.28%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$138.08** / 初期 $100.00 (+38.08%)
- 確定: 1042件 (Win 251 / Loss 320 / Flat 471) / skip 1438件
- 成長率目線: 平均log +0.000310 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $138.08

## 4. Latest Market Context

- 更新: 2026-06-07T02:11:23.786704+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=61488.8
- Funnel: target 771 → liquid 127 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.9 >= 65=1, 4h RSI 70.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +52.39% | $62,891,562.47 |
| SKYAI/USDT:USDT | +36.65% | $32,513,087.81 |
| FIDA/USDT:USDT | +30.64% | $3,556,923.68 |
| CLO/USDT:USDT | +24.90% | $2,613,912.37 |
| BTW/USDT:USDT | +23.97% | $10,649,350.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +1.57% | +1.51% |
| BABY/USDT:USDT | below_1h_threshold | +1.27% | +1.22% |
| PENGU/USDT:USDT | below_1h_threshold | +1.15% | +1.10% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.08% | +1.03% |
| ALLO/USDT:USDT | below_1h_threshold | +1.01% | +0.95% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
