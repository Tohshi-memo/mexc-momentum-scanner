# Decision Report

- generated_at: 2026-08-10T09:36:30.255358+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11145**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.42% / filled 20/20。**
- 全期間 MARKET基準: n=11145, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.42% | **+1.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.64% | **+1.48%** |
| MARKET | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.81% | **+0.44%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.63% | **+0.44%** |
| LIMIT_BB3S | 3/20 | 15.0% | +1.94% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.98% | **+0.64%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.87% | **+0.48%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$622.98** / 初期 $100.00 (+522.98%)
- 確定: 3934件 (Win 1230 / Loss 1283 / Flat 1421) / skip 3772件
- 成長率目線: 平均log +0.000465 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.32% 残高後 $622.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 3043件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.08** / 初期 $100.00 (+18.08%)
- 確定: 1297件 (Win 403 / Loss 501 / Flat 393) / pending 3件 / skip 1315件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000281 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TST/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.08

## 6. Latest Market Context

- 更新: 2026-08-10T09:36:16.232638+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=65110.4
- Funnel: target 958 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +45.97% | $2,765,311.69 |
| LONGXIA/USDT:USDT | +44.05% | $1,089,423.04 |
| GRVT/USDT:USDT | +28.39% | $3,649,014.79 |
| BMT/USDT:USDT | +16.43% | $21,691,023.49 |
| CAP/USDT:USDT | +15.99% | $6,615,440.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RE/USDT:USDT | below_1h_threshold | +3.71% | +3.88% |
| USOIL/USDT:USDT | below_1h_threshold | +1.10% | +1.27% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.92% | +1.09% |
| JTO/USDT:USDT | below_1h_threshold | +0.58% | +0.75% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.55% | +0.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
