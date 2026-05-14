# Decision Report

- generated_at: 2026-05-14T23:45:58.469058+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4312**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.96% / filled 20/20。**
- 全期間 MARKET基準: n=4312, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+0.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.96% | **+0.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/13 | 38.5% | +4.35% | **+1.67%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.36% | **+1.09%** |
| ASK | 20/20 | 100.0% | +1.02% | **+1.02%** |
| MARKET | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.64% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.75% | **+1.25%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +2.68% | **+0.67%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.48** / 初期 $100.00 (+20.48%)
- 確定: 365件 (Win 96 / Loss 129 / Flat 140) / skip 508件
- 成長率目線: 平均log +0.000511 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $120.48

## 4. Latest Market Context

- 更新: 2026-05-14T23:45:55.482730+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=81177.2
- Funnel: target 759 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UP/USDT:USDT | +20.27% | $3,750,258.91 |
| TAC/USDT:USDT | +18.98% | $1,807,053.66 |
| FIGSTOCK/USDT:USDT | +14.60% | $2,979,193.30 |
| NAORIS/USDT:USDT | +8.03% | $2,792,723.29 |
| ASTEROID/USDT:USDT | +7.93% | $1,054,838.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.07% | +3.37% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.48% | +1.77% |
| CFX/USDT:USDT | below_1h_threshold | +1.38% | +1.68% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.02% | +1.31% |
| NAORIS/USDT:USDT | below_1h_threshold | +0.82% | +1.11% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
