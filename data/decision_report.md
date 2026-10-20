# Decision Report

- generated_at: 2026-10-20T08:36:20.209988+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17048**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.49% / filled 20/20。**
- 全期間 MARKET基準: n=17048, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.49% | **+1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.27% | **+1.14%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.29% | **+0.91%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_BB3S | 2/14 | 14.3% | +3.70% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +2.90% | **+2.90%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +1.36% | **+0.95%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.37% | **+0.30%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.19% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,311.11** / 初期 $100.00 (+1211.11%)
- 確定: 6477件 (Win 1883 / Loss 2066 / Flat 2528) / skip 7132件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $1,311.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.39** / 初期 $100.00 (+178.39%)
- 確定: 3801件 (Win 1044 / Loss 886 / Flat 1871) / skip 6658件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0346 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $278.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5207件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000314 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T08:36:08.013839+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=81552.7
- Funnel: target 1078 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +47.52% | $2,133,642.32 |
| ALT/USDT:USDT | +26.06% | $1,441,077.36 |
| PHA/USDT:USDT | +18.91% | $18,236,547.37 |
| BR/USDT:USDT | +13.77% | $45,075,745.77 |
| A/USDT:USDT | +12.41% | $23,178,126.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +3.51% | +3.47% |
| APR/USDT:USDT | below_1h_threshold | +1.62% | +1.58% |
| SOXS/USDT:USDT | below_1h_threshold | +1.61% | +1.57% |
| BAT/USDT:USDT | below_1h_threshold | +1.24% | +1.20% |
| ALT/USDT:USDT | below_1h_threshold | +1.08% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
