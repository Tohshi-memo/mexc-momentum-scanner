# Decision Report

- generated_at: 2026-06-06T07:08:22.536802+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5791**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.06% / filled 20/20。**
- 全期間 MARKET基準: n=5791, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.06% | **+3.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +3.10% | **+3.10%** |
| MARKET | 20/20 | 100.0% | +3.06% | **+3.06%** |
| LIMIT_BB3S | 4/18 | 22.2% | +2.00% | **+0.44%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.28% | **+0.10%** |
| LIMIT_5PCT | 3/20 | 15.0% | -0.70% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.45% | **+0.09%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.36% | **-0.20%** |
| LIMIT_6PCT_LONG | 14/20 | 70.0% | -0.60% | **-0.42%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1013件 (Win 239 / Loss 313 / Flat 461) / skip 1339件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T07:08:20.393538+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.33% price=60970.6
- Funnel: target 771 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +33.25% | $2,352,630.30 |
| CLO/USDT:USDT | +31.98% | $2,170,978.86 |
| ALLO/USDT:USDT | +27.07% | $9,896,877.94 |
| ZEST/USDT:USDT | +26.62% | $1,757,822.60 |
| OPN/USDT:USDT | +19.66% | $22,149,992.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEST/USDT:USDT | below_1h_threshold | +2.85% | +2.52% |
| VELVET/USDT:USDT | below_1h_threshold | +2.33% | +2.00% |
| JTO/USDT:USDT | below_1h_threshold | +1.74% | +1.41% |
| FET/USDT:USDT | below_1h_threshold | +1.55% | +1.21% |
| BEAT/USDT:USDT | below_1h_threshold | +1.53% | +1.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
