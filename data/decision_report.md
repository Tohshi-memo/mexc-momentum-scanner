# Decision Report

- generated_at: 2026-06-25T17:21:29.573989+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7576**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.75% / filled 20/20。**
- 全期間 MARKET基準: n=7576, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+3.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.75% | **+3.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.75% | **+3.75%** |
| ASK | 20/20 | 100.0% | +3.62% | **+3.62%** |
| LIMIT_BB3S | 6/13 | 46.2% | +3.93% | **+1.81%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.36% | **+0.47%** |
| LIMIT_8PCT_LONG | 14/20 | 70.0% | +0.37% | **+0.26%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -0.00% | **-0.00%** |
| LIMIT_7PCT_LONG | 14/20 | 70.0% | -1.41% | **-0.99%** |

## 2. $100 Live Portfolio

- 残高: **$102.94** / 初期 $100.00 (+2.94%)
- 確定トレード: 39件 (TP 15 / SL 24 / EXP 0)
- 最新: MUSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.24** / 初期 $100.00 (+119.24%)
- 確定: 2132件 (Win 629 / Loss 715 / Flat 788) / skip 2005件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $219.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定: 369件 (Win 102 / Loss 100 / Flat 167) / skip 618件
- 成長率目線: 平均log +0.000196 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0475 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $107.51

## 5. Latest Market Context

- 更新: 2026-06-25T17:21:24.332738+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=59461.8
- Funnel: target 807 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VVV/USDT:USDT | +8.71% | $2,994,857.52 |
| BEAT/USDT:USDT | +8.22% | $33,010,318.27 |
| HEI/USDT:USDT | +7.42% | $4,009,723.01 |
| ARX/USDT:USDT | +4.71% | $2,612,278.92 |
| AXTISTOCK/USDT:USDT | +4.34% | $4,186,204.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AAVE/USDT:USDT | below_1h_threshold | +3.71% | +3.41% |
| VVV/USDT:USDT | below_1h_threshold | +3.06% | +2.76% |
| BEAT/USDT:USDT | below_1h_threshold | +2.26% | +1.96% |
| DOGE/USDT:USDT | below_1h_threshold | +1.85% | +1.55% |
| APT/USDT:USDT | below_1h_threshold | +1.69% | +1.39% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
