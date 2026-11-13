# Decision Report

- generated_at: 2026-11-13T04:01:27.244713+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18778**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.07% / filled 20/20。**
- 全期間 MARKET基準: n=18778, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.40% | **+0.26%** |
| LIMIT_BB3S | 2/18 | 11.1% | +2.00% | **+0.22%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.30% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.02% | **+0.92%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.56% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,724.15** / 初期 $100.00 (+1624.15%)
- 確定: 7248件 (Win 2088 / Loss 2322 / Flat 2838) / skip 8091件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,724.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$398.81** / 初期 $100.00 (+298.81%)
- 確定: 4797件 (Win 1293 / Loss 1065 / Flat 2439) / skip 7392件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0232 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $398.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6937件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000185 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T04:01:13.920619+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=68839.2
- Funnel: target 1105 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BARD/USDT:USDT | +39.72% | $8,938,905.41 |
| KOR/USDT:USDT | +37.87% | $1,514,734.45 |
| ARIA/USDT:USDT | +37.56% | $9,051,989.08 |
| GANG/USDT:USDT | +17.88% | $1,130,831.23 |
| CBRSSTOCK/USDT:USDT | +11.42% | $3,519,373.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +4.10% | +4.24% |
| SQQQ/USDT:USDT | below_1h_threshold | +1.43% | +1.56% |
| BARD/USDT:USDT | below_1h_threshold | +1.16% | +1.29% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.15% | +0.28% |
| ALUMINUM/USDT:USDT | below_1h_threshold | +0.14% | +0.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
