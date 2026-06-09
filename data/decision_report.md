# Decision Report

- generated_at: 2026-06-09T14:17:31.770132+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6142**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.85% / filled 20/20。**
- 全期間 MARKET基準: n=6142, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.88% | **+1.88%** |
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.28% | **+1.82%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.62% | **+1.46%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.52% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.51% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.43% | **+0.21%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.14% | **+0.09%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.88** / 初期 $100.00 (+48.88%)
- 確定: 1182件 (Win 296 / Loss 371 / Flat 515) / skip 1521件
- 成長率目線: 平均log +0.000337 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $148.88

## 4. Latest Market Context

- 更新: 2026-06-09T14:17:29.774604+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.66% price=61833.2
- Funnel: target 774 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +46.24% | $23,760,388.36 |
| JCT/USDT:USDT | +32.46% | $1,358,076.29 |
| SLX/USDT:USDT | +27.57% | $5,739,609.45 |
| POWER/USDT:USDT | +21.84% | $4,357,898.99 |
| VELVET/USDT:USDT | +20.75% | $21,752,508.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POWER/USDT:USDT | below_1h_threshold | +3.45% | +4.11% |
| VELVET/USDT:USDT | below_1h_threshold | +2.05% | +2.71% |
| ALLO/USDT:USDT | below_1h_threshold | +0.57% | +1.23% |
| UAI/USDT:USDT | below_1h_threshold | +0.48% | +1.14% |
| NGAS/USDT:USDT | below_1h_threshold | +0.35% | +1.01% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
