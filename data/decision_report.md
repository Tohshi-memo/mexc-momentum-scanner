# Decision Report

- generated_at: 2026-07-03T03:26:03.978658+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8127**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.09% / filled 20/20。**
- 全期間 MARKET基準: n=8127, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +1.48% | **+1.11%** |
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |
| ASK | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.26% | **+0.49%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.31% | **+0.28%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.14% | **+0.08%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | -0.24% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$102.62** / 初期 $100.00 (+2.62%)
- 確定トレード: 53件 (TP 19 / SL 33 / EXP 1)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.62
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$285.42** / 初期 $100.00 (+185.42%)
- 確定: 2449件 (Win 755 / Loss 817 / Flat 877) / skip 2239件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $285.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.81** / 初期 $100.00 (+5.81%)
- 確定: 581件 (Win 141 / Loss 138 / Flat 302) / skip 957件
- 成長率目線: 平均log +0.000097 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0378 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NES/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +0.69% 残高後 $105.81

## 5. Latest Market Context

- 更新: 2026-07-03T03:25:58.031503+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=61553.7
- Funnel: target 834 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZKP/USDT:USDT | +31.85% | $1,096,574.73 |
| RIF/USDT:USDT | +30.79% | $5,402,543.66 |
| MAGMA/USDT:USDT | +22.99% | $5,411,356.46 |
| THE/USDT:USDT | +22.83% | $2,100,480.90 |
| PIPPIN/USDT:USDT | +21.97% | $7,527,948.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +4.57% | +4.34% |
| ALLO/USDT:USDT | below_1h_threshold | +1.98% | +1.75% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.88% | +1.65% |
| ZKP/USDT:USDT | below_1h_threshold | +1.67% | +1.44% |
| BEAT/USDT:USDT | below_1h_threshold | +1.35% | +1.12% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
