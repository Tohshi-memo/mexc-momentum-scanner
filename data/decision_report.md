# Decision Report

- generated_at: 2026-11-19T02:01:23.161760+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19174**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.69% / filled 20/20。**
- 全期間 MARKET基準: n=19174, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.81% | **+1.72%** |
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.73% | **+1.47%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.62% | **+1.14%** |
| LIMIT_BB3S | 5/14 | 35.7% | +2.93% | **+1.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +2.01% | **+1.00%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.43% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,719.29** / 初期 $100.00 (+1619.29%)
- 確定: 7363件 (Win 2114 / Loss 2363 / Flat 2886) / skip 8372件
- 成長率目線: 平均log +0.000386 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,719.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.70** / 初期 $100.00 (+330.70%)
- 確定: 5022件 (Win 1335 / Loss 1087 / Flat 2600) / skip 7563件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $430.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7333件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000284 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-19T02:01:09.567209+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=62756.3
- Funnel: target 1079 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +37.39% | $6,493,603.28 |
| HUMA/USDT:USDT | +19.42% | $2,457,824.56 |
| VELVET/USDT:USDT | +19.01% | $4,030,982.14 |
| PHAROS/USDT:USDT | +16.24% | $1,977,009.45 |
| LUNC/USDT:USDT | +13.84% | $1,753,141.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HUMA/USDT:USDT | below_1h_threshold | +1.22% | +1.32% |
| EVAA/USDT:USDT | below_1h_threshold | +1.12% | +1.21% |
| PHAROS/USDT:USDT | below_1h_threshold | +0.15% | +0.25% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +0.10% | +0.20% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.08% | +0.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
