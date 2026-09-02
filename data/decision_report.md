# Decision Report

- generated_at: 2026-09-02T13:36:24.983306+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13336**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13336, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.89% | **-0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_BB3S | 9/17 | 52.9% | +1.14% | **+0.60%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.68% | **+0.38%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.47% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.57% | **+1.41%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.39% | **+1.19%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.67% | **+1.00%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +2.62% | **+0.66%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.89% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$838.59** / 初期 $100.00 (+738.59%)
- 確定: 4962件 (Win 1505 / Loss 1628 / Flat 1829) / skip 4935件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.82% 残高後 $838.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.36** / 初期 $100.00 (+74.36%)
- 確定: 2315件 (Win 643 / Loss 554 / Flat 1118) / skip 4432件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0514 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $174.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 0件 / skip 2711件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000185 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T13:36:17.217367+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=76667.1
- Funnel: target 1044 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| T/USDT:USDT | +51.78% | $11,507,662.76 |
| MAGMA/USDT:USDT | +45.36% | $10,888,648.72 |
| FONE/USDT:USDT | +40.89% | $1,888,603.30 |
| UAI/USDT:USDT | +20.83% | $29,325,493.29 |
| CASHCAT/USDT:USDT | +20.31% | $1,949,596.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.42% | +4.30% |
| SYRUP/USDT:USDT | below_1h_threshold | +2.14% | +2.02% |
| SILVER/USDT:USDT | below_1h_threshold | +1.55% | +1.43% |
| UAI/USDT:USDT | below_1h_threshold | +1.30% | +1.18% |
| PYTH/USDT:USDT | below_1h_threshold | +1.11% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
