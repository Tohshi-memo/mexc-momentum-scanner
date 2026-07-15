# Decision Report

- generated_at: 2026-07-15T12:16:09.810288+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8739**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8739, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.43% | **-0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 9/20 | 45.0% | +4.93% | **+2.22%** |
| LIMIT_8PCT | 8/20 | 40.0% | +5.43% | **+2.17%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 10/20 | 50.0% | +1.96% | **+0.98%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +3.28% | **+2.34%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.87% | **+2.30%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.79% | **+2.10%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.46% | **+1.60%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.98% | **+1.29%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 98件 (TP 34 / SL 62 / EXP 2)
- 最新: MAGMA/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.63** / 初期 $100.00 (+242.63%)
- 確定: 2879件 (Win 901 / Loss 935 / Flat 1043) / skip 2421件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAVE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.82% 残高後 $342.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.35** / 初期 $100.00 (+6.35%)
- 確定: 705件 (Win 166 / Loss 165 / Flat 374) / skip 1445件
- 成長率目線: 平均log +0.000087 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0872 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 0G/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.19% 残高後 $106.35

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 61件 (Win 19 / Loss 39 / Flat 3) / pending 3件 / skip 150件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000340 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 0G/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-15T12:16:03.770512+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64710.7
- Funnel: target 870 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +175.81% | $19,535,039.41 |
| DODO/USDT:USDT | +37.30% | $11,263,395.42 |
| US/USDT:USDT | +34.93% | $5,113,650.20 |
| AEHRSTOCK/USDT:USDT | +30.95% | $3,959,502.20 |
| 0G/USDT:USDT | +17.66% | $1,820,160.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 0G/USDT:USDT | below_1h_threshold | +4.52% | +4.52% |
| US/USDT:USDT | below_1h_threshold | +1.48% | +1.47% |
| TAC/USDT:USDT | below_1h_threshold | +1.11% | +1.10% |
| INJ/USDT:USDT | below_1h_threshold | +0.85% | +0.85% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.82% | +0.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
