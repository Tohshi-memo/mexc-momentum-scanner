# Decision Report

- generated_at: 2026-09-05T11:06:16.998951+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13728**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13728, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.26% | **-0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +0.72% | **+0.57%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.50% | **+0.40%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.83% | **+1.56%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.05% | **+1.54%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.70% | **+1.48%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.81% | **+0.98%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.17% | **+0.97%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$854.06** / 初期 $100.00 (+754.06%)
- 確定: 5034件 (Win 1517 / Loss 1646 / Flat 1871) / skip 5255件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $854.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.12** / 初期 $100.00 (+88.12%)
- 確定: 2473件 (Win 695 / Loss 587 / Flat 1191) / skip 4666件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0642 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $188.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.78** / 初期 $100.00 (+18.78%)
- 確定: 2353件 (Win 702 / Loss 901 / Flat 750) / pending 3件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $118.78

## 6. Latest Market Context

- 更新: 2026-09-05T11:06:07.165877+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=79618.8
- Funnel: target 1050 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +86.35% | $12,324,076.56 |
| 4/USDT:USDT | +62.88% | $19,513,041.10 |
| AKE/USDT:USDT | +43.60% | $15,811,546.08 |
| B/USDT:USDT | +38.33% | $2,781,478.29 |
| MARSCOIN/USDT:USDT | +37.84% | $8,288,547.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +3.67% | +3.62% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.48% | +1.43% |
| BTR/USDT:USDT | below_1h_threshold | +1.06% | +1.01% |
| UAI/USDT:USDT | below_1h_threshold | +0.98% | +0.94% |
| WLD/USDT:USDT | below_1h_threshold | +0.82% | +0.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
