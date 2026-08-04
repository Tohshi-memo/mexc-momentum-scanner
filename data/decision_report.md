# Decision Report

- generated_at: 2026-08-04T22:21:29.699448+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10319**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10319, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.24% | **-0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +1.06% | **+0.79%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.20% | **+0.66%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.34% | **+0.25%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.09% | **+3.09%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.21% | **+1.21%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.53% | **+0.84%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.68% | **+0.67%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.66% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$577.81** / 初期 $100.00 (+477.81%)
- 確定: 3726件 (Win 1179 / Loss 1222 / Flat 1325) / skip 3154件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $577.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2445件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0246 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.11** / 初期 $100.00 (+17.11%)
- 確定: 1076件 (Win 346 / Loss 416 / Flat 314) / pending 6件 / skip 714件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000375 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $117.11

## 6. Latest Market Context

- 更新: 2026-08-04T22:21:23.033987+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64200.4
- Funnel: target 937 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +29.69% | $3,396,266.04 |
| BICO/USDT:USDT | +24.90% | $14,416,530.05 |
| TAKE/USDT:USDT | +23.17% | $1,122,201.13 |
| HFT/USDT:USDT | +16.48% | $1,345,031.84 |
| COTI/USDT:USDT | +9.20% | $5,347,843.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +3.53% | +3.48% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.10% | +2.05% |
| TAKE/USDT:USDT | below_1h_threshold | +1.32% | +1.27% |
| CYS/USDT:USDT | below_1h_threshold | +1.23% | +1.18% |
| COTI/USDT:USDT | below_1h_threshold | +1.11% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
