# Decision Report

- generated_at: 2026-08-15T12:46:27.938775+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11663**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.80% / filled 20/20。**
- 全期間 MARKET基準: n=11663, expectancy=-0.01%
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
| LIMIT_2PCT | 13/20 | 65.0% | +3.40% | **+2.21%** |
| LIMIT_1PCT | 14/20 | 70.0% | +2.37% | **+1.66%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.72% | **+0.86%** |
| LIMIT_BB3S | 3/15 | 20.0% | +2.30% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +3.81% | **+1.33%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +2.41% | **+0.96%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.56% | **-0.14%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_5PCT_LONG | 15/20 | 75.0% | -0.58% | **-0.43%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.37** / 初期 $100.00 (+541.37%)
- 確定: 4131件 (Win 1290 / Loss 1355 / Flat 1486) / skip 4093件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $641.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.00** / 初期 $100.00 (+55.00%)
- 確定: 1726件 (Win 490 / Loss 413 / Flat 823) / skip 3348件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1045 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.08% 残高後 $155.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.52** / 初期 $100.00 (+19.52%)
- 確定: 1605件 (Win 489 / Loss 606 / Flat 510) / pending 6件 / skip 1525件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000623 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $119.52

## 6. Latest Market Context

- 更新: 2026-08-15T12:46:20.677914+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=62924.5
- Funnel: target 985 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.5 >= 65=1, 4h RSI 78.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COW/USDT:USDT | +57.40% | $6,783,268.10 |
| WAL/USDT:USDT | +34.64% | $1,240,723.61 |
| VELVET/USDT:USDT | +26.60% | $32,898,809.74 |
| ANSEM/USDT:USDT | +25.43% | $1,632,849.29 |
| AEON1/USDT:USDT | +19.86% | $1,008,585.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MOVR/USDT:USDT | below_1h_threshold | +4.85% | +4.96% |
| PRL/USDT:USDT | below_1h_threshold | +3.43% | +3.53% |
| AEON1/USDT:USDT | below_1h_threshold | +1.96% | +2.07% |
| VELVET/USDT:USDT | below_1h_threshold | +1.44% | +1.55% |
| US/USDT:USDT | below_1h_threshold | +1.42% | +1.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
