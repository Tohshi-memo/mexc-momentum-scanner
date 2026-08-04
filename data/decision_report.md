# Decision Report

- generated_at: 2026-08-04T23:01:25.441033+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10323**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10323, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.14% | **-0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +1.69% | **+1.27%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.90% | **+0.67%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.02% | **+0.61%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.49% | **+0.22%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.09% | **+3.09%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.44% | **+1.47%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.77% | **+1.06%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.93% | **+0.97%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.68% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$577.81** / 初期 $100.00 (+477.81%)
- 確定: 3726件 (Win 1179 / Loss 1222 / Flat 1325) / skip 3158件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $577.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2449件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0361 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1080件 (Win 347 / Loss 419 / Flat 314) / pending 2件 / skip 714件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000300 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-04T23:01:16.558696+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64212.6
- Funnel: target 937 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +33.19% | $3,675,843.71 |
| BICO/USDT:USDT | +27.63% | $14,478,345.76 |
| TAKE/USDT:USDT | +25.68% | $1,171,465.18 |
| HFT/USDT:USDT | +23.47% | $1,347,165.21 |
| PUMPFUN/USDT:USDT | +8.27% | $51,164,794.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HFT/USDT:USDT | below_1h_threshold | +1.31% | +1.35% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +0.93% | +0.97% |
| BICO/USDT:USDT | below_1h_threshold | +0.82% | +0.86% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.80% | +0.83% |
| NVIDIA/USDT:USDT | below_1h_threshold | +0.63% | +0.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
