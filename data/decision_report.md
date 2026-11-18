# Decision Report

- generated_at: 2026-11-18T19:11:36.610174+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19162**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=19162, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +0.71% | **+0.50%** |
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.48% | **+0.38%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.35% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.63% | **+1.09%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.01% | **+0.45%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.50% | **+0.30%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.40% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,685.66** / 初期 $100.00 (+1585.66%)
- 確定: 7355件 (Win 2110 / Loss 2359 / Flat 2886) / skip 8368件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIPPIN/USDT:USDT `MARKET` TP_HIT account +1.00% 残高後 $1,685.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.70** / 初期 $100.00 (+330.70%)
- 確定: 5014件 (Win 1335 / Loss 1087 / Flat 2592) / skip 7559件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0359 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIPPIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $430.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7324件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000155 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-18T19:11:27.071843+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.66% price=62735.0
- Funnel: target 1080 → liquid 143 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HUMA/USDT:USDT | +14.65% | $1,744,635.59 |
| PIPPIN/USDT:USDT | +10.94% | $5,236,011.94 |
| ARIA/USDT:USDT | +7.29% | $3,989,640.29 |
| EVAA/USDT:USDT | +6.79% | $12,811,667.66 |
| BLESS/USDT:USDT | +6.05% | $20,972,956.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +1.89% | +2.55% |
| ARIA/USDT:USDT | below_1h_threshold | +1.82% | +2.48% |
| PLTRSTOCK/USDT:USDT | below_1h_threshold | +1.78% | +2.44% |
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +1.04% | +1.70% |
| TQQQ/USDT:USDT | below_1h_threshold | +1.03% | +1.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
