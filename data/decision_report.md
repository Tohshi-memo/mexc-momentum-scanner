# Decision Report

- generated_at: 2026-05-21T03:53:50.049142+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4601**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.30% / filled 20/20。**
- 全期間 MARKET基準: n=4601, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+2.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.30% | **+2.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.30% | **+2.30%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.34% | **+1.87%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.43% | **+1.83%** |
| ASK | 20/20 | 100.0% | +1.71% | **+1.71%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.34% | **+0.87%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +2.22% | **+1.33%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +1.78% | **+1.07%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.07% | **+0.69%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.27% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 545件 (Win 138 / Loss 185 / Flat 222) / skip 617件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T03:53:47.278781+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=77999.9
- Funnel: target 765 → liquid 129 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.2 >= 65=1, 4h RSI 66.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +63.50% | $1,366,499.78 |
| EDEN/USDT:USDT | +44.91% | $30,424,605.11 |
| NIL/USDT:USDT | +19.66% | $3,491,681.27 |
| SATO/USDT:USDT | +15.35% | $3,552,341.30 |
| JTO/USDT:USDT | +14.39% | $3,278,617.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROAM/USDT:USDT | below_1h_threshold | +4.91% | +4.81% |
| BEAT/USDT:USDT | below_1h_threshold | +4.16% | +4.05% |
| USELESS/USDT:USDT | below_1h_threshold | +2.93% | +2.82% |
| LIT/USDT:USDT | below_1h_threshold | +2.71% | +2.60% |
| SUI/USDT:USDT | below_1h_threshold | +1.87% | +1.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
