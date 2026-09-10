# Decision Report

- generated_at: 2026-09-10T00:06:14.344166+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14132**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.08% / filled 20/20。**
- 全期間 MARKET基準: n=14132, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.08% | **+3.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +3.45% | **+3.11%** |
| MARKET | 20/20 | 100.0% | +3.08% | **+3.08%** |
| LIMIT_2PCT | 13/20 | 65.0% | +3.93% | **+2.55%** |
| LIMIT_ATR | 12/20 | 60.0% | +3.16% | **+1.90%** |
| LIMIT_BB3S | 9/20 | 45.0% | +1.88% | **+0.85%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.43% | **+0.64%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.39% | **+0.63%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -0.06% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5380件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$197.40** / 初期 $100.00 (+97.40%)
- 確定: 2726件 (Win 749 / Loss 639 / Flat 1338) / skip 4817件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0512 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $197.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.14** / 初期 $100.00 (+19.14%)
- 確定: 2637件 (Win 773 / Loss 1009 / Flat 855) / pending 2件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000365 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.14

## 6. Latest Market Context

- 更新: 2026-09-10T00:06:04.027103+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=78311.4
- Funnel: target 1064 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +14.88% | $2,791,930.13 |
| BTR/USDT:USDT | +14.83% | $2,027,471.58 |
| WAVES/USDT:USDT | +9.80% | $1,197,070.97 |
| MINA/USDT:USDT | +4.25% | $1,186,725.75 |
| IOST/USDT:USDT | +3.42% | $41,862,413.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +0.95% | +0.89% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.85% | +0.79% |
| VET/USDT:USDT | below_1h_threshold | +0.82% | +0.76% |
| SNXX/USDT:USDT | below_1h_threshold | +0.79% | +0.73% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.71% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
