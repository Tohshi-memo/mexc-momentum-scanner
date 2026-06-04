# Decision Report

- generated_at: 2026-06-04T01:13:05.491452+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5588**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.31% / filled 20/20。**
- 全期間 MARKET基準: n=5588, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.31% | **+2.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.33% | **+2.33%** |
| MARKET | 20/20 | 100.0% | +2.31% | **+2.31%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.31% | **+2.08%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.87% | **+1.31%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.99% | **+1.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +3.12% | **+1.56%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.59% | **+0.33%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.34% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$98.06** / 初期 $100.00 (-1.94%)
- 確定トレード: 93件 (TP 28 / SL 62 / EXP 3)
- 最新: XPL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.06
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1004件 (Win 239 / Loss 312 / Flat 453) / skip 1145件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T01:13:03.138229+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=63133.7
- Funnel: target 769 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +23.34% | $22,242,037.48 |
| STO/USDT:USDT | +18.72% | $6,676,792.16 |
| BP/USDT:USDT | +9.48% | $1,553,522.47 |
| MAGMA/USDT:USDT | +7.47% | $4,313,026.80 |
| EPIC/USDT:USDT | +7.41% | $3,536,370.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +0.88% | +1.16% |
| GUA/USDT:USDT | below_1h_threshold | +0.79% | +1.06% |
| ZORA/USDT:USDT | below_1h_threshold | +0.78% | +1.06% |
| XPT/USDT:USDT | below_1h_threshold | +0.73% | +1.01% |
| TESLA/USDT:USDT | below_1h_threshold | +0.71% | +0.99% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
