# Decision Report

- generated_at: 2026-10-09T17:41:16.609429+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16442**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16442, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.65% | **+0.61%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.64% | **+0.51%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_BB3S | 7/15 | 46.7% | +0.35% | **+0.16%** |
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.78% | **+0.97%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.85% | **+0.68%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$121.24** / 初期 $100.00 (+21.24%)
- 確定トレード: 236件 (TP 87 / SL 142 / EXP 7)
- 最新: STRK/USDT:USDT SL_HIT PnL -3.05% 残高後 $121.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,309.24** / 初期 $100.00 (+1209.24%)
- 確定: 6284件 (Win 1845 / Loss 2013 / Flat 2426) / skip 6719件
- 成長率目線: 平均log +0.000409 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MRNASTOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $1,309.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3635件 (Win 1010 / Loss 853 / Flat 1772) / skip 6218件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGIC/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4604件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000089 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-09T17:41:05.126485+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=82640.3
- Funnel: target 1089 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGIC/USDT:USDT | +17.42% | $2,871,575.59 |
| BAT/USDT:USDT | +10.11% | $4,733,635.74 |
| LPT/USDT:USDT | +5.29% | $1,011,197.62 |
| UAI/USDT:USDT | +4.59% | $2,059,591.60 |
| CT/USDT:USDT | +3.88% | $1,811,220.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAT/USDT:USDT | below_1h_threshold | +4.42% | +4.50% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +2.54% | +2.62% |
| MAGIC/USDT:USDT | below_1h_threshold | +2.40% | +2.49% |
| ZRX/USDT:USDT | below_1h_threshold | +1.52% | +1.60% |
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +1.50% | +1.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
