# Decision Report

- generated_at: 2026-08-15T09:36:33.414316+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11650**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.87% / filled 20/20。**
- 全期間 MARKET基準: n=11650, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.87% | **+2.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.87% | **+2.87%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.73% | **+1.91%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.26% | **+1.81%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.83% | **+1.56%** |
| LIMIT_5PCT | 4/20 | 20.0% | +4.48% | **+0.90%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +3.00% | **+1.80%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +3.91% | **+1.56%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +5.04% | **+1.51%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.07% | **+0.70%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -0.03% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.37** / 初期 $100.00 (+541.37%)
- 確定: 4118件 (Win 1288 / Loss 1353 / Flat 1477) / skip 4093件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $641.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.91** / 初期 $100.00 (+54.91%)
- 確定: 1713件 (Win 488 / Loss 410 / Flat 815) / skip 3348件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1170 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $154.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.05** / 初期 $100.00 (+18.05%)
- 確定: 1593件 (Win 484 / Loss 605 / Flat 504) / pending 6件 / skip 1525件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000241 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_9PCT_LONG` TP_HIT account +0.34% 残高後 $118.05

## 6. Latest Market Context

- 更新: 2026-08-15T09:36:21.302873+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=62965.9
- Funnel: target 985 → liquid 161 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.1 >= 65=1, 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COW/USDT:USDT | +48.80% | $1,021,342.69 |
| ANSEM/USDT:USDT | +25.38% | $1,271,471.72 |
| VELVET/USDT:USDT | +20.87% | $34,389,091.34 |
| CYS/USDT:USDT | +18.50% | $17,238,281.68 |
| ROBO/USDT:USDT | +18.38% | $6,915,546.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ON/USDT:USDT | below_1h_threshold | +2.62% | +2.53% |
| DOT/USDT:USDT | below_1h_threshold | +0.91% | +0.82% |
| WLFI/USDT:USDT | below_1h_threshold | +0.69% | +0.60% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +0.65% | +0.56% |
| US/USDT:USDT | below_1h_threshold | +0.60% | +0.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
