# Decision Report

- generated_at: 2026-08-25T12:21:27.140776+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12599**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=12599, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.46% | **+0.41%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.21% | **+0.06%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.06% | **+0.04%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.56% | **+1.01%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.36% | **+0.68%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.93% | **+0.65%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.00% | **+0.45%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.55% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$697.77** / 初期 $100.00 (+597.77%)
- 確定: 4579件 (Win 1392 / Loss 1503 / Flat 1684) / skip 4581件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $697.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4033件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.06** / 初期 $100.00 (+15.06%)
- 確定: 1927件 (Win 564 / Loss 734 / Flat 629) / pending 6件 / skip 2141件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000041 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.06

## 6. Latest Market Context

- 更新: 2026-08-25T12:21:16.724155+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=78892.8
- Funnel: target 1023 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +90.15% | $4,964,547.90 |
| JIMOTHY/USDT:USDT | +65.85% | $1,694,359.02 |
| ONG/USDT:USDT | +34.13% | $8,973,506.25 |
| TAC/USDT:USDT | +31.20% | $6,790,818.34 |
| BR/USDT:USDT | +16.30% | $3,638,391.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROM/USDT:USDT | below_1h_threshold | +3.32% | +3.58% |
| COW/USDT:USDT | below_1h_threshold | +2.67% | +2.93% |
| CASHCAT/USDT:USDT | below_1h_threshold | +2.59% | +2.85% |
| HOLO/USDT:USDT | below_1h_threshold | +1.12% | +1.38% |
| STORJ/USDT:USDT | below_1h_threshold | +0.97% | +1.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
