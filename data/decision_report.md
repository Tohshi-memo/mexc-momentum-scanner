# Decision Report

- generated_at: 2026-08-20T10:56:26.425797+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12037**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12037, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.00% | **-0.00%** |
| LIMIT_7PCT | 5/20 | 25.0% | -0.24% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +4.69% | **+2.58%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +4.13% | **+2.48%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.96% | **+1.59%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.18% | **+1.53%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.15** / 初期 $100.00 (+506.15%)
- 確定: 4251件 (Win 1304 / Loss 1390 / Flat 1557) / skip 4347件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $606.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3627件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.69** / 初期 $100.00 (+16.69%)
- 確定: 1757件 (Win 521 / Loss 672 / Flat 564) / pending 0件 / skip 1751件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000070 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PUMPFUN/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $116.69

## 6. Latest Market Context

- 更新: 2026-08-20T10:56:16.319649+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=71871.2
- Funnel: target 1005 → liquid 201 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.3 >= 65=1, 4h RSI 88.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +73.18% | $3,851,169.54 |
| BOME/USDT:USDT | +47.90% | $8,432,651.32 |
| MAGMA/USDT:USDT | +35.40% | $9,608,313.02 |
| USELESS/USDT:USDT | +23.81% | $2,068,341.97 |
| ORDI/USDT:USDT | +23.32% | $5,894,858.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BOME/USDT:USDT | below_1h_threshold | +4.11% | +3.99% |
| CRV/USDT:USDT | below_1h_threshold | +3.14% | +3.01% |
| KAS/USDT:USDT | below_1h_threshold | +2.93% | +2.81% |
| KORU/USDT:USDT | below_1h_threshold | +2.75% | +2.62% |
| WIF/USDT:USDT | below_1h_threshold | +2.62% | +2.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
