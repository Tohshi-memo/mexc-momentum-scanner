# Decision Report

- generated_at: 2026-10-22T01:11:17.362399+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17111**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=17111, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.80% | **+0.76%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.49% | **+0.42%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.40% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +3.04% | **+0.91%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.78% | **+0.66%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.85% | **+0.25%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.01% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,345.26** / 初期 $100.00 (+1245.26%)
- 確定: 6493件 (Win 1890 / Loss 2072 / Flat 2531) / skip 7179件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DOOD/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,345.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.63** / 初期 $100.00 (+178.63%)
- 確定: 3824件 (Win 1051 / Loss 894 / Flat 1879) / skip 6698件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $278.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5270件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000268 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-22T01:11:07.744693+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=84194.5
- Funnel: target 1089 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALT/USDT:USDT | +32.70% | $7,508,352.59 |
| PTB/USDT:USDT | +29.41% | $1,021,889.30 |
| BULLA/USDT:USDT | +23.24% | $4,553,294.68 |
| LIT/USDT:USDT | +12.37% | $17,022,362.03 |
| BTW/USDT:USDT | +11.79% | $31,199,565.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +2.19% | +2.15% |
| VVV/USDT:USDT | below_1h_threshold | +1.44% | +1.40% |
| CHIP/USDT:USDT | below_1h_threshold | +1.23% | +1.19% |
| LIT/USDT:USDT | below_1h_threshold | +1.18% | +1.14% |
| BAT/USDT:USDT | below_1h_threshold | +1.04% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
