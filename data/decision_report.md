# Decision Report

- generated_at: 2026-09-10T03:01:20.462047+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14148**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14148, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.89% | **+1.13%** |
| LIMIT_6PCT | 8/20 | 40.0% | +2.65% | **+1.06%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +3.92% | **+3.33%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.25% | **+2.76%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.34% | **+2.22%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,058.79** / 初期 $100.00 (+958.79%)
- 確定: 5328件 (Win 1603 / Loss 1718 / Flat 2007) / skip 5381件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VTHO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,058.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$207.48** / 初期 $100.00 (+107.48%)
- 確定: 2742件 (Win 759 / Loss 642 / Flat 1341) / skip 4817件
- 成長率目線: 平均log +0.000266 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0935 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VTHO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $207.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.14** / 初期 $100.00 (+22.14%)
- 確定: 2653件 (Win 783 / Loss 1012 / Flat 858) / pending 4件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000572 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VTHO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.14

## 6. Latest Market Context

- 更新: 2026-09-10T03:01:10.863902+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78335.0
- Funnel: target 1064 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VTHO/USDT:USDT | +61.17% | $1,926,539.99 |
| CATE/USDT:USDT | +36.64% | $2,850,401.72 |
| BTR/USDT:USDT | +25.08% | $2,624,097.38 |
| VET/USDT:USDT | +4.09% | $5,155,594.50 |
| MINA/USDT:USDT | +2.97% | $1,331,917.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOFTBANKSTOCK/USDT:USDT | below_1h_threshold | +0.83% | +0.82% |
| POL/USDT:USDT | below_1h_threshold | +0.42% | +0.41% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.38% | +0.37% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.38% | +0.36% |
| EWY/USDT:USDT | below_1h_threshold | +0.36% | +0.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
