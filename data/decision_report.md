# Decision Report

- generated_at: 2026-07-27T12:01:19.046276+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9628**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9628, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +3.30% | **+1.49%** |
| LIMIT_4PCT | 16/20 | 80.0% | +1.50% | **+1.20%** |
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.35% | **+0.32%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.63% | **+1.84%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.74% | **+1.78%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |
| LIMIT_BB3S_LONG | 8/9 | 88.9% | +1.48% | **+1.32%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$461.45** / 初期 $100.00 (+361.45%)
- 確定: 3419件 (Win 1084 / Loss 1112 / Flat 1223) / skip 2770件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $461.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1816件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0043 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.02** / 初期 $100.00 (+9.02%)
- 確定: 650件 (Win 216 / Loss 245 / Flat 189) / pending 5件 / skip 445件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000473 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $109.02

## 6. Latest Market Context

- 更新: 2026-07-27T12:01:10.809550+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=65094.3
- Funnel: target 902 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +50.69% | $4,226,685.73 |
| AKE/USDT:USDT | +48.98% | $43,056,900.21 |
| ON/USDT:USDT | +45.46% | $6,174,619.23 |
| DIA/USDT:USDT | +27.03% | $10,836,436.23 |
| NIL/USDT:USDT | +23.79% | $3,115,738.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QBTSSTOCK/USDT:USDT | below_1h_threshold | +3.86% | +3.83% |
| BTW/USDT:USDT | below_1h_threshold | +1.08% | +1.05% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +0.57% | +0.54% |
| DIA/USDT:USDT | below_1h_threshold | +0.41% | +0.38% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.37% | +0.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
