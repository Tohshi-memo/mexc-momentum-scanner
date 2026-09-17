# Decision Report

- generated_at: 2026-09-17T12:46:19.741510+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14794**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.93% / filled 20/20。**
- 全期間 MARKET基準: n=14794, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.93% | **+1.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.48% | **+2.35%** |
| MARKET | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.56% | **+0.28%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_BB3S | 2/19 | 10.5% | +2.00% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.00% | **+0.55%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.82% | **+0.45%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,165.60** / 初期 $100.00 (+1065.60%)
- 確定: 5601件 (Win 1679 / Loss 1813 / Flat 2109) / skip 5754件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,165.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$239.89** / 初期 $100.00 (+139.89%)
- 確定: 3130件 (Win 870 / Loss 747 / Flat 1513) / skip 5075件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $239.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2957件 (Win 878 / Loss 1165 / Flat 914) / pending 1件 / skip 3310件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-17T12:46:11.104088+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.50% price=76831.2
- Funnel: target 1050 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AVA/USDT:USDT | +90.32% | $3,200,813.34 |
| ONE/USDT:USDT | +68.65% | $11,088,048.79 |
| GENIUS/USDT:USDT | +28.80% | $1,161,118.32 |
| 4STOCK/USDT:USDT | +23.92% | $1,102,615.41 |
| BATON/USDT:USDT | +21.85% | $2,565,381.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POWER/USDT:USDT | below_1h_threshold | +4.37% | +3.87% |
| SYN/USDT:USDT | below_1h_threshold | +3.90% | +3.40% |
| ONE/USDT:USDT | below_1h_threshold | +3.69% | +3.19% |
| ETHFI/USDT:USDT | below_1h_threshold | +3.50% | +3.00% |
| BULLA/USDT:USDT | below_1h_threshold | +3.43% | +2.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
