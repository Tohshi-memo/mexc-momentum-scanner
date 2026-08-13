# Decision Report

- generated_at: 2026-08-13T10:41:23.042343+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11437**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=11437, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.50% | **+1.43%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.81% | **+1.00%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.60% | **+0.96%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.24% | **+0.93%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.04% | **+0.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.40% | **+1.19%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_FIB1272_LONG | 15/20 | 75.0% | +1.41% | **+1.06%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.15% | **+1.03%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$622.39** / 初期 $100.00 (+522.39%)
- 確定: 3955件 (Win 1237 / Loss 1292 / Flat 1426) / skip 4043件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $622.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$150.98** / 初期 $100.00 (+50.98%)
- 確定: 1625件 (Win 464 / Loss 385 / Flat 776) / skip 3223件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1501 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $150.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.50** / 初期 $100.00 (+16.50%)
- 確定: 1444件 (Win 425 / Loss 542 / Flat 477) / pending 4件 / skip 1460件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000186 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $116.50

## 6. Latest Market Context

- 更新: 2026-08-13T10:41:14.349367+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=63576.7
- Funnel: target 973 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.2 >= 65=1, 4h RSI 82.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AVAAI/USDT:USDT | +35.54% | $1,252,603.90 |
| AKE/USDT:USDT | +29.63% | $4,797,219.80 |
| ACU/USDT:USDT | +19.71% | $6,552,453.27 |
| BTW/USDT:USDT | +18.59% | $26,450,149.14 |
| BANK/USDT:USDT | +14.98% | $5,092,971.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.43% | +3.71% |
| COTI/USDT:USDT | below_1h_threshold | +3.01% | +3.30% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +2.84% | +3.13% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.59% | +2.88% |
| RE/USDT:USDT | below_1h_threshold | +1.38% | +1.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
