# Decision Report

- generated_at: 2026-08-23T01:01:25.123959+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12429**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.33% / filled 20/20。**
- 全期間 MARKET基準: n=12429, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.33% | **+0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.46% | **+0.95%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.30% | **+0.83%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.62% | **+0.59%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| MARKET | 20/20 | 100.0% | +0.33% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +8.00% | **+4.00%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.81% | **+1.27%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.58% | **+1.03%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.10% | **+0.82%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.87% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$702.69** / 初期 $100.00 (+602.69%)
- 確定: 4458件 (Win 1365 / Loss 1457 / Flat 1636) / skip 4532件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $702.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1935件 (Win 533 / Loss 465 / Flat 937) / skip 3905件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.84** / 初期 $100.00 (+16.84%)
- 確定: 1863件 (Win 549 / Loss 706 / Flat 608) / pending 0件 / skip 2039件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000130 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.84

## 6. Latest Market Context

- 更新: 2026-08-23T01:01:15.051201+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=77273.1
- Funnel: target 1018 → liquid 207 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +38.19% | $12,491,249.21 |
| TUT/USDT:USDT | +35.09% | $42,553,941.21 |
| ZRO/USDT:USDT | +14.91% | $8,830,743.06 |
| UAI/USDT:USDT | +14.22% | $3,070,863.64 |
| STX/USDT:USDT | +13.46% | $9,879,756.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPK/USDT:USDT | below_1h_threshold | +0.61% | +0.66% |
| VET/USDT:USDT | below_1h_threshold | +0.31% | +0.36% |
| CATE/USDT:USDT | below_1h_threshold | +0.31% | +0.36% |
| TRIA/USDT:USDT | below_1h_threshold | +0.31% | +0.35% |
| ARX/USDT:USDT | below_1h_threshold | +0.24% | +0.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
