# Decision Report

- generated_at: 2026-07-14T02:41:08.484512+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8657**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8657, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.85% | **+0.77%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.84% | **+0.59%** |
| LIMIT_BB3S | 5/19 | 26.3% | +1.71% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.50% | **+1.27%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.29% | **+1.15%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$102.20** / 初期 $100.00 (+2.20%)
- 確定トレード: 95件 (TP 32 / SL 61 / EXP 2)
- 最新: O/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$329.26** / 初期 $100.00 (+229.26%)
- 確定: 2825件 (Win 887 / Loss 923 / Flat 1015) / skip 2393件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLAST/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $329.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.41** / 初期 $100.00 (+5.41%)
- 確定: 657件 (Win 156 / Loss 159 / Flat 342) / skip 1411件
- 成長率目線: 平均log +0.000080 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0171 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLAST/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.31** / 初期 $100.00 (-0.69%)
- 確定: 40件 (Win 14 / Loss 26 / Flat 0) / pending 0件 / skip 86件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000241 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLAST/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.31

## 6. Latest Market Context

- 更新: 2026-07-14T02:41:02.228816+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=62497.3
- Funnel: target 867 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +31.90% | $6,003,393.50 |
| EVAA/USDT:USDT | +20.22% | $22,224,958.21 |
| ZBT/USDT:USDT | +15.49% | $1,996,020.32 |
| BLAST/USDT:USDT | +13.14% | $1,685,424.01 |
| VELVET/USDT:USDT | +11.26% | $31,690,467.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +4.94% | +4.95% |
| BSB/USDT:USDT | below_1h_threshold | +3.87% | +3.88% |
| BLAST/USDT:USDT | below_1h_threshold | +2.66% | +2.68% |
| T/USDT:USDT | below_1h_threshold | +2.46% | +2.48% |
| CAP/USDT:USDT | below_1h_threshold | +1.61% | +1.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
