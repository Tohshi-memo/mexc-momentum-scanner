# Decision Report

- generated_at: 2026-09-23T04:46:22.367486+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15389**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.51% / filled 20/20。**
- 全期間 MARKET基準: n=15389, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.51% | **+0.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.29% | **+0.22%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.23% | **+0.21%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.34% | **+1.12%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.10% | **+0.77%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.76% | **+0.61%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +1.97% | **+0.49%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.56% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,164.04** / 初期 $100.00 (+1064.04%)
- 確定: 5865件 (Win 1732 / Loss 1882 / Flat 2251) / skip 6085件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `MARKET_LONG` EXPIRED account +0.22% 残高後 $1,164.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5447件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.43** / 初期 $100.00 (+22.43%)
- 確定: 3125件 (Win 920 / Loss 1226 / Flat 979) / pending 4件 / skip 3738件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `MARKET_LONG` EXPIRED account +0.07% 残高後 $122.43

## 6. Latest Market Context

- 更新: 2026-09-23T04:46:11.185073+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.49% price=87089.5
- Funnel: target 1058 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +61.44% | $1,193,770.52 |
| MUBARAK/USDT:USDT | +22.48% | $18,892,221.57 |
| ALLO/USDT:USDT | +17.83% | $2,642,254.11 |
| DRIFT/USDT:USDT | +17.58% | $1,799,578.25 |
| PENGU/USDT:USDT | +17.11% | $16,547,151.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LONGXIA/USDT:USDT | below_1h_threshold | +3.81% | +3.32% |
| MUBARAK/USDT:USDT | below_1h_threshold | +3.61% | +3.12% |
| TUT/USDT:USDT | below_1h_threshold | +3.15% | +2.66% |
| PENGU/USDT:USDT | below_1h_threshold | +2.77% | +2.27% |
| 1000BONK/USDT:USDT | below_1h_threshold | +2.34% | +1.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
