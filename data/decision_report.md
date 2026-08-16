# Decision Report

- generated_at: 2026-08-16T18:46:34.034823+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11765**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=11765, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/18 | 27.8% | +3.57% | **+0.99%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.00% | **+0.95%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.02% | **+0.41%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.65% | **+0.39%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.94% | **+0.33%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.44% | **+0.27%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.12% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 184件 (TP 71 / SL 108 / EXP 5)
- 最新: APR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4183件 (Win 1292 / Loss 1363 / Flat 1528) / skip 4143件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CROSS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.46** / 初期 $100.00 (+54.46%)
- 確定: 1787件 (Win 496 / Loss 418 / Flat 873) / skip 3389件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $154.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.10** / 初期 $100.00 (+19.10%)
- 確定: 1661件 (Win 501 / Loss 627 / Flat 533) / pending 5件 / skip 1572件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000123 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.10

## 6. Latest Market Context

- 更新: 2026-08-16T18:46:22.842246+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=63113.4
- Funnel: target 986 → liquid 145 → pre 50 → checked 49 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=1
- Strict後reject: 4h RSI 65.9 >= 65=1, 4h RSI 88.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HFT/USDT:USDT | +54.30% | $1,352,489.02 |
| PORTAL/USDT:USDT | +27.64% | $8,540,442.85 |
| APR/USDT:USDT | +19.10% | $5,481,921.95 |
| BTW/USDT:USDT | +6.48% | $17,241,998.87 |
| RIVER/USDT:USDT | +5.69% | $2,203,318.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.58% | +4.61% |
| BR/USDT:USDT | below_1h_threshold | +2.30% | +2.33% |
| BEAT/USDT:USDT | below_1h_threshold | +2.17% | +2.20% |
| VELVET/USDT:USDT | below_1h_threshold | +1.36% | +1.38% |
| KAITO/USDT:USDT | below_1h_threshold | +1.18% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
