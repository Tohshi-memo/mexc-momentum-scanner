# Decision Report

- generated_at: 2026-08-04T19:46:20.195253+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10316**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10316, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.48% | **-0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.64% | **+0.35%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.16% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.56% | **+0.48%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.30% | **+0.45%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.80% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$577.81** / 初期 $100.00 (+477.81%)
- 確定: 3726件 (Win 1179 / Loss 1222 / Flat 1325) / skip 3151件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $577.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2442件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0193 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.01** / 初期 $100.00 (+17.01%)
- 確定: 1074件 (Win 345 / Loss 415 / Flat 314) / pending 5件 / skip 711件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000291 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $117.01

## 6. Latest Market Context

- 更新: 2026-08-04T19:46:12.653727+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=64337.6
- Funnel: target 937 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +20.92% | $1,791,186.61 |
| BICO/USDT:USDT | +14.30% | $14,097,549.02 |
| COTI/USDT:USDT | +11.23% | $5,012,232.19 |
| PUMPFUN/USDT:USDT | +5.40% | $36,901,857.93 |
| HFT/USDT:USDT | +5.39% | $1,227,311.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.43% | +4.32% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.70% | +2.60% |
| AKE/USDT:USDT | below_1h_threshold | +2.68% | +2.57% |
| BLESS/USDT:USDT | below_1h_threshold | +2.48% | +2.38% |
| COTI/USDT:USDT | below_1h_threshold | +2.38% | +2.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
