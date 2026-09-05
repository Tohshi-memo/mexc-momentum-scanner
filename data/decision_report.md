# Decision Report

- generated_at: 2026-09-05T18:06:19.866915+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13767**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13767, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.65% | **-0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.86% | **+0.26%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.30% | **+0.21%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +0.35% | **+0.18%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$851.33** / 初期 $100.00 (+751.33%)
- 確定: 5073件 (Win 1521 / Loss 1654 / Flat 1898) / skip 5255件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $851.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.98** / 初期 $100.00 (+88.98%)
- 確定: 2512件 (Win 700 / Loss 592 / Flat 1220) / skip 4666件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0603 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $188.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.95** / 初期 $100.00 (+19.95%)
- 確定: 2385件 (Win 708 / Loss 904 / Flat 773) / pending 3件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000287 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.95

## 6. Latest Market Context

- 更新: 2026-09-05T18:06:06.213863+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80036.9
- Funnel: target 1050 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +21.31% | $24,723,360.01 |
| MAGMA/USDT:USDT | +19.75% | $2,183,687.52 |
| NIULAI/USDT:USDT | +14.75% | $2,657,998.25 |
| USELESS/USDT:USDT | +13.09% | $20,312,083.44 |
| BASECAT/USDT:USDT | +13.07% | $2,044,006.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASECAT/USDT:USDT | below_1h_threshold | +1.72% | +1.72% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.15% | +1.14% |
| USELESS/USDT:USDT | below_1h_threshold | +0.91% | +0.90% |
| PONS/USDT:USDT | below_1h_threshold | +0.77% | +0.77% |
| UNI/USDT:USDT | below_1h_threshold | +0.77% | +0.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
