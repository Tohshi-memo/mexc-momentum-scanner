# Decision Report

- generated_at: 2026-07-27T06:56:21.008901+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9612**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9612, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 6/20 | 30.0% | +3.58% | **+1.07%** |
| LIMIT_9PCT | 6/20 | 30.0% | +1.43% | **+0.43%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.46% | **+0.37%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.42% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +2.96% | **+2.52%** |
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +2.54% | **+2.28%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +2.40% | **+1.80%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +3.39% | **+1.69%** |
| LIMIT_BB3S_LONG | 11/14 | 78.6% | +1.87% | **+1.47%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$454.96** / 初期 $100.00 (+354.96%)
- 確定: 3408件 (Win 1081 / Loss 1110 / Flat 1217) / skip 2765件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $454.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1800件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.81** / 初期 $100.00 (+7.81%)
- 確定: 637件 (Win 211 / Loss 243 / Flat 183) / pending 5件 / skip 443件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000081 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $107.81

## 6. Latest Market Context

- 更新: 2026-07-27T06:56:10.705794+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=65388.9
- Funnel: target 903 → liquid 148 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.6 >= 65=1, 4h RSI 77.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +43.86% | $31,453,837.23 |
| BTW/USDT:USDT | +28.88% | $1,597,610.89 |
| ON/USDT:USDT | +22.60% | $3,849,828.36 |
| DIA/USDT:USDT | +20.66% | $7,961,402.81 |
| NIL/USDT:USDT | +14.21% | $1,679,935.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +4.88% | +4.95% |
| LDO/USDT:USDT | below_1h_threshold | +2.84% | +2.91% |
| US/USDT:USDT | below_1h_threshold | +2.83% | +2.90% |
| DIA/USDT:USDT | below_1h_threshold | +1.62% | +1.69% |
| ENA/USDT:USDT | below_1h_threshold | +1.03% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
