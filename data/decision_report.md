# Decision Report

- generated_at: 2026-09-21T10:46:33.100299+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15250**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=15250, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +1.75% | **+0.81%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.52% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +0.81% | **+0.40%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.23% | **+0.37%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.36% | **+0.18%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.22% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,174.95** / 初期 $100.00 (+1074.95%)
- 確定: 5741件 (Win 1710 / Loss 1846 / Flat 2185) / skip 6070件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,174.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.51** / 初期 $100.00 (+147.51%)
- 確定: 3312件 (Win 915 / Loss 765 / Flat 1632) / skip 5349件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0155 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $247.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.69** / 初期 $100.00 (+22.69%)
- 確定: 3028件 (Win 892 / Loss 1186 / Flat 950) / pending 6件 / skip 3690件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000114 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $122.69

## 6. Latest Market Context

- 更新: 2026-09-21T10:46:19.718093+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.49% price=84206.7
- Funnel: target 1050 → liquid 158 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.2 >= 65=1, 4h RSI 68.6 >= 65=1, 4h RSI 66.6 >= 65=1, 4h RSI 71.4 >= 65=1, 4h RSI 87.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZETA/USDT:USDT | +69.18% | $6,526,862.26 |
| PHA/USDT:USDT | +67.39% | $2,561,641.14 |
| NIL/USDT:USDT | +31.28% | $7,468,488.29 |
| PTB/USDT:USDT | +28.64% | $1,162,118.27 |
| UAI/USDT:USDT | +26.87% | $1,759,505.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.77% | +5.27% |
| ONDO/USDT:USDT | below_1h_threshold | +3.38% | +3.87% |
| ZRO/USDT:USDT | below_1h_threshold | +3.27% | +3.76% |
| ENA/USDT:USDT | below_1h_threshold | +3.01% | +3.50% |
| EVAA/USDT:USDT | below_1h_threshold | +2.68% | +3.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
