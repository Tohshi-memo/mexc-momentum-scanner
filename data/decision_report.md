# Decision Report

- generated_at: 2026-07-11T13:11:10.325389+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8534**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.59% / filled 20/20。**
- 全期間 MARKET基準: n=8534, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.59% | **+1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.59% | **+1.59%** |
| ASK | 17/17 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.50% | **+1.13%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.82% | **+1.00%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.45% | **+0.87%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | -1.33% | **-0.40%** |
| MARKET_LONG | 20/20 | 100.0% | -0.41% | **-0.41%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | -1.11% | **-0.56%** |

## 2. $100 Live Portfolio

- 残高: **$104.09** / 初期 $100.00 (+4.09%)
- 確定トレード: 83件 (TP 30 / SL 52 / EXP 1)
- 最新: NES/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$317.94** / 初期 $100.00 (+217.94%)
- 確定: 2722件 (Win 861 / Loss 914 / Flat 947) / skip 2373件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $317.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1303件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.65** / 初期 $100.00 (-0.35%)
- 確定: 2件 (Win 0 / Loss 2 / Flat 0) / pending 2件 / skip 0件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000246 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $99.65

## 6. Latest Market Context

- 更新: 2026-07-11T13:11:04.272720+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64147.4
- Funnel: target 863 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| T/USDT:USDT | +28.69% | $1,849,715.39 |
| CLO/USDT:USDT | +25.14% | $1,067,597.50 |
| BEAT/USDT:USDT | +18.71% | $33,894,257.99 |
| HMSTR/USDT:USDT | +17.64% | $1,567,193.76 |
| ANSEM/USDT:USDT | +17.44% | $7,171,068.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| T/USDT:USDT | below_1h_threshold | +2.09% | +2.13% |
| CLO/USDT:USDT | below_1h_threshold | +2.05% | +2.09% |
| THETA/USDT:USDT | below_1h_threshold | +1.02% | +1.05% |
| MMT/USDT:USDT | below_1h_threshold | +0.75% | +0.78% |
| VET/USDT:USDT | below_1h_threshold | +0.71% | +0.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
