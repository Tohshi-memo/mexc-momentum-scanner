# Decision Report

- generated_at: 2026-08-13T11:21:21.425973+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11442**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=11442, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.50% | **+1.43%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.66% | **+1.16%** |
| LIMIT_BB3S | 3/14 | 21.4% | +4.91% | **+1.05%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.24% | **+0.93%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.04% | **+0.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.32% | **+0.86%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.90% | **+0.86%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.86% | **+0.73%** |
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +2.00% | **+0.67%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.57% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$613.10** / 初期 $100.00 (+513.10%)
- 確定: 3960件 (Win 1237 / Loss 1295 / Flat 1428) / skip 4043件
- 成長率目線: 平均log +0.000458 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AVAAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $613.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$150.04** / 初期 $100.00 (+50.04%)
- 確定: 1630件 (Win 465 / Loss 388 / Flat 777) / skip 3223件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1314 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AVAAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $150.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.19** / 初期 $100.00 (+16.19%)
- 確定: 1449件 (Win 426 / Loss 545 / Flat 478) / pending 1件 / skip 1460件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000181 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AVAAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.19

## 6. Latest Market Context

- 更新: 2026-08-13T11:21:11.535001+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=63586.3
- Funnel: target 973 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +40.80% | $7,857,044.35 |
| ACU/USDT:USDT | +22.70% | $6,694,799.80 |
| BANK/USDT:USDT | +22.11% | $5,662,959.72 |
| AVAAI/USDT:USDT | +20.14% | $1,504,639.41 |
| BTW/USDT:USDT | +18.00% | $25,481,313.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +4.08% | +4.15% |
| AKE/USDT:USDT | below_1h_threshold | +3.41% | +3.47% |
| MYX/USDT:USDT | below_1h_threshold | +2.07% | +2.13% |
| ATOM/USDT:USDT | below_1h_threshold | +1.56% | +1.63% |
| BLUAI/USDT:USDT | below_1h_threshold | +1.41% | +1.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
