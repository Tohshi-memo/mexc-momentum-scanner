# Decision Report

- generated_at: 2026-07-23T13:11:12.537555+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9366**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.83% / filled 20/20。**
- 全期間 MARKET基準: n=9366, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.11% | **+1.90%** |
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_3PCT | 14/20 | 70.0% | +2.02% | **+1.41%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.39% | **+1.11%** |
| LIMIT_BB3S | 4/18 | 22.2% | +3.35% | **+0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.01% | **+0.25%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.20% | **+0.15%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.12% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$426.05** / 初期 $100.00 (+326.05%)
- 確定: 3321件 (Win 1048 / Loss 1075 / Flat 1198) / skip 2606件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $426.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1162件 (Win 312 / Loss 254 / Flat 596) / skip 1615件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0252 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BROCCOLIF3B/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 432件 (Win 143 / Loss 180 / Flat 109) / pending 2件 / skip 401件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000115 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $100.91

## 6. Latest Market Context

- 更新: 2026-07-23T13:11:07.164108+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=65000.6
- Funnel: target 897 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +42.53% | $5,995,046.18 |
| BANK/USDT:USDT | +38.65% | $107,893,515.32 |
| JIMOTHY/USDT:USDT | +28.64% | $5,650,355.74 |
| ZAMA/USDT:USDT | +27.78% | $6,846,012.01 |
| ON/USDT:USDT | +21.10% | $5,489,206.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +2.58% | +2.79% |
| ALLO/USDT:USDT | below_1h_threshold | +1.68% | +1.89% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.36% | +1.58% |
| POPMARTSTOCK/USDT:USDT | below_1h_threshold | +1.11% | +1.33% |
| NGAS/USDT:USDT | below_1h_threshold | +0.89% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
