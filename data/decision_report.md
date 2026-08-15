# Decision Report

- generated_at: 2026-08-15T05:56:30.141634+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11641**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.75% / filled 20/20。**
- 全期間 MARKET基準: n=11641, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.38% | **+1.10%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.97% | **+1.04%** |
| LIMIT_ATR | 8/20 | 40.0% | +2.43% | **+0.97%** |
| LIMIT_BB3S | 3/16 | 18.8% | +4.60% | **+0.86%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.42% | **+1.21%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.22% | **+1.00%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.36% | **+0.47%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.60% | **+0.42%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$639.61** / 初期 $100.00 (+539.61%)
- 確定: 4109件 (Win 1286 / Loss 1353 / Flat 1470) / skip 4093件
- 成長率目線: 平均log +0.000452 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $639.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.92** / 初期 $100.00 (+54.92%)
- 確定: 1704件 (Win 488 / Loss 409 / Flat 807) / skip 3348件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0448 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $154.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.55** / 初期 $100.00 (+17.55%)
- 確定: 1585件 (Win 481 / Loss 605 / Flat 499) / pending 6件 / skip 1523件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000168 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_9PCT_LONG` SL_HIT account -0.17% 残高後 $117.55

## 6. Latest Market Context

- 更新: 2026-08-15T05:56:16.190011+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=63027.8
- Funnel: target 985 → liquid 167 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.1 >= 65=1, 4h RSI 82.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROBO/USDT:USDT | +32.86% | $5,083,782.36 |
| VELVET/USDT:USDT | +30.20% | $46,721,325.88 |
| ONE/USDT:USDT | +20.96% | $1,582,857.18 |
| ANSEM/USDT:USDT | +20.41% | $1,020,104.13 |
| PRL/USDT:USDT | +19.62% | $1,067,426.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOLO/USDT:USDT | below_1h_threshold | +4.30% | +4.41% |
| ONE/USDT:USDT | below_1h_threshold | +4.14% | +4.24% |
| NIL/USDT:USDT | below_1h_threshold | +4.13% | +4.23% |
| US/USDT:USDT | below_1h_threshold | +3.80% | +3.90% |
| BTW/USDT:USDT | below_1h_threshold | +2.71% | +2.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
