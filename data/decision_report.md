# Decision Report

- generated_at: 2026-08-26T11:16:18.472930+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12698**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12698, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.50% | **-0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR | 18/20 | 90.0% | +0.86% | **+0.77%** |
| LIMIT_BB3S | 8/18 | 44.4% | +1.28% | **+0.57%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.64% | **+0.29%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.92% | **+1.82%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.47% | **+1.60%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.98% | **+1.58%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.53% | **+0.84%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +1.62% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$707.54** / 初期 $100.00 (+607.54%)
- 確定: 4599件 (Win 1400 / Loss 1511 / Flat 1688) / skip 4660件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $707.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$159.27** / 初期 $100.00 (+59.27%)
- 確定: 1994件 (Win 544 / Loss 478 / Flat 972) / skip 4115件
- 成長率目線: 平均log +0.000233 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1804 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $159.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.23** / 初期 $100.00 (+17.23%)
- 確定: 1971件 (Win 580 / Loss 750 / Flat 641) / pending 5件 / skip 2195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000440 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $117.23

## 6. Latest Market Context

- 更新: 2026-08-26T11:16:09.498386+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78676.0
- Funnel: target 1023 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +236.55% | $15,543,819.22 |
| TAC/USDT:USDT | +59.70% | $6,846,585.62 |
| BMT/USDT:USDT | +56.40% | $15,212,266.65 |
| LONGXIA/USDT:USDT | +26.14% | $1,982,517.53 |
| PONS/USDT:USDT | +22.87% | $1,136,826.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +3.84% | +3.86% |
| BICO/USDT:USDT | below_1h_threshold | +1.87% | +1.88% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.04% | +1.05% |
| LIGHT/USDT:USDT | below_1h_threshold | +0.81% | +0.82% |
| STX/USDT:USDT | below_1h_threshold | +0.78% | +0.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
