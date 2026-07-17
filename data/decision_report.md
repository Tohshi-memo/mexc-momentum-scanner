# Decision Report

- generated_at: 2026-07-17T10:31:13.864284+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8841**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=8841, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/13 | 30.8% | +3.64% | **+1.12%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.87% | **+0.93%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.77% | **+0.71%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.30% | **+0.91%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.12% | **+0.90%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.34% | **+0.29%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$111.81** / 初期 $100.00 (+11.81%)
- 確定トレード: 111件 (TP 42 / SL 65 / EXP 4)
- 最新: DODO/USDT:USDT TP_HIT PnL +8.00% 残高後 $111.81
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$344.46** / 初期 $100.00 (+244.46%)
- 確定: 2956件 (Win 922 / Loss 947 / Flat 1087) / skip 2446件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XEC/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $344.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.33** / 初期 $100.00 (+8.33%)
- 確定: 803件 (Win 189 / Loss 171 / Flat 443) / skip 1449件
- 成長率目線: 平均log +0.000100 / 幾何平均 +0.010% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0348 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $108.33

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.20** / 初期 $100.00 (-1.80%)
- 確定: 108件 (Win 34 / Loss 70 / Flat 4) / pending 2件 / skip 200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000218 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.20

## 6. Latest Market Context

- 更新: 2026-07-17T10:31:07.177852+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=63054.5
- Funnel: target 885 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +29.38% | $6,818,217.79 |
| XEC/USDT:USDT | +29.08% | $1,441,231.73 |
| LUMIA/USDT:USDT | +21.87% | $2,634,367.63 |
| AKE/USDT:USDT | +18.24% | $42,323,099.79 |
| KAITO/USDT:USDT | +15.70% | $4,500,755.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +2.63% | +2.48% |
| RIVER/USDT:USDT | below_1h_threshold | +1.92% | +1.77% |
| MYX/USDT:USDT | below_1h_threshold | +1.71% | +1.56% |
| VELVET/USDT:USDT | below_1h_threshold | +1.70% | +1.55% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.42% | +1.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
