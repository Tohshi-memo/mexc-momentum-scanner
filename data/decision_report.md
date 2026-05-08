# Decision Report

- generated_at: 2026-05-08T15:00:14.266974+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3793**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.51% / filled 20/20。**
- 全期間 MARKET基準: n=3793, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.63% | **+1.63%** |
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.06% | **+0.90%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +2.92% | **+2.92%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.43% | **+0.79%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.83% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 163件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T15:00:11.125494+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.63% price=80114.3
- Funnel: target 773 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +47.16% | $13,903,774.47 |
| PHAROS/USDT:USDT | +43.86% | $12,859,192.48 |
| PLAY/USDT:USDT | +34.16% | $14,020,165.94 |
| COLLECT/USDT:USDT | +33.20% | $1,267,026.07 |
| AGT/USDT:USDT | +29.32% | $5,963,338.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOT/USDT:USDT | below_relative_strength | +5.11% | +4.48% |
| TIA/USDT:USDT | below_1h_threshold | +4.16% | +3.53% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +2.93% | +2.30% |
| ONDO/USDT:USDT | below_1h_threshold | +2.87% | +2.24% |
| GALA/USDT:USDT | below_1h_threshold | +2.51% | +1.88% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
