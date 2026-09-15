# Decision Report

- generated_at: 2026-09-15T02:26:22.306946+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14550**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.24% / filled 20/20。**
- 全期間 MARKET基準: n=14550, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.24% | **+1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| MARKET | 20/20 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.53% | **+0.89%** |
| LIMIT_BB3S | 3/16 | 18.8% | +2.15% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.10% | **+0.73%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.70% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 213件 (TP 79 / SL 129 / EXP 5)
- 最新: STORJ/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,073.59** / 初期 $100.00 (+973.59%)
- 確定: 5452件 (Win 1639 / Loss 1770 / Flat 2043) / skip 5659件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SHROOM/USDT:USDT `LIMIT_FIB1272` TP_HIT account +1.00% 残高後 $1,073.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$229.18** / 初期 $100.00 (+129.18%)
- 確定: 2993件 (Win 831 / Loss 716 / Flat 1446) / skip 4968件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0258 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SHROOM/USDT:USDT `LIMIT_FIB1272` TP_HIT account +0.69% 残高後 $229.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.52** / 初期 $100.00 (+25.52%)
- 確定: 2896件 (Win 861 / Loss 1124 / Flat 911) / pending 4件 / skip 3121件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000460 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SHROOM/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $125.52

## 6. Latest Market Context

- 更新: 2026-09-15T02:26:10.603166+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=77942.4
- Funnel: target 1073 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +47.34% | $1,286,547.49 |
| AIN/USDT:USDT | +27.57% | $7,572,793.03 |
| POWER/USDT:USDT | +24.77% | $6,167,584.60 |
| CNPY/USDT:USDT | +20.87% | $1,788,410.40 |
| CAP/USDT:USDT | +11.92% | $2,621,034.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POWER/USDT:USDT | below_1h_threshold | +4.79% | +4.72% |
| BLESS/USDT:USDT | below_1h_threshold | +2.97% | +2.90% |
| PONS/USDT:USDT | below_1h_threshold | +2.85% | +2.78% |
| CNPY/USDT:USDT | below_1h_threshold | +2.33% | +2.26% |
| JUP/USDT:USDT | below_1h_threshold | +1.85% | +1.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
