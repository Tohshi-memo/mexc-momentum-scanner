# Decision Report

- generated_at: 2026-05-16T09:38:29.721111+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4367**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.87% / filled 20/20。**
- 全期間 MARKET基準: n=4367, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +1.64% | **+0.98%** |
| ASK | 20/20 | 100.0% | +0.90% | **+0.90%** |
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.02% | **+0.56%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.38% | **-0.08%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | -0.66% | **-0.36%** |

## 2. $100 Live Portfolio

- 残高: **$97.20** / 初期 $100.00 (-2.80%)
- 確定トレード: 47件 (TP 12 / SL 32 / EXP 3)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.20
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 391件 (Win 97 / Loss 136 / Flat 158) / skip 537件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account +0.00% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-16T09:38:26.347676+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=78070.7
- Funnel: target 760 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARCSOL/USDT:USDT | +31.47% | $2,267,616.85 |
| LAB/USDT:USDT | +18.19% | $107,298,190.75 |
| ASTEROID/USDT:USDT | +17.34% | $4,666,074.95 |
| GUA/USDT:USDT | +14.28% | $2,664,441.00 |
| TAC/USDT:USDT | +11.54% | $1,064,906.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FF/USDT:USDT | below_1h_threshold | +2.45% | +2.86% |
| LAB/USDT:USDT | below_1h_threshold | +1.58% | +1.98% |
| GUA/USDT:USDT | below_1h_threshold | +1.36% | +1.77% |
| CHZ/USDT:USDT | below_1h_threshold | +0.96% | +1.36% |
| INX/USDT:USDT | below_1h_threshold | +0.47% | +0.87% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
