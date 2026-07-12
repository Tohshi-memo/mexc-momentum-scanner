# Decision Report

- generated_at: 2026-07-12T17:16:08.625739+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8602**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.58% / filled 20/20。**
- 全期間 MARKET基準: n=8602, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.58% | **+1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.09% | **+1.98%** |
| MARKET | 20/20 | 100.0% | +1.58% | **+1.58%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.14% | **+0.85%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.64% | **+0.45%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.40% | **+1.44%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.75% | **+0.96%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.18% | **+0.65%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$102.22** / 初期 $100.00 (+2.22%)
- 確定トレード: 89件 (TP 30 / SL 57 / EXP 2)
- 最新: BSB/USDT:USDT EXPIRED PnL +5.08% 残高後 $102.22
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$319.81** / 初期 $100.00 (+219.81%)
- 確定: 2784件 (Win 875 / Loss 922 / Flat 987) / skip 2379件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $319.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 644件 (Win 152 / Loss 159 / Flat 333) / skip 1369件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 27件 (Win 9 / Loss 18 / Flat 0) / pending 0件 / skip 49件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000402 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.00

## 6. Latest Market Context

- 更新: 2026-07-12T17:16:03.768734+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=64110.5
- Funnel: target 863 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIPPIN/USDT:USDT | +5.91% | $1,912,420.05 |
| ALLO/USDT:USDT | +3.09% | $14,272,440.51 |
| BASED/USDT:USDT | +2.58% | $2,488,130.00 |
| T/USDT:USDT | +2.38% | $19,649,850.38 |
| ZEC/USDT:USDT | +2.35% | $195,921,875.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +1.64% | +1.69% |
| BXSTOCK/USDT:USDT | below_1h_threshold | +1.48% | +1.54% |
| ALLO/USDT:USDT | below_1h_threshold | +1.40% | +1.45% |
| FHE/USDT:USDT | below_1h_threshold | +1.23% | +1.28% |
| APE/USDT:USDT | below_1h_threshold | +0.97% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
