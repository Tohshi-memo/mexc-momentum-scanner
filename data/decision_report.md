# Decision Report

- generated_at: 2026-08-15T14:06:31.096784+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11674**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=11674, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.25% | **+0.15%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.00% | **+0.00%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | -0.60% | **-0.18%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -2.45% | **-0.37%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.75% | **-0.38%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.37** / 初期 $100.00 (+541.37%)
- 確定: 4142件 (Win 1290 / Loss 1355 / Flat 1497) / skip 4093件
- 成長率目線: 平均log +0.000449 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CYS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $641.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1737件 (Win 492 / Loss 413 / Flat 832) / skip 3348件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0960 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.76** / 初期 $100.00 (+19.76%)
- 確定: 1615件 (Win 493 / Loss 611 / Flat 511) / pending 5件 / skip 1527件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000571 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $119.76

## 6. Latest Market Context

- 更新: 2026-08-15T14:06:18.704173+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=63011.1
- Funnel: target 985 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COW/USDT:USDT | +51.60% | $8,237,428.85 |
| CYS/USDT:USDT | +32.74% | $20,841,071.46 |
| ANSEM/USDT:USDT | +26.77% | $1,727,412.72 |
| WAL/USDT:USDT | +26.31% | $1,515,079.42 |
| VELVET/USDT:USDT | +23.47% | $27,202,278.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AEON1/USDT:USDT | below_1h_threshold | +1.45% | +1.47% |
| US/USDT:USDT | below_1h_threshold | +1.34% | +1.37% |
| ONE/USDT:USDT | below_1h_threshold | +1.14% | +1.16% |
| CAP/USDT:USDT | below_1h_threshold | +1.02% | +1.04% |
| RE/USDT:USDT | below_1h_threshold | +0.74% | +0.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
