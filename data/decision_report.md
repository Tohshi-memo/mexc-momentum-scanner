# Decision Report

- generated_at: 2026-08-04T16:11:27.898280+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10308**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10308, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.03% | **-1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.54% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.60% | **+1.28%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.61% | **+0.96%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +2.55% | **+0.64%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.02% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$577.81** / 初期 $100.00 (+477.81%)
- 確定: 3726件 (Win 1179 / Loss 1222 / Flat 1325) / skip 3143件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $577.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2434件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0172 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.41** / 初期 $100.00 (+16.41%)
- 確定: 1069件 (Win 342 / Loss 413 / Flat 314) / pending 4件 / skip 708件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000251 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.41

## 6. Latest Market Context

- 更新: 2026-08-04T16:11:19.251963+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=64012.7
- Funnel: target 937 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CASHCAT/USDT:USDT | +4.48% | $1,237,617.94 |
| 1000RATS/USDT:USDT | +2.86% | $13,944,708.03 |
| GIGGLE/USDT:USDT | +2.65% | $3,749,084.25 |
| HOME/USDT:USDT | +2.50% | $15,520,104.49 |
| CAP/USDT:USDT | +2.50% | $1,953,327.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +4.49% | +4.61% |
| 1000RATS/USDT:USDT | below_1h_threshold | +2.87% | +2.99% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.65% | +2.77% |
| CAP/USDT:USDT | below_1h_threshold | +2.51% | +2.63% |
| HOME/USDT:USDT | below_1h_threshold | +2.51% | +2.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
