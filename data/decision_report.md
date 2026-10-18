# Decision Report

- generated_at: 2026-10-18T01:46:19.617680+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16932**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.75% / filled 20/20。**
- 全期間 MARKET基準: n=16932, expectancy=+0.02%
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
| LIMIT_FIB1272 | 6/20 | 30.0% | +4.14% | **+1.24%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.42% | **+1.00%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.00% | **+0.85%** |
| LIMIT_BB3S | 7/18 | 38.9% | +2.07% | **+0.81%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.80% | **+0.81%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.08% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,292.27** / 初期 $100.00 (+1192.27%)
- 確定: 6398件 (Win 1864 / Loss 2046 / Flat 2488) / skip 7095件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.27% 残高後 $1,292.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.42** / 初期 $100.00 (+176.42%)
- 確定: 3697件 (Win 1029 / Loss 878 / Flat 1790) / skip 6646件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0454 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.18% 残高後 $276.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5090件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000191 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-18T01:46:07.372497+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.41% price=81847.7
- Funnel: target 1084 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +40.10% | $2,001,952.14 |
| AGT/USDT:USDT | +29.55% | $15,334,673.30 |
| BR/USDT:USDT | +26.73% | $10,408,246.28 |
| Q/USDT:USDT | +17.21% | $7,543,865.94 |
| AVA/USDT:USDT | +15.42% | $2,219,233.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_relative_strength | +5.12% | +4.71% |
| CLAUDIA/USDT:USDT | below_1h_threshold | +3.67% | +3.26% |
| BAT/USDT:USDT | below_1h_threshold | +3.06% | +2.64% |
| AVA/USDT:USDT | below_1h_threshold | +2.68% | +2.27% |
| NEAR/USDT:USDT | below_1h_threshold | +2.38% | +1.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
