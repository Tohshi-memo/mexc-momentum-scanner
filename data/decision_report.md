# Decision Report

- generated_at: 2026-09-04T19:51:27.653476+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13660**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13660, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.26% | **+0.68%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_BB3S | 2/13 | 15.4% | +2.00% | **+0.31%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.44% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +2.03% | **+1.45%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.03% | **+1.32%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.93% | **+1.16%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.32% | **+1.13%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 201件 (TP 75 / SL 121 / EXP 5)
- 最新: UAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5011件 (Win 1516 / Loss 1644 / Flat 1851) / skip 5210件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.38** / 初期 $100.00 (+85.38%)
- 確定: 2422件 (Win 682 / Loss 577 / Flat 1163) / skip 4649件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0186 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.98** / 初期 $100.00 (+17.98%)
- 確定: 2299件 (Win 683 / Loss 881 / Flat 735) / pending 6件 / skip 2831件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000286 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $117.98

## 6. Latest Market Context

- 更新: 2026-09-04T19:51:16.509363+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=79680.0
- Funnel: target 1050 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +38.92% | $4,629,729.06 |
| MARSCOIN/USDT:USDT | +17.25% | $7,994,634.71 |
| UAI/USDT:USDT | +13.35% | $6,935,362.71 |
| NEAR/USDT:USDT | +11.84% | $19,480,169.17 |
| BASECAT/USDT:USDT | +9.31% | $1,831,874.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CP/USDT:USDT | below_1h_threshold | +3.35% | +3.22% |
| VVV/USDT:USDT | below_1h_threshold | +3.24% | +3.11% |
| BTR/USDT:USDT | below_1h_threshold | +3.22% | +3.09% |
| USELESS/USDT:USDT | below_1h_threshold | +2.55% | +2.42% |
| KORU/USDT:USDT | below_1h_threshold | +1.86% | +1.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
