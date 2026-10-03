# Decision Report

- generated_at: 2026-10-03T06:36:25.558102+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16041**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=16041, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +0.95% | **+0.86%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.33% | **+1.16%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.44% | **+1.11%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.58%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.11% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,291.26** / 初期 $100.00 (+1191.26%)
- 確定: 6146件 (Win 1812 / Loss 1972 / Flat 2362) / skip 6456件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MANA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.46% 残高後 $1,291.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3606件 (Win 1005 / Loss 845 / Flat 1756) / skip 5846件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0348 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4204件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000163 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-03T06:36:12.048969+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=84608.5
- Funnel: target 1099 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +31.89% | $17,996,521.99 |
| SAND/USDT:USDT | +25.10% | $111,580,889.33 |
| VELVET/USDT:USDT | +11.02% | $10,427,826.09 |
| NIGHT/USDT:USDT | +10.45% | $12,104,097.95 |
| AKE/USDT:USDT | +6.75% | $2,696,386.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IMX/USDT:USDT | below_1h_threshold | +3.82% | +3.81% |
| AKE/USDT:USDT | below_1h_threshold | +3.45% | +3.44% |
| VELVET/USDT:USDT | below_1h_threshold | +2.10% | +2.10% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.71% | +1.70% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.65% | +1.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
