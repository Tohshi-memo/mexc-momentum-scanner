# Decision Report

- generated_at: 2026-08-20T10:51:26.360231+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12035**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12035, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.70% | **-1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.02% | **+0.02%** |
| LIMIT_7PCT | 5/20 | 25.0% | -0.24% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +4.69% | **+2.58%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.99% | **+2.19%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.96% | **+1.59%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.14% | **+1.39%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.15** / 初期 $100.00 (+506.15%)
- 確定: 4250件 (Win 1304 / Loss 1390 / Flat 1556) / skip 4346件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $606.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3625件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.77** / 初期 $100.00 (+16.77%)
- 確定: 1756件 (Win 521 / Loss 671 / Flat 564) / pending 1件 / skip 1750件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000070 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `MARKET` EXPIRED account -0.00% 残高後 $116.77

## 6. Latest Market Context

- 更新: 2026-08-20T10:51:15.063277+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=71890.4
- Funnel: target 1005 → liquid 201 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.9 >= 65=1, 4h RSI 88.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +71.71% | $3,719,228.88 |
| BOME/USDT:USDT | +48.01% | $8,217,538.34 |
| MAGMA/USDT:USDT | +33.84% | $9,531,493.03 |
| USELESS/USDT:USDT | +23.71% | $2,063,155.13 |
| ORDI/USDT:USDT | +22.51% | $5,722,601.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BOME/USDT:USDT | below_1h_threshold | +3.94% | +3.78% |
| KAS/USDT:USDT | below_1h_threshold | +3.01% | +2.85% |
| ENA/USDT:USDT | below_1h_threshold | +2.84% | +2.68% |
| AVNT/USDT:USDT | below_1h_threshold | +2.82% | +2.66% |
| KORU/USDT:USDT | below_1h_threshold | +2.75% | +2.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
