# Decision Report

- generated_at: 2026-08-10T02:11:14.331924+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11112**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.70% / filled 20/20。**
- 全期間 MARKET基準: n=11112, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.37% | **+2.25%** |
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.88% | **+1.50%** |
| LIMIT_BB3S | 3/16 | 18.8% | +2.32% | **+0.43%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.63% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +1.96% | **+1.17%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.39% | **+0.83%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.41% | **+0.33%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.37% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$624.97** / 初期 $100.00 (+524.97%)
- 確定: 3933件 (Win 1230 / Loss 1282 / Flat 1421) / skip 3740件
- 成長率目線: 平均log +0.000466 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $624.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 3010件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.30** / 初期 $100.00 (+17.30%)
- 確定: 1283件 (Win 397 / Loss 493 / Flat 393) / pending 0件 / skip 1300件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000125 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` EXPIRED account +0.20% 残高後 $117.30

## 6. Latest Market Context

- 更新: 2026-08-10T02:11:06.081439+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=65094.0
- Funnel: target 961 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BMT/USDT:USDT | +57.83% | $18,521,895.22 |
| TUT/USDT:USDT | +38.11% | $82,815,892.90 |
| TST/USDT:USDT | +18.93% | $3,225,862.35 |
| CAP/USDT:USDT | +14.75% | $2,168,864.04 |
| COOKIE/USDT:USDT | +12.44% | $6,657,936.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +1.53% | +1.65% |
| NIL/USDT:USDT | below_1h_threshold | +1.33% | +1.45% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.08% | +1.20% |
| KAITO/USDT:USDT | below_1h_threshold | +1.05% | +1.17% |
| RE/USDT:USDT | below_1h_threshold | +0.89% | +1.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
