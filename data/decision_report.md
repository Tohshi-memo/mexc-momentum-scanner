# Decision Report

- generated_at: 2026-09-15T17:51:32.219954+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14610**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14610, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/18 | 44.4% | +0.48% | **+0.22%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.11% | **+0.09%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.38% | **+0.25%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.19%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.35% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,065.27** / 初期 $100.00 (+965.27%)
- 確定: 5512件 (Win 1645 / Loss 1782 / Flat 2085) / skip 5659件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,065.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.42** / 初期 $100.00 (+130.42%)
- 確定: 3049件 (Win 839 / Loss 719 / Flat 1491) / skip 4972件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $230.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.11** / 初期 $100.00 (+24.11%)
- 確定: 2909件 (Win 863 / Loss 1133 / Flat 913) / pending 0件 / skip 3176件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000192 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: POWR/USDT:USDT `MARKET` EXPIRED account +0.10% 残高後 $124.11

## 6. Latest Market Context

- 更新: 2026-09-15T17:51:18.253349+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.88% price=77025.1
- Funnel: target 1060 → liquid 158 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.7 >= 65=1, 4h RSI 97.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +17.66% | $3,862,564.85 |
| 4/USDT:USDT | +8.45% | $1,144,441.06 |
| PONS/USDT:USDT | +7.20% | $9,551,099.18 |
| AIN/USDT:USDT | +6.51% | $18,950,009.83 |
| ZRO/USDT:USDT | +5.50% | $3,442,381.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_relative_strength | +5.46% | +4.58% |
| REZ/USDT:USDT | below_relative_strength | +5.07% | +4.19% |
| AKE/USDT:USDT | below_1h_threshold | +3.72% | +2.84% |
| CNPY/USDT:USDT | below_1h_threshold | +2.80% | +1.92% |
| ZEC/USDT:USDT | below_1h_threshold | +2.52% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
