# Decision Report

- generated_at: 2026-07-21T02:11:20.258051+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9138**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=9138, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.63% | **+1.31%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.00% | **+0.90%** |
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.01% | **-0.01%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.59% | **+0.53%** |
| MARKET_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.62% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$404.40** / 初期 $100.00 (+304.40%)
- 確定: 3200件 (Win 1001 / Loss 1018 / Flat 1181) / skip 2499件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $404.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.72** / 初期 $100.00 (+27.72%)
- 確定: 1099件 (Win 287 / Loss 226 / Flat 586) / skip 1450件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1263 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $127.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.45** / 初期 $100.00 (+1.45%)
- 確定: 334件 (Win 118 / Loss 147 / Flat 69) / pending 6件 / skip 273件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000277 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: US/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $101.45

## 6. Latest Market Context

- 更新: 2026-07-21T02:11:10.693452+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=65264.1
- Funnel: target 885 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ERA/USDT:USDT | +47.62% | $1,065,730.04 |
| JIMOTHY/USDT:USDT | +22.85% | $2,782,683.97 |
| BLESS/USDT:USDT | +12.55% | $1,627,652.78 |
| HEMI/USDT:USDT | +9.63% | $3,156,991.76 |
| LDO/USDT:USDT | +8.95% | $6,108,542.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.41% | +2.32% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.57% | +1.49% |
| BLESS/USDT:USDT | below_1h_threshold | +1.34% | +1.25% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.07% | +0.98% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.94% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
