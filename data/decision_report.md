# Decision Report

- generated_at: 2026-08-15T07:51:29.384771+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11647**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.66% / filled 20/20。**
- 全期間 MARKET基準: n=11647, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.66% | **+2.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.66% | **+2.66%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.53% | **+2.15%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.73% | **+1.91%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.83% | **+1.56%** |
| LIMIT_ATR | 7/20 | 35.0% | +2.98% | **+1.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +3.27% | **+1.80%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.33% | **+1.16%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.91% | **+0.64%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.84% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$640.49** / 初期 $100.00 (+540.49%)
- 確定: 4115件 (Win 1287 / Loss 1353 / Flat 1475) / skip 4093件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALICE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $640.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.92** / 初期 $100.00 (+54.92%)
- 確定: 1710件 (Win 488 / Loss 409 / Flat 813) / skip 3348件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1120 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALICE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $154.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.60** / 初期 $100.00 (+17.60%)
- 確定: 1591件 (Win 482 / Loss 605 / Flat 504) / pending 6件 / skip 1523件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000188 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ALICE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $117.60

## 6. Latest Market Context

- 更新: 2026-08-15T07:51:18.228192+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=63049.9
- Funnel: target 985 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROBO/USDT:USDT | +29.42% | $5,992,575.67 |
| VELVET/USDT:USDT | +29.24% | $38,117,105.13 |
| NIL/USDT:USDT | +26.71% | $3,109,438.89 |
| PRL/USDT:USDT | +25.76% | $1,412,564.19 |
| CYS/USDT:USDT | +20.35% | $17,644,382.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_1h_threshold | +4.03% | +4.09% |
| ROBO/USDT:USDT | below_1h_threshold | +3.89% | +3.95% |
| US/USDT:USDT | below_1h_threshold | +3.43% | +3.49% |
| NIL/USDT:USDT | below_1h_threshold | +2.60% | +2.66% |
| CAP/USDT:USDT | below_1h_threshold | +2.27% | +2.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
