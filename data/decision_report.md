# Decision Report

- generated_at: 2026-07-15T20:26:23.527200+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8763**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.35% / filled 20/20。**
- 全期間 MARKET基準: n=8763, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.35% | **+3.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.35% | **+3.35%** |
| LIMIT_1PCT | 18/20 | 90.0% | +3.27% | **+2.94%** |
| LIMIT_2PCT | 15/20 | 75.0% | +3.46% | **+2.59%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.56% | **+1.41%** |
| LIMIT_ATR | 11/20 | 55.0% | +2.13% | **+1.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +0.14% | **+0.14%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | -0.59% | **-0.39%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 98件 (TP 34 / SL 62 / EXP 2)
- 最新: MAGMA/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.89** / 初期 $100.00 (+242.89%)
- 確定: 2884件 (Win 903 / Loss 938 / Flat 1043) / skip 2440件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $342.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.40** / 初期 $100.00 (+5.40%)
- 確定: 727件 (Win 167 / Loss 168 / Flat 392) / skip 1447件
- 成長率目線: 平均log +0.000072 / 幾何平均 +0.007% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0942 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROAM/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $105.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 172件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000265 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-15T20:26:13.238340+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=64970.5
- Funnel: target 871 → liquid 173 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +16.20% | $2,835,677.56 |
| SKL/USDT:USDT | +13.22% | $1,556,138.63 |
| CAP/USDT:USDT | +12.03% | $1,241,996.02 |
| SNXX/USDT:USDT | +10.97% | $1,321,180.15 |
| ONDO/USDT:USDT | +6.09% | $27,366,647.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +2.86% | +2.80% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +2.30% | +2.23% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.06% | +1.99% |
| WLD/USDT:USDT | below_1h_threshold | +1.70% | +1.63% |
| ALABSTOCK/USDT:USDT | below_1h_threshold | +1.66% | +1.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
