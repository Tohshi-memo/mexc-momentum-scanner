# Decision Report

- generated_at: 2026-08-02T05:06:21.337069+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10145**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10145, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.65% | **-0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.22% | **+0.91%** |
| LIMIT_BB3S | 3/18 | 16.7% | +4.00% | **+0.67%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.83% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.55% | **+1.08%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.34% | **+0.81%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.85% | **+0.47%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.97% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$580.31** / 初期 $100.00 (+480.31%)
- 確定: 3664件 (Win 1165 / Loss 1198 / Flat 1301) / skip 3042件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $580.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1280件 (Win 359 / Loss 297 / Flat 624) / skip 2276件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0992 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$113.20** / 初期 $100.00 (+13.20%)
- 確定: 953件 (Win 304 / Loss 370 / Flat 279) / pending 3件 / skip 660件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000341 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $113.20

## 6. Latest Market Context

- 更新: 2026-08-02T05:06:14.170799+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=63491.5
- Funnel: target 922 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 1000RATS/USDT:USDT | +59.03% | $25,757,320.73 |
| BLESS/USDT:USDT | +35.65% | $8,322,060.54 |
| UAI/USDT:USDT | +29.78% | $20,961,719.56 |
| HOME/USDT:USDT | +24.82% | $1,212,220.57 |
| ON/USDT:USDT | +9.25% | $6,365,951.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZAMA/USDT:USDT | below_1h_threshold | +2.36% | +2.47% |
| BLESS/USDT:USDT | below_1h_threshold | +1.50% | +1.60% |
| HOME/USDT:USDT | below_1h_threshold | +0.70% | +0.80% |
| AVAX/USDT:USDT | below_1h_threshold | +0.59% | +0.69% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.57% | +0.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
