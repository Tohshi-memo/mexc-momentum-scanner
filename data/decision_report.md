# Decision Report

- generated_at: 2026-10-17T11:11:30.871211+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16869**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.08% / filled 20/20。**
- 全期間 MARKET基準: n=16869, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.08% | **+2.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.08% | **+2.08%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.46% | **+1.24%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.56% | **+1.01%** |
| LIMIT_ATR | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.92% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.08% | **-0.04%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -2.29% | **-0.23%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,271.71** / 初期 $100.00 (+1171.71%)
- 確定: 6343件 (Win 1855 / Loss 2032 / Flat 2456) / skip 7087件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $1,271.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3689件 (Win 1027 / Loss 878 / Flat 1784) / skip 6591件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0550 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5031件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000177 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-17T11:11:18.124612+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=81616.4
- Funnel: target 1084 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +92.39% | $19,022,006.53 |
| EPIC/USDT:USDT | +23.66% | $1,206,329.33 |
| BTW/USDT:USDT | +12.74% | $23,390,867.97 |
| UVXY/USDT:USDT | +11.12% | $2,968,571.60 |
| FOLKS/USDT:USDT | +10.39% | $1,655,378.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.73% | +4.73% |
| EPIC/USDT:USDT | below_1h_threshold | +1.79% | +1.79% |
| AGT/USDT:USDT | below_1h_threshold | +1.74% | +1.74% |
| TMX/USDT:USDT | below_1h_threshold | +1.45% | +1.44% |
| MAGIC/USDT:USDT | below_1h_threshold | +1.39% | +1.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
