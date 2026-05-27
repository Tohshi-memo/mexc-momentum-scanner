# Decision Report

- generated_at: 2026-05-27T04:04:38.602248+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4916**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.54% / filled 20/20。**
- 全期間 MARKET基準: n=4916, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.61% | **+0.61%** |
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.27% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.16% | **+1.04%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.16% | **+0.75%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.21% | **+0.67%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.77% | **+0.50%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.70% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.71** / 初期 $100.00 (+28.71%)
- 確定: 680件 (Win 172 / Loss 217 / Flat 291) / skip 797件
- 成長率目線: 平均log +0.000371 / 幾何平均 +0.037% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DRIFT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $128.71

## 4. Latest Market Context

- 更新: 2026-05-27T04:04:36.152150+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=75629.7
- Funnel: target 770 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| REQ/USDT:USDT | +18.99% | $1,192,852.12 |
| LUNC/USDT:USDT | +11.32% | $8,289,532.49 |
| GUA/USDT:USDT | +10.76% | $3,466,532.53 |
| PLAY/USDT:USDT | +9.39% | $7,934,871.93 |
| MRVLSTOCK/USDT:USDT | +7.00% | $1,215,793.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| REQ/USDT:USDT | below_1h_threshold | +3.67% | +3.68% |
| LUNC/USDT:USDT | below_1h_threshold | +0.70% | +0.71% |
| PLAY/USDT:USDT | below_1h_threshold | +0.35% | +0.36% |
| SEI/USDT:USDT | below_1h_threshold | +0.30% | +0.31% |
| CHIP/USDT:USDT | below_1h_threshold | +0.18% | +0.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
