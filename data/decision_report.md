# Decision Report

- generated_at: 2026-05-08T14:02:39.998845+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3788**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.53% / filled 20/20。**
- 全期間 MARKET基準: n=3788, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+1.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.53% | **+1.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.65% | **+1.65%** |
| MARKET | 20/20 | 100.0% | +1.53% | **+1.53%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.59% | **+0.87%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +5.23% | **+5.23%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.99% | **+0.54%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 158件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T14:02:36.982802+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=79703.7
- Funnel: target 773 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHAROS/USDT:USDT | +50.91% | $12,265,403.82 |
| BSB/USDT:USDT | +45.67% | $12,555,977.35 |
| PLAY/USDT:USDT | +38.76% | $12,220,303.56 |
| COLLECT/USDT:USDT | +31.31% | $1,140,195.23 |
| AGT/USDT:USDT | +28.53% | $5,889,982.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +2.69% | +2.57% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +1.74% | +1.63% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +1.68% | +1.57% |
| PLAY/USDT:USDT | below_1h_threshold | +1.30% | +1.19% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.18% | +1.07% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
