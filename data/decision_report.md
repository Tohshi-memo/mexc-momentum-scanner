# Decision Report

- generated_at: 2026-05-08T15:12:43.863160+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3794**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=3794, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.49% | **+1.49%** |
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.89% | **+0.76%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.95% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.82% | **+1.82%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.36% | **+0.61%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.47% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 164件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T15:12:41.030641+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=79856.0
- Funnel: target 773 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +49.68% | $14,085,321.82 |
| PHAROS/USDT:USDT | +48.80% | $12,947,012.15 |
| PLAY/USDT:USDT | +35.75% | $14,007,603.40 |
| COLLECT/USDT:USDT | +32.87% | $1,286,021.99 |
| AGT/USDT:USDT | +30.09% | $5,965,856.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHAROS/USDT:USDT | below_1h_threshold | +3.43% | +3.76% |
| BILL/USDT:USDT | below_1h_threshold | +3.17% | +3.49% |
| STRK/USDT:USDT | below_1h_threshold | +1.85% | +2.18% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.35% | +1.67% |
| BSB/USDT:USDT | below_1h_threshold | +1.28% | +1.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
