# Decision Report

- generated_at: 2026-09-05T10:36:14.549720+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13727**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13727, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.26% | **-0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +1.35% | **+1.08%** |
| LIMIT_3PCT | 16/20 | 80.0% | +1.06% | **+0.85%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.32% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +3.14% | **+1.88%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.83% | **+1.56%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.46% | **+1.38%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.75% | **+1.37%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.67% | **+1.34%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$854.06** / 初期 $100.00 (+754.06%)
- 確定: 5033件 (Win 1517 / Loss 1646 / Flat 1870) / skip 5255件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $854.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.12** / 初期 $100.00 (+88.12%)
- 確定: 2472件 (Win 695 / Loss 587 / Flat 1190) / skip 4666件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0642 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: B/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $188.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.78** / 初期 $100.00 (+18.78%)
- 確定: 2352件 (Win 702 / Loss 901 / Flat 749) / pending 2件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $118.78

## 6. Latest Market Context

- 更新: 2026-09-05T10:36:04.702833+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=79583.9
- Funnel: target 1050 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +82.23% | $11,698,366.99 |
| 4/USDT:USDT | +66.00% | $19,376,402.20 |
| AKE/USDT:USDT | +43.72% | $15,505,861.65 |
| ICX/USDT:USDT | +38.88% | $1,024,225.58 |
| B/USDT:USDT | +37.95% | $2,667,817.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +4.77% | +4.79% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.74% | +3.75% |
| 4/USDT:USDT | below_1h_threshold | +3.22% | +3.23% |
| ICX/USDT:USDT | below_1h_threshold | +3.14% | +3.16% |
| AKE/USDT:USDT | below_1h_threshold | +2.67% | +2.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
