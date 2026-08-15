# Decision Report

- generated_at: 2026-08-15T10:51:25.112932+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11659**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.80% / filled 20/20。**
- 全期間 MARKET基準: n=11659, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.80% | **+3.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.80% | **+3.80%** |
| LIMIT_1PCT | 17/20 | 85.0% | +3.36% | **+2.86%** |
| LIMIT_2PCT | 14/20 | 70.0% | +3.73% | **+2.61%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.77% | **+1.66%** |
| LIMIT_BB3S | 3/16 | 18.8% | +2.30% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 8/20 | 40.0% | +4.33% | **+1.73%** |
| LIMIT_9PCT_LONG | 9/20 | 45.0% | +3.03% | **+1.36%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | +0.92% | **+0.60%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.26% | **+0.17%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.37% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$644.59** / 初期 $100.00 (+544.59%)
- 確定: 4127件 (Win 1290 / Loss 1354 / Flat 1483) / skip 4093件
- 成長率目線: 平均log +0.000452 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $644.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.41** / 初期 $100.00 (+55.41%)
- 確定: 1722件 (Win 489 / Loss 412 / Flat 821) / skip 3348件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1149 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.92** / 初期 $100.00 (+18.92%)
- 確定: 1601件 (Win 487 / Loss 605 / Flat 509) / pending 5件 / skip 1525件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000274 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $118.92

## 6. Latest Market Context

- 更新: 2026-08-15T10:51:15.947796+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=63024.9
- Funnel: target 985 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.6 >= 65=1, 4h RSI 72.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COW/USDT:USDT | +50.10% | $3,437,732.10 |
| ANSEM/USDT:USDT | +30.99% | $1,469,747.95 |
| ROBO/USDT:USDT | +26.59% | $7,171,665.32 |
| US/USDT:USDT | +20.13% | $6,175,548.40 |
| BMT/USDT:USDT | +19.70% | $1,133,719.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BMT/USDT:USDT | below_1h_threshold | +3.48% | +3.44% |
| ACU/USDT:USDT | below_1h_threshold | +3.40% | +3.35% |
| US/USDT:USDT | below_1h_threshold | +2.88% | +2.84% |
| NIL/USDT:USDT | below_1h_threshold | +2.72% | +2.68% |
| RE/USDT:USDT | below_1h_threshold | +2.54% | +2.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
