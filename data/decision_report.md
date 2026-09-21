# Decision Report

- generated_at: 2026-09-21T00:26:27.053457+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15221**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15221, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +1.66% | **+1.16%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.10% | **+0.88%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.41% | **+0.37%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.41% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.39% | **+0.69%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.06% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,173.63** / 初期 $100.00 (+1073.63%)
- 確定: 5717件 (Win 1705 / Loss 1845 / Flat 2167) / skip 6065件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OFC/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,173.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$246.81** / 初期 $100.00 (+146.81%)
- 確定: 3297件 (Win 911 / Loss 765 / Flat 1621) / skip 5335件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $246.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.97** / 初期 $100.00 (+21.97%)
- 確定: 3001件 (Win 888 / Loss 1185 / Flat 928) / pending 4件 / skip 3689件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000206 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.04% 残高後 $121.97

## 6. Latest Market Context

- 更新: 2026-09-21T00:26:13.696346+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.70% price=81713.7
- Funnel: target 1050 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIL/USDT:USDT | +26.25% | $4,841,123.39 |
| SAGA/USDT:USDT | +19.59% | $7,839,213.47 |
| S/USDT:USDT | +16.35% | $3,574,863.26 |
| AR/USDT:USDT | +14.88% | $7,303,069.90 |
| SEI/USDT:USDT | +14.14% | $14,221,040.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SUI/USDT:USDT | below_1h_threshold | +4.87% | +4.17% |
| B2/USDT:USDT | below_1h_threshold | +3.97% | +3.27% |
| NIL/USDT:USDT | below_1h_threshold | +3.44% | +2.74% |
| AR/USDT:USDT | below_1h_threshold | +3.36% | +2.66% |
| SAGA/USDT:USDT | below_1h_threshold | +3.33% | +2.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
