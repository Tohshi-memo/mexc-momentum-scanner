# Decision Report

- generated_at: 2026-09-10T03:36:12.307217+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14149**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14149, expectancy=-0.01%
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
| LIMIT_5PCT | 13/20 | 65.0% | +1.82% | **+1.18%** |
| LIMIT_6PCT | 9/20 | 45.0% | +2.57% | **+1.15%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +4.41% | **+3.53%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.81% | **+2.67%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.93% | **+2.36%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,058.79** / 初期 $100.00 (+958.79%)
- 確定: 5329件 (Win 1603 / Loss 1718 / Flat 2008) / skip 5381件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,058.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$207.48** / 初期 $100.00 (+107.48%)
- 確定: 2743件 (Win 759 / Loss 642 / Flat 1342) / skip 4817件
- 成長率目線: 平均log +0.000266 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0980 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $207.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.14** / 初期 $100.00 (+22.14%)
- 確定: 2654件 (Win 783 / Loss 1012 / Flat 859) / pending 3件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000535 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.14

## 6. Latest Market Context

- 更新: 2026-09-10T03:36:04.248789+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=78313.7
- Funnel: target 1064 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VTHO/USDT:USDT | +56.85% | $2,129,723.74 |
| CATE/USDT:USDT | +32.42% | $2,970,752.32 |
| BTR/USDT:USDT | +23.69% | $2,849,684.32 |
| VET/USDT:USDT | +3.60% | $5,183,949.19 |
| MINA/USDT:USDT | +3.51% | $1,353,040.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALGO/USDT:USDT | below_1h_threshold | +0.89% | +0.90% |
| SOFTBANKSTOCK/USDT:USDT | below_1h_threshold | +0.83% | +0.85% |
| PI/USDT:USDT | below_1h_threshold | +0.73% | +0.74% |
| MINA/USDT:USDT | below_1h_threshold | +0.68% | +0.69% |
| BULLA/USDT:USDT | below_1h_threshold | +0.57% | +0.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
