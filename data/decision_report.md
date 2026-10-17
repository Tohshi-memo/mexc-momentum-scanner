# Decision Report

- generated_at: 2026-10-17T13:36:23.710279+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16878**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.68% / filled 20/20。**
- 全期間 MARKET基準: n=16878, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.83% | **+0.62%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.92% | **+0.51%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.49% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.49% | **+0.89%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.60% | **+0.39%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.07% | **-0.06%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | -0.54% | **-0.16%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.21% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,265.35** / 初期 $100.00 (+1165.35%)
- 確定: 6352件 (Win 1855 / Loss 2033 / Flat 2464) / skip 7087件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $1,265.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3690件 (Win 1027 / Loss 878 / Flat 1785) / skip 6599件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0439 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SIREN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5037件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000157 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-17T13:36:11.368345+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=81477.7
- Funnel: target 1084 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +91.15% | $20,030,234.23 |
| Q/USDT:USDT | +34.36% | $1,339,139.54 |
| EPIC/USDT:USDT | +28.62% | $1,538,389.24 |
| ICNT/USDT:USDT | +19.01% | $9,471,334.90 |
| BTW/USDT:USDT | +18.21% | $23,993,728.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +1.67% | +1.68% |
| A/USDT:USDT | below_1h_threshold | +1.28% | +1.29% |
| UVXY/USDT:USDT | below_1h_threshold | +1.24% | +1.25% |
| LIT/USDT:USDT | below_1h_threshold | +0.57% | +0.58% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.49% | +0.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
