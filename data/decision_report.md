# Decision Report

- generated_at: 2026-05-16T22:48:22.054376+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4370**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.78% / filled 20/20。**
- 全期間 MARKET基準: n=4370, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.78% | **+1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.78% | **+1.78%** |
| ASK | 20/20 | 100.0% | +1.76% | **+1.76%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.21% | **+0.85%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.89% | **+0.49%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.64% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +1.42% | **+0.85%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.30% | **+0.32%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.30% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$97.20** / 初期 $100.00 (-2.80%)
- 確定トレード: 47件 (TP 12 / SL 32 / EXP 3)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.20
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 392件 (Win 97 / Loss 136 / Flat 159) / skip 539件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-16T22:48:18.767765+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=78177.7
- Funnel: target 760 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LYN/USDT:USDT | +11.52% | $1,539,788.89 |
| BSB/USDT:USDT | +9.61% | $3,514,353.52 |
| LUNC/USDT:USDT | +7.90% | $11,443,665.67 |
| NMR/USDT:USDT | +6.77% | $1,169,895.95 |
| ASTEROID/USDT:USDT | +6.22% | $4,564,509.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LUNC/USDT:USDT | below_1h_threshold | +2.80% | +2.86% |
| CSCOSTOCK/USDT:USDT | below_1h_threshold | +1.14% | +1.21% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +0.95% | +1.01% |
| LYN/USDT:USDT | below_1h_threshold | +0.91% | +0.97% |
| CGPT/USDT:USDT | below_1h_threshold | +0.74% | +0.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
