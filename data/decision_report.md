# Decision Report

- generated_at: 2026-08-10T02:56:21.510879+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11113**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.30% / filled 20/20。**
- 全期間 MARKET基準: n=11113, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.30% | **+2.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +3.00% | **+2.85%** |
| MARKET | 20/20 | 100.0% | +2.30% | **+2.30%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.50% | **+2.00%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.77% | **+0.46%** |
| LIMIT_BB3S | 3/16 | 18.8% | +2.32% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +2.42% | **+1.57%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.89% | **+1.23%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.86% | **+0.73%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.24% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$624.97** / 初期 $100.00 (+524.97%)
- 確定: 3933件 (Win 1230 / Loss 1282 / Flat 1421) / skip 3741件
- 成長率目線: 平均log +0.000466 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $624.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 3011件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.30** / 初期 $100.00 (+17.30%)
- 確定: 1283件 (Win 397 / Loss 493 / Flat 393) / pending 0件 / skip 1301件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000088 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` EXPIRED account +0.20% 残高後 $117.30

## 6. Latest Market Context

- 更新: 2026-08-10T02:56:13.367736+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=65080.0
- Funnel: target 961 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BMT/USDT:USDT | +51.03% | $18,937,946.28 |
| TUT/USDT:USDT | +33.81% | $83,507,363.06 |
| CAP/USDT:USDT | +23.24% | $2,473,938.32 |
| NIL/USDT:USDT | +17.14% | $2,203,970.01 |
| TST/USDT:USDT | +12.90% | $3,277,525.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BMT/USDT:USDT | below_1h_threshold | +4.51% | +4.65% |
| CAP/USDT:USDT | below_1h_threshold | +4.14% | +4.28% |
| CASHCAT/USDT:USDT | below_1h_threshold | +3.56% | +3.70% |
| KAITO/USDT:USDT | below_1h_threshold | +2.56% | +2.70% |
| ON/USDT:USDT | below_1h_threshold | +2.34% | +2.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
