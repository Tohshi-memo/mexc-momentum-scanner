# Decision Report

- generated_at: 2026-06-07T02:55:20.386115+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5923**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=5923, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.25% | **+1.25%** |
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| ASK | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.77% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.44% | **+1.10%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +1.21% | **+0.81%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +2.15% | **+0.64%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.26% | **+0.22%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.10% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$137.39** / 初期 $100.00 (+37.39%)
- 確定: 1044件 (Win 251 / Loss 321 / Flat 472) / skip 1440件
- 成長率目線: 平均log +0.000304 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $137.39

## 4. Latest Market Context

- 更新: 2026-06-07T02:55:14.920669+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=61490.2
- Funnel: target 771 → liquid 129 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.1 >= 65=1, 4h RSI 68.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +52.64% | $64,927,635.33 |
| SKYAI/USDT:USDT | +33.40% | $34,271,020.80 |
| FIDA/USDT:USDT | +32.59% | $3,650,770.77 |
| BTW/USDT:USDT | +24.36% | $10,789,750.20 |
| EDEN/USDT:USDT | +21.86% | $1,266,337.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.40% | +3.34% |
| ALLO/USDT:USDT | below_1h_threshold | +2.52% | +2.46% |
| FIDA/USDT:USDT | below_1h_threshold | +2.27% | +2.21% |
| BABY/USDT:USDT | below_1h_threshold | +1.53% | +1.47% |
| TAO/USDT:USDT | below_1h_threshold | +1.50% | +1.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
