# Decision Report

- generated_at: 2026-08-04T13:26:25.867521+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10299**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10299, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.36% | **-1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +3.63% | **+1.27%** |
| LIMIT_5PCT | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.14% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.19% | **+1.53%** |
| MARKET_LONG | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.46% | **+1.17%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$577.81** / 初期 $100.00 (+477.81%)
- 確定: 3726件 (Win 1179 / Loss 1222 / Flat 1325) / skip 3134件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $577.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1284件 (Win 359 / Loss 299 / Flat 626) / skip 2426件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0308 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HOME/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.23** / 初期 $100.00 (+17.23%)
- 確定: 1064件 (Win 342 / Loss 409 / Flat 313) / pending 5件 / skip 702件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000295 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $117.23

## 6. Latest Market Context

- 更新: 2026-08-04T13:26:18.372396+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=63911.6
- Funnel: target 937 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CYS/USDT:USDT | +70.18% | $9,425,747.62 |
| HOME/USDT:USDT | +42.38% | $12,647,456.80 |
| CASHCAT/USDT:USDT | +42.01% | $1,156,065.05 |
| BANK/USDT:USDT | +31.70% | $14,734,034.53 |
| SKYAI/USDT:USDT | +25.99% | $41,583,305.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.80% | +4.74% |
| BANK/USDT:USDT | below_1h_threshold | +3.83% | +3.77% |
| CYS/USDT:USDT | below_1h_threshold | +2.76% | +2.70% |
| COTI/USDT:USDT | below_1h_threshold | +2.58% | +2.52% |
| VELVET/USDT:USDT | below_1h_threshold | +2.50% | +2.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
