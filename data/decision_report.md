# Decision Report

- generated_at: 2026-06-09T02:10:28.041943+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6111**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.40% / filled 20/20。**
- 全期間 MARKET基準: n=6111, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.04% | **+0.73%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.49% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.25** / 初期 $100.00 (+54.25%)
- 確定: 1151件 (Win 285 / Loss 352 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000377 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $154.25

## 4. Latest Market Context

- 更新: 2026-06-09T02:10:25.136991+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=62807.8
- Funnel: target 777 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +20.47% | $23,621,344.93 |
| MOVE/USDT:USDT | +17.76% | $3,503,581.10 |
| SLX/USDT:USDT | +16.06% | $1,018,480.49 |
| 4/USDT:USDT | +4.70% | $1,656,971.12 |
| FOLKS/USDT:USDT | +4.65% | $1,443,444.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +1.28% | +1.16% |
| MOVE/USDT:USDT | below_1h_threshold | +1.06% | +0.94% |
| SLX/USDT:USDT | below_1h_threshold | +0.94% | +0.82% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.78% | +0.66% |
| GLWSTOCK/USDT:USDT | below_1h_threshold | +0.69% | +0.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
