# Decision Report

- generated_at: 2026-06-01T06:03:43.071001+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5277**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.55% / filled 20/20。**
- 全期間 MARKET基準: n=5277, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.55% | **+2.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.87% | **+2.87%** |
| MARKET | 20/20 | 100.0% | +2.55% | **+2.55%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.14% | **+1.71%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.25% | **+1.46%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.64% | **+1.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.23% | **+0.74%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.18% | **+0.11%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.31% | **-0.15%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.40% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 944件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T06:03:40.775140+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=73308.2
- Funnel: target 778 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +162.17% | $30,788,707.28 |
| SLX/USDT:USDT | +112.92% | $1,041,707.29 |
| H/USDT:USDT | +60.39% | $23,529,104.48 |
| HOME/USDT:USDT | +37.51% | $4,468,307.17 |
| FHE/USDT:USDT | +27.66% | $1,241,189.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +4.17% | +4.18% |
| HOME/USDT:USDT | below_1h_threshold | +1.92% | +1.93% |
| H/USDT:USDT | below_1h_threshold | +1.77% | +1.79% |
| PLAY/USDT:USDT | below_1h_threshold | +1.75% | +1.76% |
| STG/USDT:USDT | below_1h_threshold | +1.07% | +1.08% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
