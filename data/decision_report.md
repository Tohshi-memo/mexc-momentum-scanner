# Decision Report

- generated_at: 2026-07-22T02:21:24.048729+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9232**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9232, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.12% | **-1.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.55% | **+1.09%** |
| LIMIT_5PCT | 12/20 | 60.0% | +0.89% | **+0.53%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.98% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.60% | **+2.16%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.97% | **+1.87%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.47% | **+1.85%** |
| MARKET_LONG | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3250件 (Win 1021 / Loss 1039 / Flat 1190) / skip 2543件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1484件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定: 377件 (Win 125 / Loss 157 / Flat 95) / pending 5件 / skip 325件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000124 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_7PCT` SL_HIT account -0.17% 残高後 $100.99

## 6. Latest Market Context

- 更新: 2026-07-22T02:21:15.761701+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=66417.1
- Funnel: target 885 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +47.73% | $4,005,622.05 |
| PONS/USDT:USDT | +23.61% | $2,088,733.86 |
| SMCISTOCK/USDT:USDT | +19.30% | $3,632,105.13 |
| FWDISTOCK/USDT:USDT | +13.09% | $3,947,956.83 |
| RE/USDT:USDT | +12.44% | $1,513,447.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRAM/USDT:USDT | below_1h_threshold | +2.63% | +2.61% |
| FWDISTOCK/USDT:USDT | below_1h_threshold | +1.97% | +1.94% |
| BNCSTOCK/USDT:USDT | below_1h_threshold | +1.81% | +1.78% |
| LAB/USDT:USDT | below_1h_threshold | +1.79% | +1.76% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
