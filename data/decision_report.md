# Decision Report

- generated_at: 2026-08-20T10:41:30.025276+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12031**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12031, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.65% | **-1.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.02% | **+0.02%** |
| LIMIT_BB3S | 9/13 | 69.2% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +4.35% | **+2.39%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +4.65% | **+2.33%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.77% | **+1.94%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.39% | **+1.19%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.15** / 初期 $100.00 (+506.15%)
- 確定: 4248件 (Win 1304 / Loss 1390 / Flat 1554) / skip 4344件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $606.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3621件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.77** / 初期 $100.00 (+16.77%)
- 確定: 1755件 (Win 521 / Loss 670 / Flat 564) / pending 2件 / skip 1748件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000069 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `MARKET` EXPIRED account +0.01% 残高後 $116.77

## 6. Latest Market Context

- 更新: 2026-08-20T10:41:19.436040+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=71818.6
- Funnel: target 1005 → liquid 201 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.3 >= 65=1, 4h RSI 87.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +64.26% | $3,509,335.23 |
| BOME/USDT:USDT | +46.08% | $7,975,105.06 |
| MAGMA/USDT:USDT | +36.46% | $9,429,405.08 |
| USELESS/USDT:USDT | +23.66% | $2,052,656.47 |
| ORDI/USDT:USDT | +22.48% | $5,416,326.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KAS/USDT:USDT | below_1h_threshold | +2.97% | +2.92% |
| WIF/USDT:USDT | below_1h_threshold | +2.88% | +2.83% |
| KORU/USDT:USDT | below_1h_threshold | +2.75% | +2.70% |
| ENA/USDT:USDT | below_1h_threshold | +2.68% | +2.63% |
| BOME/USDT:USDT | below_1h_threshold | +2.56% | +2.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
