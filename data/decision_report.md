# Decision Report

- generated_at: 2026-09-24T07:26:19.830599+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15465**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15465, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.99% | **+0.94%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.39% | **+1.79%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +3.29% | **+1.48%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.25% | **+1.13%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.97% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5898件 (Win 1739 / Loss 1890 / Flat 2269) / skip 6128件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$253.10** / 初期 $100.00 (+153.10%)
- 確定: 3412件 (Win 942 / Loss 791 / Flat 1679) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0805 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $253.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.86** / 初期 $100.00 (+20.86%)
- 確定: 3155件 (Win 930 / Loss 1244 / Flat 981) / pending 3件 / skip 3777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000431 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $120.86

## 6. Latest Market Context

- 更新: 2026-09-24T07:26:08.545184+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=84182.7
- Funnel: target 1066 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +57.10% | $3,457,783.62 |
| NIL/USDT:USDT | +37.85% | $18,701,224.18 |
| LSK/USDT:USDT | +33.50% | $7,818,657.31 |
| LTC/USDT:USDT | +14.36% | $48,448,444.60 |
| CHR/USDT:USDT | +14.08% | $1,352,314.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +4.20% | +4.07% |
| NIL/USDT:USDT | below_1h_threshold | +2.29% | +2.16% |
| COMP/USDT:USDT | below_1h_threshold | +2.19% | +2.06% |
| BEAT/USDT:USDT | below_1h_threshold | +1.21% | +1.07% |
| JASMY/USDT:USDT | below_1h_threshold | +0.78% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
