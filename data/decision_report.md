# Decision Report

- generated_at: 2026-06-13T02:21:32.978493+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6557**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.25% / filled 20/20。**
- 全期間 MARKET基準: n=6557, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+3.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.25% | **+3.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.25% | **+3.25%** |
| ASK | 20/20 | 100.0% | +2.71% | **+2.71%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.98% | **+1.38%** |
| LIMIT_ATR | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_2PCT | 11/20 | 55.0% | +1.35% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +4.22% | **+1.05%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -0.97% | **-0.29%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -1.61% | **-0.88%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.48** / 初期 $100.00 (+64.48%)
- 確定: 1430件 (Win 389 / Loss 464 / Flat 577) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VVV/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $164.48

## 4. Latest Market Context

- 更新: 2026-06-13T02:21:30.276741+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=63720.0
- Funnel: target 774 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDGE/USDT:USDT | +19.91% | $1,376,071.55 |
| H/USDT:USDT | +15.76% | $26,286,006.86 |
| SQD/USDT:USDT | +15.42% | $1,045,816.66 |
| RIF/USDT:USDT | +14.03% | $1,283,429.94 |
| VVV/USDT:USDT | +10.97% | $3,990,733.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +3.54% | +3.66% |
| VVV/USDT:USDT | below_1h_threshold | +3.06% | +3.18% |
| COAI/USDT:USDT | below_1h_threshold | +2.27% | +2.40% |
| HOME/USDT:USDT | below_1h_threshold | +1.36% | +1.49% |
| SQD/USDT:USDT | below_1h_threshold | +1.29% | +1.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
