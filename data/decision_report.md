# Decision Report

- generated_at: 2026-07-26T12:31:13.104376+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9573**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=9573, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.35% | **+1.28%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.06% | **+0.79%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.17% | **+0.76%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.51% | **+0.63%** |
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.94% | **+5.94%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.66% | **+0.75%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.73% | **+0.44%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.60% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$454.84** / 初期 $100.00 (+354.84%)
- 確定: 3398件 (Win 1078 / Loss 1105 / Flat 1215) / skip 2736件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DIA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $454.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.72** / 初期 $100.00 (+37.72%)
- 確定: 1222件 (Win 338 / Loss 274 / Flat 610) / skip 1762件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.28** / 初期 $100.00 (+8.28%)
- 確定: 614件 (Win 206 / Loss 237 / Flat 171) / pending 2件 / skip 427件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000274 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $108.28

## 6. Latest Market Context

- 更新: 2026-07-26T12:31:06.366602+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64541.0
- Funnel: target 898 → liquid 119 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +71.48% | $39,501,808.35 |
| DIA/USDT:USDT | +48.53% | $3,978,453.65 |
| PIEVERSE/USDT:USDT | +35.65% | $5,906,038.47 |
| BANK/USDT:USDT | +25.44% | $90,390,024.44 |
| KAITO/USDT:USDT | +24.71% | $5,882,202.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DIA/USDT:USDT | below_1h_threshold | +3.22% | +3.13% |
| UNI/USDT:USDT | below_1h_threshold | +1.51% | +1.42% |
| APT/USDT:USDT | below_1h_threshold | +1.37% | +1.28% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.03% | +0.94% |
| BOME/USDT:USDT | below_1h_threshold | +0.92% | +0.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
