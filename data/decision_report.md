# Decision Report

- generated_at: 2026-09-06T04:46:18.237625+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13796**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13796, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.61% | **+0.15%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.11% | **+0.08%** |
| LIMIT_BB3S | 4/14 | 28.6% | -0.05% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.72% | **+1.77%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.16% | **+1.62%** |
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +4.74% | **+1.58%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.38% | **+1.43%** |
| MARKET_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$862.96** / 初期 $100.00 (+762.96%)
- 確定: 5102件 (Win 1533 / Loss 1665 / Flat 1904) / skip 5255件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEC/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $862.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$192.26** / 初期 $100.00 (+92.26%)
- 確定: 2541件 (Win 710 / Loss 602 / Flat 1229) / skip 4666件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0582 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.68% 残高後 $192.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.02** / 初期 $100.00 (+20.02%)
- 確定: 2412件 (Win 719 / Loss 916 / Flat 777) / pending 1件 / skip 2854件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000206 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $120.02

## 6. Latest Market Context

- 更新: 2026-09-06T04:46:06.650466+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=79897.2
- Funnel: target 1050 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +46.75% | $128,027,652.48 |
| RAY/USDT:USDT | +36.76% | $1,858,097.44 |
| FLOCK/USDT:USDT | +23.35% | $1,105,749.48 |
| BASECAT/USDT:USDT | +22.59% | $2,155,877.42 |
| MAGMA/USDT:USDT | +15.37% | $2,582,878.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +4.00% | +4.12% |
| BASECAT/USDT:USDT | below_1h_threshold | +3.40% | +3.52% |
| DASH/USDT:USDT | below_1h_threshold | +3.27% | +3.39% |
| BULLA/USDT:USDT | below_1h_threshold | +2.54% | +2.65% |
| LIT/USDT:USDT | below_1h_threshold | +1.46% | +1.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
